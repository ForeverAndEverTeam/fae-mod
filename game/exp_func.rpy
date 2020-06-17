init -10 python:
    bg_day = False #Changed by '01bg.rpy', if the current BG has day/high light
    s_ypos = 0
    COLOR_STEP = (60.0**2)/255.0 #Time, needed for change a RBG value with get_time_transition_factor by 1
    
    if not persistent.customization:
        persistent.customization = {
            'hair': 'usual', # Hair Style
            'body': 'uniform', # Body Style
            'asec_head': None, # Head accessory (e.g. glasses)
        }

    import re
    
    SAYORI_IMAGES_PATH = 'mod_assets/images/s_newer'
    
    EXP_PATHS = {
        2: "skin", 
        3: "mouth", 
        4: "eyes", 
        5: "brows",
        8: "arms"
    }
    #Key = insert position
    CUSTOM_PATHS = {
        0: "hair_back",
        1: "body",
        7: "hair",
        9: "hair_front"
    }
    BG_PATHS = {
        6: "table"
    }
    SPR_PATHS = {}
    for i in range(10):
        SPR_PATHS[i] = EXP_PATHS.get(i) or CUSTOM_PATHS.get(i) or BG_PATHS.get(i)
        
    
    def get_asset_path(part, file = 'a', body = None, dark = False):
        if dark:
            file += "_d"
        path = ""
        if body:
            path = "%s/%s/%s/%s.png" % (SAYORI_IMAGES_PATH, part, body, file)
        else:
            path = "%s/%s/%s.png" % (SAYORI_IMAGES_PATH, part, file)
        try:
            #Check if the file is present
            f = renpy.file(path)
            f.close()
            return path
        except:
            raise IOError('File %s is not present' % path)
    
    def l_range(t, *args):
        """Creates a letter list. Uses a range()-like agrument syntax, but the result includes the last value."""
        al = len(args)
        f = 97
        s = args[1] if al > 1 else 1
        
        if al == 0:
            t = ord(t)
        else:
            f, t = ord(t), ord(args[0])
        
        return [chr(x) for x in range(f, t+1, s)]
    
    #Sprite Info Classes
    class SpriteInfo:
        def __init__(self, part, file, has_dark_version = False, body_depended = False, name = None, allowed = "*****"):
            self.part = part
            self.file = file
            self.body_depended = body_depended
            self.name = name
            self.allowed_temp = allowed #Template for expression codes where the sprite can be used
        
        def get_path(self, dark = False, body = None):
            return get_asset_path(self.part, self.file, body, dark)
            
        def get_image(self, body = None, dark = False):
            path = self.get_path(False, body)
            darkened = dark and self.get_path(True, body)
            if darkened:
                path = self.get_path(True, body)
            return path
        
        def allowed(self, code):
            #Template syntax:
            #* - any char
            #! - except the next char
            #{} - char group (any of these chars)
            t = self.allowed_temp
            tl, cl = len(t), len(code)
            if cl > 5:
                ph = '*'
                if t[0] != "*":
                    ph = "0"
                nl = 0
                while code[nl].isdigit():
                    nl += 1
                for i in range(nl-1):
                    code = ph + code
                tl = len(t)
            elif tl > 5:
                nl = 0
                while t[nl].isdigit():
                    nl += 1
                for i in range(nl):
                    code = '0' + code
                cl = len(code)
            code = code.ljust(tl)
            not_next = False
            in_group = False
            group_ok = False
            d = 0
            for i in range(tl):
                if in_group:
                    if (t[i] == code[i-d]):
                        group_ok = True
                    if (t[i] == '}'):
                        in_group = False
                        if not_next:
                            if group_ok:
                                return False
                        elif not group_ok:
                            return False
                        not_next = False
                    d += 1
                elif not_next:
                    if t[i] == code[i-d]:
                        return False
                    elif t[i] == '{':
                        in_group = True
                    else:
                        not_next = False
                elif t[i] == '{':
                    in_group = True
                    d += 1
                elif t[i] == '!':
                    not_next = True
                    d += 1
                elif not (t[i] == '*' or t[i] == code[i-d]):
                    return False
            return True
    
    class DummySprite(SpriteInfo):
        def __init__(self):
            self.part = None
            self.file = None
            self.body_depended = False
            self.name = None
            self.allowed_temp = "*****"
        
        def get_path(self, *args):
            return ""
        
        def get_image(self, *args):
            return im.Composite((0,0))

    
    exp_codes = [{}, {}, {}, {}, {}] ## Updated by sprites.rpy
    
    CUSTOM_TEMPLATES = {
        'hair': {},
        'hair_front': {},
        'hair_back': {},
        'body': {}
    }
    
    def get_custom(t, name):
        if not (t is None or name is None):
            return CUSTOM_TEMPLATES[t].get(name)
    
    def sayori_compose(exp_code, bg_loaded = False):
        sprites = []
        # print exp_code
        arms = exp_code[:-4]
        exp = exp_code[-4:]
        exp_i = 0
        for pos in SPR_PATHS:
            ek = SPR_PATHS[pos]
            sprites.append((0,0))
            if pos == 8: #Arm key
                sprites.append(exp_codes[0][arms].get_image(custom_current['body']))
            elif pos in EXP_PATHS:
                spr_cat = exp_codes[exp_i+1]
                if pos == 2: #Skin key
                    eyes_code = exp[2]
                    spr = spr_cat.get(exp[exp_i]+eyes_code) or spr_cat[exp[exp_i]]
                elif pos == 4: #Eyes key
                    skin_code = exp[0]
                    spr = spr_cat.get(exp[exp_i]+skin_code) or spr_cat[exp[exp_i]]
                else:
                    spr = spr_cat[exp[exp_i]]
                sprites.append(spr.get_image())
                exp_i+=1
            elif pos in CUSTOM_PATHS:
                sprites.append(CUSTOM_TEMPLATES[ek][custom_current[ek]].get_image())
            elif bg_loaded:
                sprites.append(backgrounds.current.sprites[ek].get_image())
            else:
                del sprites[-1]
        # print sprites
        return im.Composite((1280, 720), *sprites)
    
    s_last_frames = []
    def dyn_s(st, at, exp, *args, **kwargs):
        spr = composed_sprites[exp]
        frame = backgrounds.current.apply_current_matrix(spr)
        return frame, COLOR_STEP
    def make_dyn_s(from_what):
        return DynamicDisplayable(dyn_s, from_what)

