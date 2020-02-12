init -10 python:
    bg_day = False #Changed by '01bg.rpy', if the current BG has day/high light
    s_ypos = 0
    COLOR_STEP = 60**2/255 #Time, needed for change a RBG value with get_time_transition_factor by 1
    
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
        7: "arms"
    }
    #Key = insert position
    CUSTOM_PATHS = {
        0: "hair_back",
        1: "body",
        6: "hair",
        8: "hair_front"
    }
    BG_PATHS = {
        6: "table"
    }
    SPR_PATHS = {}
    for i in range(8):
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
        def __init__(self, part, file, has_dark_version = False, body_depended = False, name = None):
            self.part = part
            self.file = file
            self.body_depended = body_depended
            self.name = name
        
        def get_path(self, dark = False, body = None):
            return get_asset_path(self.part, self.file, body, dark)
            
        def get_image(self, body = None, dark = False):
            path = self.get_path(False, body)
            darkened = dark and self.get_path(True, body)
            if darkened:
                path = self.get_path(True, body)
            return path
    
    class DummySprite(SpriteInfo):
        def __init__(self):
            self.part = None
            self.file = None
            self.body_depended = False
            self.name = None
        
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
    
    def sayori_compose(exp_code):
        sprites = []
        print(exp_code)
        arms = exp_code[:-4]
        exp = exp_code[-4:]
        exp_i = 0
        for pos in SPR_PATHS:
            ek = SPR_PATHS[pos]
            sprites.append((0,0))
            if pos == 7:
                sprites.append(exp_codes[0][arms].get_image(custom_current['body']))
            elif pos in EXP_PATHS:
                sprites.append(exp_codes[exp_i+1][exp[exp_i]].get_image())
                exp_i+=1
            elif pos in CUSTOM_PATHS:
                sprites.append(CUSTOM_TEMPLATES[ek][custom_current[ek]].get_image())
            else:
                sprites.append(backgrounds.current.sprites[ek])
        return im.Composite((1280, 720), *sprites)
    
    s_last_frames = []
    def make_dyn_s(from_what):
        def dyn_s(st, at, *args, **kwargs):
            frame = backgrounds.current.apply_current_matrix(from_what)
            return frame, COLOR_STEP
        return DynamicDisplayable(dyn_s)

init -8 python: ## new_exp.rpy code must have order -10<x<-8
    custom_current = {}
    composed_sprites = {}
    for k in CUSTOM_TEMPLATES:
        custom_current[k] = persistent.customization.get(k) or "usual"
    exps = []
    try:
        f = renpy.file('exp.txt')
        for line in f.readlines():
            limit = re.search('\s', line)
            limit = limit and limit.start() or len(line)
            exps.append(line[:limit])
        f.close()
    except:
        for body in bodies:
            for s in exp_codes[0]:
                for m in exp_codes[1]:
                    for e in exp_codes[2]:
                        for b in exp_codes[3]:
                            exps.append(body+s+m+e+b)
    
    for exp in exps:
        composed_sprites[exp] = sayori_compose(exp)
        renpy.image("sayori "+ exp, make_dyn_s(composed_sprites[exp]))
    
    def recompose_s():
        for exp in composed_sprites:
            composed_sprites[exp] = sayori_compose(exp)
