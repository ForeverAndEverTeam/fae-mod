default persistent.current_bg = 'spaceroom'
default persistent.static_bg = False

#Spaceroom displayables

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

image monika_room = "images/cg/monika/monika_room.png"
image monika_room_highlight:
    "images/cg/monika/monika_room_highlight.png"
    function monika_alpha


image room_glitch = "images/cg/monika/monika_bg_glitch.png"

image rm = LiveComposite((1280, 720), (0, 0), "mask_test", (0, 0), "mask_test2", pos = (0,380), zoom = 0.25)
image rm2 = LiveComposite((1280, 720), (0, 0), "mask_test3", (0, 0), "mask_test4", pos = (600,380), zoom = 0.25)

image monika_room_static = "mod_assets/images/bg/spaceroom_bg.png"

init -8 python:
    class Background:
        def __init__(self, constructor = None, destructor = None):
            self.constructor = constructor
            self.destructor = destructor
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
                return self.constructor(static)
            else:
                self.shown = True
                self.static = static
                if nc:
                    renpy.call_in_new_context(self.constructor, static)
                else:
                    renpy.call(self.constructor, static)
        
        def hide(self, nc = False):
            if not self.constructor:
                raise ValueError("BG destructor must be definded")
            elif callable(self.destructor):
                self.shown = False
                self.static = None
                return self.destructor()
            else:
                self.shown = False
                self.static = None
                if nc:
                    renpy.call_in_new_context(self.destructor, static)
                else:
                    renpy.call(self.destructor)
    
    class BGList:
        def __init__(self):
            self.bgs = {}
        
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
                id = self.current
            if static is None:
                static = persistent.static_bg
            
            #if self.bgs[self.current].shown:
            #   self.bgs[self.current].hide() 
            
            r = self.bgs[id].show(static, nc)
            self.current = id
            return r
        
        def hide_current(self, change = False):
            if not self.current:
                raise ValueError("None BG is shown")
            r = self.bgs[self.current].hide()
            if not change:
                self.current = None
            return r
    
    backgrounds = BGList()
    
    def sroom_c(static = False):
        if static:
            renpy.show('monika_room_static', layer = 'bg')
        else:
            renpy.show('mask_2', layer = 'bg')
            renpy.show('mask_3', layer = 'bg')
            renpy.show('rm', layer = 'bg')
            renpy.show('rm2', layer = 'bg')
            renpy.show('monika_room', layer = 'bg')
            renpy.show('monika_room_highlight', layer = 'bg')
    def sroom_d():
        renpy.scene('bg')
    
    backgrounds['spaceroom'] = Background(sroom_c, sroom_d)
    
