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
        show sayori idle at t11 zorder fae_sprites.SAYO_ZORDER
        $ ats(_return)
        jump cnc
    
    jump ch30_loop

label first_leave:
    s "See ya"
    return { "quit": None }


#Farewells
label farewell_sleep: #The actual first farewell of this mod
    show sayori abhfaoa at ss1 zorder 2
    s "Oh, are you heading out, [player]?" 
    s abhfcoa "Got it- I;ll see you later, then! Be safe out there!"
    return "quit"

label farewell_school:
    show sayori abhfaaa at ss1 zorder 2
    s "Goodbye, [player]!"
    s "You can come back whenever you're feeling lonely, you know..."
    s abfdaoa "I'll always be here to spend time with you!"
    return "quit"

label farewell_game:
    show sayori abhfaaa at ss1 zorder 2
    s "Bye, [player]!"
    s abgccqa "Don't forget to come see me again soon!"
    return "quit"

label farewell_eat:
    show sayori abhfaaa at ss1 zorder 2
    s "Bye-bye!"
    s "I’ll be wishing you health and happiness!"
    s abheaka "Be safe out there, okay, [player]? Ehehe~."
    return "quit"

label farewell_exercise:
    if fae_find_hour() == 0:
        s abhfaaa "Goodnight, [player]!"
        s fbhaica "Make sure you get enough sleep so you aren’t all grumpy when you wake up, okay?"
    elif fae_find_hour() < 3:
        s abhfaaa "Have a good day, [player]!"
        s abhfaaa "I hope you can accomplish all of your goals for today, whether they’re big or small. I’ll be proud of you either way!"
    else:
        s abhfaaa "See you later, [player]!"
        s "I'm glad you were able to spend the day with me!"
    return "quit"

label farewell_work:
    show sayori abhfaaa at ss1 zorder 2
    s "Bye, [player]!"
    s fbhaica "And don’t forget to make sure that you’re taking good care of yourself!"
    s abagcaa "I want you to be able to come back and be safe and sound, okay?"
    return "quit"

label farewell_die:
    show sayori abhfaaa at ss1 zorder 2
    s "See you later, [player]!"
    s abfbaha "I wish I could give you a little farewell hug..."
    s abfdcqa "But as long as you know that I would if I were able to... that’s already enough, isn’t it? Ehehe~"
    return "quit"


init 5 python:

    chatReg(
        Chat(
            persistent._farewell_db,
            label="farewell_my_own",
            unlocked=True
        ),
        chat_group=CHAT_GROUP_FAREWELL
    )

label farewell_my_own:

    s "Bye!"
    return { "quit": None }