init -8 python: ## new_exp.rpy code must have order -10<x<-8
    custom_current = {}
    composed_sprites = {}
    for k in CUSTOM_TEMPLATES:
        custom_current[k] = persistent.customization.get(k) or "usual"
    
    def exp_allowed(code):
        if not exp_codes[0][code[:-4]].allowed(code):
            return False
        for i in range(1, 5):
            if not exp_codes[i][code[-5+i]].allowed(code):
                return False
        return True
    
    def load_all_exps(ignore_allowed = False):
        exps = []
        #Use recursion to defind all the possible expressions
        def rec_add_exp(code, depth = 1):
            if depth >= 5:
                if ignore_allowed or exp_allowed(code):
                    exps.append(code)
                    return code
                return None
            for c in exp_codes[depth]:
                if len(c) == 1:
                    rec_add_exp(code + c, depth + 1)
                else:
                    return None
        #Expression loading for each arms
        for arms in exp_codes[0]:
            if arms.isdigit(): #To exclude special expressions if they accidentally are in the generic arm list
                rec_add_exp(arms)
        return exps
    
    def load_exps_from_lines(lines):
        exps = []
        for line in lines:
            limit = re.search('\s', line)
            limit = limit and limit.start() or len(line)
            exps.append(line[:limit])
        return exps
    
    def load_exps_from_file(file = 'exp.txt', close = False):
        if type(file) == str:
            file = renpy.file(file)
            close = True
        exps = load_exps_from_lines(file.readlines())
        if close:
            file.close()
        return exps
    
    def compile_exps(exps):
        for exp in exps:
            composed_sprites[exp] = sayori_compose(exp)
            renpy.image("sayori "+ exp, make_dyn_s(exp))
    
    def recompose_exps(bg_loaded = True):
        for exp in composed_sprites:
            composed_sprites[exp] = sayori_compose(exp, bg_loaded)

    exps = []
    exps_optimized = False
    try:
        exps = load_exps_from_file()
        exps_optimized = True
    except:
        print "WARNING: Error while loading 'exp.txt'. The game will define EVERY possible expression for safe loading in cost of VERY LONG load time."
        exps = load_all_exps()
    compile_exps(exps)