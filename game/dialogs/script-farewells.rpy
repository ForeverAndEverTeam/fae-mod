default persistent._farewell_db = dict()

default persistent.fae_first_leave_response = None

default persistent.fae_player_force_quit_state = 1


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
            ("I'm going to sleep.", "s_farewell_sleep"),
            ("I'm going to school.", "s_farewell_school"),
            ("I'm going to play a game.", "s_farewell_game"),
            ("I'm going to eat.", "s_farewell_eat"),
            ("I'm going to work out.", "s_farewell_work_out"),
            ("I'm going to work.", "s_farewell_work"),
            ("I'm going to do chores.", "s_farewell_chores"),
            ("I'm going to restart.", "s_farewell_restart"),
            ("I'll be going away for a while.", "s_farewell_long_absence")
        ]
    
    def farewell_pick():


        farewell_pool = [
            ("s_farewell_1"),
            ("s_farewell_2"),
            ("s_farewell_3"),
            ("s_farewell_4"),
            ("s_farewell_5"),
            ("s_farewell_6"),
            ("s_farewell_7")
        ]

        return random.choice(farewell_pool)

label farewell_init:

    $ ats(fae_farewells.farewell_pick())
    jump cnc

label farewell_force_quit:

    s "You can't just leave!"

    $ persistent.fae_player_force_quit_state = int(fae_farewells.FAEForceQuitStates.first_force_quit)
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
    
    call screen neat_menu_scroll(selectable_leave_options, ("Nevermind.", False))

    if not _return:
        jump ch30_loop

    if isinstance(_return, basestring):
        show sayori idle at t11 zorder fae_sprites.FAE_SAYORI_ZORDER
        $ ats(_return)
        jump cnc

label first_leave:

    s "See ya!"
    return { "quit": None }


#Farewells
label s_farewell_1: #The actual first farewell of this mod
    
    s abhfbaoa "Oh, are you heading out, [player]?" 
    s abhfbcoa "I'll see you later, then! Be safe out there!"

    return { "quit": None }

label s_farewell_2:
    s "Goodbye, [player]!"
    s "You can always visit whenever you want."
    s abfdbaoa "I'll always be here to spend time with you!"
    return { "quit": None }

label s_farewell_3:
    s "Bye, [player]!"
    s abgcbcqa "I’ll see you soon!"
    return { "quit": None }

label s_farewell_4:
    s "Bye-bye!"
    s "I'll be wishing you health and happiness!"
    s abhebaka "Be safe out there, okay, [player]? Ehehehe~"
    return { "quit": None }

#label s_farewell_5:
#    if get_time_of_day() == 0:
#        s abhfbaaa "Goodnight, [player]!"
#        s fbhabica "Make sure you get enough sleep so you aren't all grumpy when you wake up, okay?"
#    elif get_time_of_day() < 3:
#        s abhfbaaa "Have a good day, [player]!"
#        s abhfbaaa "I hope you can accomplish all of your goals for today; whether they're big or small, I'll be proud of you either way!"
#    else:
#        s abhfbaaa "See you later, [player]!"
#        if get_time_of_day(launch_dt.hour) == 3:
#            s "I'm glad you were able to spend some of your evening with me!"
#        else:
#            s "I'm glad you were able to spend the day with me!"
#    return "quit"

label s_farewell_6:
    s "Bye, [player]!"
    s fbhabica "And don't forget to make sure that you're taking good care of yourself!"
    s abagbcaa "I want you to come back and be safe and sound, okay?"
    return { "quit": None }

label s_farewell_7:
    s "See you later, [player]!"
    s abfbbaha "I wish I could give you a little farewell hug..."
    s abfdbcqa "But as long as you know that I would, I’m happy, ehehehe~"
    return { "quit": None }


init 5 python:
    chatReg(
        Chat(
            persistent._farewell_db,
            label="s_farewell_school",
            unlocked=True,
            affection_range=(fae_affection.NORMAL, None)
        ),
        chat_group=CHAT_GROUP_FAREWELL
    )

label s_farewell_school:
    s abhfaoa "Oh, time for school, [player]?"
    s abfccaa "I hope everything goes smoothly for you today!"
    s abfcaoa "See you later!"
    return { "quit": None }

init 5 python:
    chatReg(
        Chat(
            persistent._farewell_db,
            label="s_farewell_work",
            unlocked=True,
            affection_range=(fae_affection.NORMAL, None)
        ),
        chat_group=CHAT_GROUP_FAREWELL
    )

label s_farewell_work:
    s abhfaoa "Oh, time to work, [player]?"
    s abfccaa "I hope everything goes smoothly for you today!"
    s abfcaoa "See you later!"
    return { "quit": None }

init 5 python:
    chatReg(
        Chat(
            persistent._farewell_db,
            label="s_farewell_chores",
            unlocked=True,
            affection_range=(fae_affection.NORMAL, None)
        ),
        chat_group=CHAT_GROUP_FAREWELL
    )


label s_farewell_chores:
    s abhfaoa "Got some housework to take care of, [player]?"
    s abfccaa "Take your time, I hope it all goes well!" 
    s abfcaoa "I’ll see you soon!"
    return { "quit": None }

init 5 python:
    chatReg(
        Chat(
            persistent._farewell_db,
            label="s_farewell_eat",
            unlocked=True,
            affection_range=(fae_affection.NORMAL, None)
        ),
        chat_group=CHAT_GROUP_FAREWELL
    )


label s_farewell_eat:
    s abhfaoa "Going to eat, [player]?" 
    s abfccma "I was getting pretty hungry myself, I think I’ll have some cookies!" 
    s abfcaoa "Enjoy your food! Ehehehe~" 
    return { "quit": None }

