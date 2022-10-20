init -1 python in fae_dev_tools:

    import store
    import datetime
    import collections

    def glitchtext(length):

        import random

        output = ""
        for x in range(length):
            output += random.choice(chaos)
        return output
    

    def breakfile(filepath, break_length=1000):

        import struct

        bad_text = glitchtext(break_length)
        bad_text = [ord(x) for x in bad_text]
        bad_text = struct.pack("{0}i".format(break_length), *bad_text)
        with open(filepath, "wb") as s_file:
            s_file.write(bad_text)
    

    def completeResetData():


        import datetime

        renpy.game.persistent._seen_ever = dict()

        renpy.game.persistent.playername = ""
        renpy.game.persistent.playthrough = 0
        renpy.game.persistent.yuri_kill = 0
        renpy.game.persistent.clear = [False] * 10
        renpy.game.persistent.special_poems = None
        renpy.game.persistent.clearall = None
        renpy.game.persistent.first_load = None


        renpy.game.persistent._event_db = dict()
        renpy.game.persistent._farewell_db = dict()
        
        renpy.game.persistent.sessions={
            'last_session_end':datetime.datetime.now(),
            'current_session_start':datetime.datetime.now(),
            'total_playtime':datetime.timedelta(seconds=0),
            'total_sessions':0,
            'first_session':datetime.datetime.now()
        }

        renpy.game.persistent._fae_player_pronouns = None

        renpy.game.persistent._fae_affection["affection"] = 0

        renpy.game.persistent._fae_chess_stats = {
            "wins": 0,
            "losses": 0,
            "draws": 0,
            "practice_wins": 0,
            "practice_losses": 0,
            "practice_draws": 0
        }

    
    def initialSessionData():
        """
        Completely resets session data to usable initial values.
        NOTE: these are not the defaults, but rather what they would be set to
        on a first load.
        """
        store.persistent.sessions = {
            "last_session_end": None,
            "current_session_start": datetime.datetime.now(),
            "total_playtime": datetime.timedelta(seconds=0),
            "total_sessions": 1,
            "first_session": datetime.datetime.now()
        }


define config.allow_skipping = True
define config.developer = True
