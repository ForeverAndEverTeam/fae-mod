default persistent.current_bg = 'spaceroom'
default persistent.static_bg = False
default persistent.day_night_cycle = 2
default matrix_mix_times = 0

#Spaceroom displayables
image sroom_night_static = "mod_assets/images/bg/spaceroom_static.png"
image mask_child:
    "images/cg/monika/child_2.png"
    xtile 2

image mask_mask:
    "images/cg/monika/mask.png"
    xtile 3

image mask_mask_flip:
    "images/cg/monika/mask.png"
    xtile 3 xzoom -1

image maskb:
    "images/cg/monika/maskb.png"
    xtile 3
  

image mask_test = AnimatedMask("#ff6000", "mask_mask", "maskb", 0.10, 32)
image mask_test2 = AnimatedMask("#ffffff", "mask_mask", "maskb", 0.03, 16)
image mask_test3 = AnimatedMask("#ff6000", "mask_mask_flip", "maskb", 0.10, 32)
image mask_test4 = AnimatedMask("#ffffff", "mask_mask_flip", "maskb", 0.03, 16)

transform bg_alpha(t = 1.0, x = 0, y = 0):
    xpos x
    ypos y
    alpha t
    linear COLOR_STEP alpha (t + 1/255)

image dclouds:
    DynamicDisplayable(dyn_clouds)
    xtile 3 subpixel True
    block:
        xoffset 1280
        linear 600 xoffset 0
        repeat


image mask_2:
    "images/cg/monika/mask_2.png"
    xtile 3 subpixel True
    block:
        xoffset 1280
        linear 1200 xoffset 0
        repeat

image mask_3:
    "images/cg/monika/mask_3.png"
    xtile 3 subpixel True
    block:
        xoffset 1280
        linear 180 xoffset 0
        repeat

image monika_room = "mod_assets/images/bg/spaceroom.png"
#image monika_room_highlight:
#    "images/cg/monika/monika_room_highlight.png"
#    function monika_alpha
#
#
image room_glitch = "images/cg/monika/monika_bg_glitch.png"
image rm = LiveComposite((1280, 720), (0, 0), "mask_test", (0, 0), "mask_test2", pos = (0,380), zoom = 0.25)
image rm2 = LiveComposite((1280, 720), (0, 0), "mask_test3", (0, 0), "mask_test4", pos = (600,380), zoom = 0.25)
image sroom_night_mask = LiveComposite((1280, 720), (0, 0), "mask_2", (0, 0), "mask_3", (0, 0), "rm",  (0, 0), "rm2")