init 5 python:
    chatReg(
        Chat(
            persistent._farewell_db,
            label="s_farewell_work_out",
            unlocked=True,
            affection_range=(fae_affection.NORMAL, None)
        ),
        chat_group=CHAT_GROUP_FAREWELL
    )


label s_farewell_work_out:
    s abhfaoa "Ooooh! Wanna work out a bit [player]?"
    s abfccaa "I’m so glad you’re taking care of yourself!" 
    s abfcaoa "I hope you have fun! Bye-bye!" 
    return { "quit": None }


init 5 python:
    chatReg(
        Chat(
            persistent._farewell_db,
            label="s_farewell_sleep",
            unlocked=True,
            affection_range=(fae_affection.NORMAL, None)
        ),
        chat_group=CHAT_GROUP_FAREWELL
    )


label s_farewell_sleep:
    s abhfaoa "Heading to bed, [player]?"
    s abhfcaa "Hope you have a good night’s sleep!"
    if Affection.isEnamoured():
        s abhebob "...can I have a goodnight kiss? Ehehehe~"
        menu: 
            "Sure, Sayori":
                s abgcceb "Yay!"
                call fae_kiss_short
            "Another time":
                s bbhfbaa "Alright then..."
    s abfcaaa "Sweet dreams, [player]!"
    return { "quit": None }

init 5 python:
    chatReg(
        Chat(
            persistent._farewell_db,
            label="s_farewell_study",
            unlocked=True,
            affection_range=(fae_affection.NORMAL, None)
        ),
        chat_group=CHAT_GROUP_FAREWELL
    )

label s_farewell_study:
    s abhfaoa "Got some studying to do, [player]?"
    s abfccaa "Make sure to take plenty of breaks in between!"
    s abfcaoa "You’ve got this, I believe in you!"
    return { "quit": None }

init 5 python:
    chatReg(
        Chat(
            persistent._farewell_db,
            label="s_farewell_game",
            unlocked=True,
            affection_range=(fae_affection.NORMAL, None)
        ),
        chat_group=CHAT_GROUP_FAREWELL
    )

label s_farewell_game:
    s abhfaoa "Alright, [player]!"
    s abfccaa "I hope you have lots of fun!"
    s abfcaoa "I’ll be cheering you on from here!"
    return { "quit": None }

init 5 python:
    chatReg(
        Chat(
            persistent._farewell_db,
            label="s_farewell_restart",
            unlocked=True,
            affection_range=(fae_affection.NORMAL, None)
        ),
        chat_group=CHAT_GROUP_FAREWELL
    )


label s_farewell_restart:
    s abhfaoa "Oh, you want to restart the game?"
    if persistent.cheat_game:
        s fbhemja "You better not be trying to get the original game back!"
        s abfccaa "Ehehehe~ just kidding, [player]! I’ll be waiting!"
    else:

        s abfccaa "Alright, [player]."
        s abfcaoa "I’ll be waiting!"
    return { "quit": None }

init 5 python:
    chatReg(
        Chat(
            persistent._farewell_db,
            label="s_farewell_long_absence",
            unlocked=True,
            affection_range=(fae_affection.NORMAL, None)
        ),
        chat_group=CHAT_GROUP_FAREWELL
    )


label s_farewell_long_absence:
    s bbfcaaa "Aww... {w=0.5}{nw}"
    extend bbfcaca "I hate to see you go, [player]."
    s abfcaca "Do you know how long you’ll be gone for?{nw}"
    $ _history_list.pop()
    menu:
        s "Do you know how long you’ll be gone for?{fast}"
        "A few days.":
            $ persistent._fae_absence_choice = "days"
            s abfcksa "Oh! {w=0.5}{nw}"
            extend abfcaoa "That’s okay, [player]!"
            s bbgcaoa "Don’t forget about me! Ehehehe~"
            s abgccoa "See you when you come back!"
            if Affection.isEnamoured():
                s bbgcaaa "I love you, [player]"

        "A few weeks":
            $ persistent._fae_absence_choice = "week"
            s abgckca "Eh? {w=0.5}{nw}"
            extend abgcaca "That’s quite a while, [player]!"
            s bbfcaaa "Don’t forget about me, will you?"
            s abfccaa "I’ll be waiting here for you!"
            if Affection.isEnamoured():
                s bbfcaaa "I love you, [player]!"
                s abfcaoa "See you when you get back!"
            else:
                s abfcaoa "See you when you get back!"

        "A few months":
            $ persistent._fae_absence_choice = "month"
            s abfckga "M-months?!"
            s abfcaca "[player]... {w=0.5}{nw}"
            extend bbfcaca "That’s an awfully long time."
            s bbfcbca "Well... {w=0.5}{nw}"
            extend bbfcaaa "I guess you can’t help it."
            s bbfcaoa "Just make sure to come back to me, okay [player]?"
            if Affection.isEnamoured():
                s bbfcaaa "I love you."
        
        "I don’t know":
            $ persistent._fae_absence_choice = "unknown"
            s abfcbfa "..."
            s bbfcmoaj "That’s a little concerning, [player]."
            s bbfcacaj "Are you sure you don’t know?"
            s abfcaaa "If you don’t know, I guess you don’t know."
            s abfccaa "I’ll wait for you, {w=0.5}{nw}"
            extend bbfcaaa "no matter how long it takes!"
            if Affection.isEnamoured():
                s bbfcaaa "I love you, [player]."
            s abfccaa "I’ll be waiting!"
        "Nevermind":
            $ persistent._fae_absence_choice = False
            s abfcaca "Oh? Are you not leaving?"
            s abfccoa "That’s good, [player]!"
            s bbfccoa "Ehehehe~"
            return
    return { "quit": None}
