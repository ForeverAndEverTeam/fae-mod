init -10 python:
    import re
    
    MOD_IMAGES_PATH = 'mod_assets/images'
    
    EXP_PATHS = {
        0: "s_new/body",
        1: "s_new/skin",
        2: "s_new/mouth",
        3: "s_new/eyes",
        4: "s_new/brows"
    }
    
    def get_asset_path(part, file = 'a'):
        """Part codes:
            0 = body
            1 = skin modification
            2 = mouth
            3 = eyes
            4 = eyebrows
        """
        return "%s/%s/%s.png" % (MOD_IMAGES_PATH, EXP_PATHS[part], file)
    
    def l_range(t, *args):
        al = len(args)
        f = 97
        s = args[1] if al > 1 else 1
        
        if al == 0:
            t = ord(t)
        else:
            f, t = ord(t), ord(args[0])
        
        return [chr(x) for x in range(f, t, s)]

    class SpriteInfo:
        def __init__(self, part, filename, pos, size = None):
            self.path = get_asset_path(part, filename)
            self.pos = pos
            self.size = size
        
        def __str__(self):
            return str(self.pos) + ', "%s"' % self.path
    
    class DummySprite(SpriteInfo):
        def __init__(self):
            self.path = ""
            self.pos = (0, 0)
            self.size = (0, 0)
    
        
        def __str__(self):
            return str(self.pos) + ', "%s"' % self.path

    
    exp_codes = [{}, {}, {}, {}] ## Updated by sprites.rpy
    
    class Body:
        def __init__(self, back, front = None):
            self.back = back
            self.front = front or []
        
        def add_front(self, sprite):
            self.front.append(sprite)
        
        def get_composite(self, exp_code = ""):
            comp_arg = [self.back.size, self.back.pos, self.back.path]
            for i in range(len(exp_code)):
                exp = exp_codes[i][exp_code[i]]
                if len(exp.path):
                    comp_arg.append(exp.pos)
                    comp_arg.append(exp.path)
            for i in self.front:
                if len(i.path):
                    comp_arg.append(i.pos)
                    comp_arg.append(i.path)
            
            #hair
            comp_arg.insert(3, (333, 0))
            comp_arg.insert(4, "mod_assets/images/s_new/hair/usual.png")
            
            return im.Composite(*comp_arg)
         
    bodies = {} ## Updated by new_exp.rpy

init -8 python: ## new_exp.rpy code must have order -10<x<-8
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
        dl = len(exp) - 4
        body = exp[:dl]
        renpy.image("sayori "+ exp, bodies[body].get_composite(exp[dl:]))