init -8 python:
    def mix(a, b, c):
        """Mix b into a in the relation of c"""
        try:
            r = []
            for i in range(min(len(a), len(b))):
                r.append(mix(a[i], b[i], c))
            return r
        except TypeError:
            return a*(1-c) + b*c
    
    sky = Solid("#fff") #Universal sky image
        
    def get_sky_color(tod, tr = 0):
        sky = None
        if tod == 0:
            sky = (0x1c, 0x1c, 0x1d)
        elif tod == 1:
            sky = (0xff ,0xc6, 0x89)
        elif tod == 2:
            sky = (0x93, 0xc6, 0xf6)
        else:
            sky = (0xff, 0xa8, 0x98)
        if tr > 0:
            next_sky = get_sky_color((tod + 1) % 4, 0)
            return mix(sky, next_sky, tr)
        return sky 
    
    def dyn_sky(st, at, *args, **kwargs):
        tr = get_time_transition_factor()
        color = get_sky_color(get_time_of_day(for_bg = True), tr)
        color = "#%02x%02x%02x" % tuple(color)
        sky.color = Color(color)
        return sky, COLOR_STEP
    
    def dyn_clouds(st, at, *args, **kwargs):
        im = Image("images/cg/monika/mask.png")
        return backgrounds.current.apply_current_matrix(im), COLOR_STEP
    
    class Background:
        defualt_matrix = im.matrix((
    1,0,0,0,0,
    0,1,0,0,0,
    0,0,1,0,0,
    0,0,0,1,0))
        def __init__(self, code, name, constructor = None, destructor = None):
            self.code = code
            self.sprites = {
                "table": SpriteInfo("table", code)
            }
            self.name = name
            self.constructor = constructor
            self.destructor = destructor
            self.matrices = [self.defualt_matrix] * 4 #[night,morning,day,evening]
            self.shown = False
            self.static = None
        
        def show(self, static = False, nc = False):
            if self.shown and static == self.static:
                return None
            if not self.constructor:
                raise ValueError("BG constructor must be definded")
            elif callable(self.constructor):
                self.shown = True
                self.static = static
                s_recompose()
                return self.constructor(self, static)
            else:
                self.shown = True
                self.static = static
                if nc:
                    renpy.call_in_new_context(self.constructor, self, static)
                else:
                    renpy.call(self.constructor, self, static)
            s_recompose()
        
        def hide(self, nc = False):
            if not self.constructor:
                raise ValueError("BG destructor must be definded")
            elif callable(self.destructor):
                self.shown = False
                self.static = None
                return self.destructor(self)
            else:
                self.shown = False
                self.static = None
                if nc:
                    renpy.call_in_new_context(self.destructor, self, static)
                else:
                    renpy.call(self.destructor)
        
        def get_current_matrix(self):
            global matrix_mix_times
            tr = get_time_transition_factor()
            cm = self.matrices[get_time_of_day(for_bg = True)]
            if tr == 0:
                return cm
            else:
                nm = self.matrices[(get_time_of_day(for_bg = True) + 1) % 4]
                matrix_mix_times += 1
                if matrix_mix_times % 500 == 0:
                    renpy.free_memory() #Memory optimization
                return mix(cm, nm, tr)
        
        def apply_current_matrix(self,img,**props):
            return im.MatrixColor(img,self.get_current_matrix(),**props)
    
    class BGList:
        def __init__(self):
            self.bgs = {}
            self.current_id = None
        
        def __setattr__(self, attr, value):
            if attr == 'current':
                persistent.current_bg = value
            else:
                self.__dict__[attr] = value
        
        def __getattr__(self, attr):
            if attr == 'current':
                return persistent.current_bg
        
        def __getitem__(self, index):
            return self.bgs[index]
        
        def __setitem__(self, index, value):
            self.bgs[index] = value
        
        def __iter__(self):
            return iter(self.bgs)
        
        def show(self, id = None, static = None, nc = False):
            if id == None:
                id = self.current_id
            if static is None:
                static = persistent.static_bg
            
            #if self.bgs[self.current].shown:
            #   self.bgs[self.current].hide() 
            
            r = self.bgs[id].show(static, nc)
            self.current_id = id
            return r
        
        def hide_current(self, change = False):
            if not self.current:
                raise ValueError("None BG is shown")
            r = self.current.hide()
            if not change:
                self.current = None
            return r
        
        @property
        def current(self):
            return self.bgs[self.current_id]
    
    backgrounds = BGList()
    #Matrix ID constants
    ID_NIGHT, ID_MORNING, ID_DAY, ID_EVENING = 0, 1, 2, 3
    
    #Spaceroom initialization
    def sroom_dyn(st, at, *args, **kwargs):
        bg = kwargs["bg"]
        frame = bg.apply_current_matrix("mod_assets/images/bg/spaceroom.png")
        return frame, COLOR_STEP
    
    def sroom_mix_f (trans, st, at):
            op, tod, tr = 0.0, get_time_of_day(for_bg = True), get_time_transition_factor()
            if tod == 0:
                op = 1.0
            elif tod < 3:
                op = 0.0
            else:
                op = 4 * max(0, tr - 0.75)
            trans.alpha = op
            return COLOR_STEP

    def sroom_mix_fday (trans, st, at):
            op, tod, tr = 0.0, get_time_of_day(for_bg = True), get_time_transition_factor()
            if tod == 0:
                op = 0.0
            elif tod < 3:
                op = 1.0
            else:
                op = 1.0 - tr
            trans.alpha = op
            return COLOR_STEP
            
    def sroom_c(self, static = False):
        dsky = DynamicDisplayable(dyn_sky)
        renpy.show("bg", what = dsky, layer = 'bg', zorder = 0)
        if not static:
            renpy.show('dclouds', at_list = [Transform(function = sroom_mix_fday)], layer = 'bg')
            renpy.show('sroom_night_mask', at_list = [Transform(function = sroom_mix_f)], layer = 'bg')
        else:
            renpy.show('sroom_night_static', at_list = [Transform(function = sroom_mix_f)], layer = 'bg')
        droom = DynamicDisplayable(sroom_dyn, bg = self)
        renpy.show("bg_room", what = droom, layer = 'bg', zorder = 2)
        
    def sroom_d(self):
        renpy.scene('bg')
    
    backgrounds['spaceroom'] = Background("spaceroom", "Spaceroom", sroom_c, sroom_d)
    
    backgrounds['spaceroom'].matrices[ID_NIGHT] = im.matrix((
    0.3,0.1,0,0,0,
    0.075,0.4,0,0,0,
    0.075,0,0.55,0,0,
    0,0,0,1,0))
    day_m = backgrounds['spaceroom'].matrices[ID_DAY]
    backgrounds['spaceroom'].matrices[ID_MORNING] = mix(day_m, im.matrix.tint(1, 0.7, 0), 0.3)
    backgrounds['spaceroom'].matrices[ID_EVENING] = mix(day_m, im.matrix.tint(1, 0.784, 0.596), 0.3)
    backgrounds.current_id = "spaceroom"
