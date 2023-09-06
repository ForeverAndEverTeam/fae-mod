default persistent._fae_game_db = dict()
default persistent._fae_mg_list = list()
default persistent.games_reset_redo = list()

init python in fae_games:

    import store

    persistent = renpy.game.persistent

    mg_list_redo = []
    persistent._fae_mg_list = mg_list_redo

init python:
    zorder_game = 4
    class minigame():
        
        def __init__(self, name, label = None, preparation = None):
            self.label = label
            self.name = name
            self.preparation = preparation
            self.available = True
        
        def __call__(self, *args, **kwargs):
            
            if self.preparation:
                self.preparation(self, *args, **kwargs)

            if self.label and not kwargs.get("restart"):
                renpy.call_in_new_context(self.label)
        
        def set_state(self, value):
            self.state = value
