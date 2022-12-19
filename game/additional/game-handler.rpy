default persistent._fae_game_db = dict()


init -10 python in fae_games:
    import store

    def is_platform_good_for_chess():
        import platform
        import sys

        if sys.maxsize > 2**32:
            return platform.system() == 'Windows' or platform.system() == 'Linux' or platform.system() == 'Darwin'

        else:
            return platform.system() == 'Windows'

init python in fae_games:

    import store

    mg_list = []

init python:
    zorder_game = 4
    class minigame():
        
        def __init__(self, name, label = None, preparation = None):
            self.label = label
            self.name = name
            self.preparation = preparation
            self.available = True
        
        def __call__(self, *args, **kwargs):
            #global justIsSitting
            
            if self.preparation:
                self.preparation(self, *args, **kwargs)
            #justIsSitting = False
            if self.label and not kwargs.get("restart"):
                renpy.call_in_new_context(self.label)
        
        def set_state(self, value):
            self.state = value
    
    #mg_list = [] #mini-game list