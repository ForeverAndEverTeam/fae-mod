default persistent._farewell_db = dict()

default persistent.fae_first_leave_response = None

default persistent.fae_force_quit_state = 1


init -1 python in fae_farewells:
    from Enum import Enum
    import random
    import store
    import store.fae_affection as fae_affection
    import store.fae_globals as fae_globals
    #import store.fae_globals as fae_globals
    import store.fae_utilities as fae_utilities

    from store import Affection

    #from store import 

    FAREWELL_DEFS = dict()

    class FAEFirstQuitCats(Enum):

        will_return = 1
        unsure = 2
        silent = 3
        force_quit = 4

        def __int__(self):
            return self.value
        
    class FAEForceQuitStates(Enum):

        not_force_quit = 1
        first_force_quit = 2
        has_force_quit = 3

        def __int__(self):
            return self.value

    def load_farewell_choices():

        return [
            ("I'm going to sleep.", "farewell_sleep"),
            ("I'm going to school.", "farewell_school"),
            ("I'm going to play a game", "farewell_game"),
            ("I'm going to eat", "farewell_eat"),
            ("I'm going to work out", "farewell_exercise"),
            ("I'm going to work", "farewell_work"),
            ("I'm going to {b}die{/b}", "farewell_die")
        ]
    
    def farewell_pick():

        if store.persistent.fae_first_leave_response is None:

            return "first_leave"
        
        kwargs = dict()

        farewell_pool = store.Chat.chat_filt(
            FAREWELL_DEFS.values(),
            affection=Affection._getAffectionStatus(),
            **kwargs
        )

        return random.choice(farewell_pool).label


label farewell_init:

    $ ats(fae_farewells.farewell_pick())
    jump cnc

label farewell_force_quit:

    $ persistent.fae_force_quit_state = int(fae_farewells.FAEForceQuitStates.first_force_quit)
    if not persistent.fae_first_leave_response:
        $ persistent.fae_first_leave_response = int(fae_farewells.FAEFirstQuitCats.force_quit)

    hide screen hidden1
    stop music

    return { "quit": None }


label farewell_options:
    python:
        selectable_leave_options = fae_farewells.load_farewell_choices()
        selectable_leave_options.sort(key = lambda option: option[0])
        selectable_leave_options.append(("Goodbye.", "farewell_init"))
    
    call screen neat_menu_scroll(selectable_leave_options, ("Nevermind.", None))

    if isinstance(_return, basestring):
        show sayori idle at t11 zorder fae_sprites.FAE_SAYORI_ZORDER
        $ ats(_return)
        jump cnc
    
    jump ch30_loop

label first_leave:

    s "See ya"
    return { "quit": None }


#Farewells
label s_farewell_1: #The actual first farewell of this mod
    
    s abhfbaoa "Oh, are you heading out, [player]?" 
    s abhfbcoa "I'll see you later, then! Be safe out there!"
    return "quit"

label s_farewell_2:
    s "Goodbye, [player]!"
    s "You can always visit whenever you want."
    s abfdbaoa "I'll always be here to spend time with you!"
    return "quit"

label s_farewell_3:
    s "Bye, [player]!"
    s abgcbcqa "I’ll see you soon!"
    return "quit"

label s_farewell_4:
    s "Bye-bye!"
    s "I'll be wishing you health and happiness!"
    s abhebaka "Be safe out there, okay, [player]? Ehehe~"
    return "quit"

label s_farewell_5:
    if get_time_of_day() == 0:
        s abhfbaaa "Goodnight, [player]!"
        s fbhabica "Make sure you get enough sleep so you aren't all grumpy when you wake up, okay?"
    elif get_time_of_day() < 3:
        s abhfbaaa "Have a good day, [player]!"
        s abhfbaaa "I hope you can accomplish all of your goals for today, whether they're big or small, I'll be proud of you either way!"
    else:
        s abhfbaaa "See you later, [player]!"
        if get_time_of_day(launch_dt.hour) == 3:
            s "I'm glad you were able to spend some of your evening with me!"
        else:
            s "I'm glad you were able to spend the day with me!"
    return "quit"

label s_farewell_6:
    s "Bye, [player]!"
    s fbhabica "And don't forget to make sure that you're taking good care of yourself!"
    s abagbcaa "I want you to come back and be safe and sound, okay?"
    return "quit"

label s_farewell_7:
    s "See you later, [player]!"
    s abfbbaha "I wish I could give you a little farewell hug..."
    s abfdbcqa "But as long as you know that I would, I’m happy, ehehe~"
    return "quit"

REASON-BASED FAREWELLS

label s_farewell_school:
    s abhfaoa "Oh, time for school, [player]?"
    s abfccaa "I hope you have a good day!"
    s abfcaoa "See you later!"
    return "quit"

label s_farewell_school:
    s abhfaoa "Oh, time for work, [player]?"
    s abfccaa  "I hope everything goes smoothly for you today!"
    s abfcaoa "See you later!"
    return "quit"


label s_farewell_chores:
    s abhfaoa "Got some housework to take care of, [player]?"
    s abfccaa  "Take your time, I hope it all goes well!" 
    s abfcaoa "I’ll See you soon!"
    return "quit"

label s_farewell_eat:
    s abhfaoa  "Going to eat, [player]?" 
    s abfccma "I was getting pretty hungry myself, I think I’ll have some cookies!" 
    s abfcaoa "Enjoy your food! Hehehe~" 
    return "quit" 

label s_farewell_work_out:
    s abhfaoa "Ooooh! Wanna work out a bit [player]?"
    s abfccaa "I’m so glad you’re taking care of yourself!" 
    s abfcaoa "I hope you have fun! Bye-bye!" 
    return "quit"

label s_farewell_sleep:
    s abhfaoa  "Heading to bed, [player]?"
    s abhfcaa  "Hope you have a good night’s sleep!"
    if Affection.isEnamored:
        s abhebob "...can I have a goodnight kiss? Ehehehe~"
        menu: 
            "Sure, Sayori":
                s abgcceb "Yay!"
                call fae_kiss_short
            "Another time":
                s bbhfbaa "Alright then…"
    s abfcaaa "Sweet dreams, [player]!"
    return "quit"

label s_farewell_study:
    s abhfaoa "Got some studying to do, [player]?"
    s abfccaa "Make sure to take plenty of breaks in between!"
    s abfcaoa "You’ve got this, I believe in you!"
    return "quit"

label s_farewell_game:
    s abhfaoa "Alright, [player]!"
    s abfccaa "I hope you have lots of fun!"
    s abfcaoa "I’ll be cheering you on from here!"
    return "quit"

label s_farewell_restart:
    s abhfaoa  "Oh, you want to restart the game?"
    if persistent.cheat_game = True:
        s fbhemja "You better not be trying to get the game back!"
        s abfccaa "Ehehehe~ just kidding, [player]! I’ll be waiting!"
    else:

        s abfccaa " Alright, [player]."
        s abfcaoa " I’ll be waiting!"
    return "quit"
