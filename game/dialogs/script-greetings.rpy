default persistent._greet_db = dict()
default persistent.fae_first_greet = True

init -1 python in fae_greetings:
    import random
    import store
    import store.fae_farewells as fae_farewells
    import store.fae_utilities as fae_utilities

    GREETING_DEFS = dict()

    def greet_sel():

        if fae_farewells.FAEForceQuitStates(store.persistent.fae_player_force_quit_state) == fae_farewells.FAEForceQuitStates.first_force_quit:
            return "greeting_first_force_quit"
        
        elif store.persistent.fae_first_greet:
            return "greeting_first_time"
        
        kwargs = dict()

        if store.persistent._fae_await_apology_quit is not None:
            kwargs.update({"extra_props": [("regret_type", store.persistent._fae_await_apology_quit)]})
        
        elif store.persistent.fae_mood_on_quit is not None:
            kwargs.update({"extra_props": [("mood_type", store.persistent.fae_mood_on_quit)]})

        else:
            kwargs.update({"no_categories": ["Mood", "Regret"]})

        #TODO: ADD "IF" STATEMENTS FOR LEAVE CONDITIONS

        #RETURN GREETING

        return random.choice(
            store.Chat.chat_filt(
                GREETING_DEFS.values(),
                affection=store.Affection._getAffectionStatus(),
                **kwargs
            )
        ).label

label greeting_first_time:
    s "Hello~"
    $ persistent.fae_first_greet = False
    return

init 5 python:
    chatReg(
        Chat(
            persistent._greet_db,
            label="s_1",
            unlocked=True
        ),
        chat_group=CHAT_GROUP_GREETING
    )

label s_1:
    s "Hello~"
    return

label greeting_first_force_quit:
    s "Hello~"

    $ persistent.fae_force_quit_state = int(fae_farewells.FAEForceQuitStates.has_force_quit)
    
    return

#Normal greetings

init 5 python:
    chatReg(
        Chat(
            persistent._greet_db,
            label="s_greeting_1",
            unlocked=True
        ),
        chat_group=CHAT_GROUP_GREETING
    )

label s_greeting_1: #The really first greeting of this mod

    #show sayori abagaaa at t11 zorder 2

    s abagaaa "I'm glad to see you again."
    s abaaaoa "Let's have a good time together!"
    return


init 5 python:
    chatReg(
        Chat(
            persistent._greet_db,
            label="s_greeting_2",
            unlocked=True
        ),
        chat_group=CHAT_GROUP_GREETING
    )

label s_greeting_2: #Try to keep it poetic while translating
    #show sayori abaaaoa at t11 zorder 2
    s abaaaoa "Ah, welcome back, [player]!" 
    s "{i}I'm so happy that you're here!{/i}"
    s "{i}You fill my heart with joy, ehehehe~{/i}"
    return


init 5 python:
    chatReg(
        Chat(
            persistent._greet_db,
            label="s_greeting_3_rus",
            unlocked=True
        ),
        chat_group=CHAT_GROUP_GREETING
    )

label s_greeting_3_rus:
    s "Привет, [player]!"
    s abagcoa "Я рада, что ты здесь."
    s abhhaoa "If you didn't understand what that means, don't worry!"
    s "I just said 'Hello, [player]! I'm glad you're here.' in Russian!"
    $ persistent.language_greeting_seen = True

    return

init 5 python:
    chatReg(
        Chat(
            persistent._greet_db,
            label="s_greeting_3_epo",
            unlocked=True
        ),
        chat_group=CHAT_GROUP_GREETING
    )

label s_greeting_3_epo:
    s "Saluton, [player]!"
    s abgcaoa "Kia ĝojo revidi vin!"
    s abbccoa "That's what 'Hello, [player]! It's such a joy to see you again!' sounds like in Esperanto!"
    $ persistent.language_greeting_seen = True
    return


init 5 python:
    chatReg(
        Chat(
            persistent._greet_db,
            label="s_greeting_3_esp",
            unlocked=True
        ),
        chat_group=CHAT_GROUP_GREETING
    )

label s_greeting_3_esp:
    s "¡Hola [player]!"
    s abgcaoa "¡Qué alegría verte de nuevo!"
    s abgccqa "Ehehehe, do you know what that means?"
    s abbcaoa "It's alright if you don't! I just said 'Hello, [player]! I'm happy to see you again!' in Spanish!"
    $ persistent.language_greeting_seen = True

    return


init 5 python:
    chatReg(
        Chat(
            persistent._greet_db,
            label="s_greeting_4",
            unlocked=True
        ),
        chat_group=CHAT_GROUP_GREETING
    )

label s_greeting_4:

    #show sayori abaaaaa at t11

    s abaaaaa "Oh, hi again!"
    s bbfbaaa "I hope nothing bad happened to you while you were gone..."
    s bbfbmabj "I just wanna make sure you're doing alright, you know?"
    s bbfbaaa "So if you aren't, you'll tell me, right?"
    return


init 5 python:
    chatReg(
        Chat(
            persistent._greet_db,
            label="s_greeting_5",
            unlocked=True
        ),
        chat_group=CHAT_GROUP_GREETING
    )

label s_greeting_5:

    #show sayori abaaaaa at t11

    s abaaaaa "Looks like you're here to visit me again, ehehehe~"
    s abagaca "It can get pretty boring here when you're not around, you know..."
    s "Cause after all, you're the only friend I have left."
    s abbccaa "But I wouldn't choose anyone else over you, because you always know how to cheer me up!"
    s "So, hopefully I can do the same for you!"
    return


init 5 python:
    chatReg(
        Chat(
            persistent._greet_db,
            label="s_greeting_6",
            unlocked=True
        ),
        chat_group=CHAT_GROUP_GREETING
    )

label s_greeting_6:
    #show sayori abgcaoa at t11
    s abgcaoa "Oh hey [player], you're back!"
    s abaaaoa "I'm glad to see you again!"
    s "Let's spend some time together."
    return
    

label player_bday:
    if time_of_day != 2 and (time_of_day != 1 or ee_chance > 0.1):
        $ chance = renpy.random.random()
        if chance < (1.0/3.0):
            s "I'm glad you're visiting me today, [player]!"
            s "Let's spend some time together!"
        elif chance < (2.0/3.0):
            s "Hey, welcome back [player]!"
            s "I'll do my best to make today really nice for you, ehehe~"
        else:
            s abbbcka "Oh, [player], you're here! I hope you're feeling good today!"
            s ebbbasa "But even if you aren't, that's okay too, you know!"
            s abhaaaa "You don't need to be in a great mood all the time. I still enjoy being by your side just as much."
            return

    if not persistent.bday_feb29:

        if not persistent.birthday1:
            $ persistent.birthday1 = True
            $ age = get_now().year - persistent.playerbdate.year
            s aahccaa "Welcome back [player]!"
            s fbgckdaj "Huh?? 'Persistent.playerbdate'? What's that abou-" 
            s bbgcegbj "OH MY GOD IT'S YOUR BIRTHDAY I'M SO SORRY!!!"
            s bbbccobj "Happy birthday, [player]!!!"
            if age == 18:
                s "Oh hey, we're finally the same age now!"
                s fbhfkda "I can't exactly age like you can, so I figure it makes sense to just call myself 18."
            s "Aww, I wish I could throw a little birthday party for you..."
            s abbcloa "Well, I'll figure something out someday, okay?"
            s aahccea "Either way, now that you're here, let's spend some time together for your special day!"
            return

    elif bday_feb29:
        if persistent.bday_feb29_seen:
            s aahccea "Happy birthday, [player]!"
            s aahcaoa "So let's get to celebrating together, [player]! And again, happy birthday!"
            return

        else:

            $ age = get_now().year - persistent.playerbdate.year
            s aahccea "Happy birthday, [player]!"
            s eahdkea "Huh, it's pretty cool that your birthday falls on the leap year!"
            s bbagapa "Though, it must be a little disappointing to not have a \"proper\" birthday most years..."
            s ebgcaoa "I wonder, do you celebrate it on the 28th of February, or March 1st?"
            s ebgckgaj "Maybe you can celebrate on both days!"
            s ebbccea "When you look at it that way, you actually have a way cooler birthday than most people!"
            s aahcaoa "So let's get to celebrating together, [player]! And again, happy birthday!"
            return


label s_val_present():
    
    $ val_date = datetime.date(get_now().date().year, 2, 14)
    
    $ has_present = poems["val"].available is False and get_now().date() >= val_date
  
    if get_now().date() == val_date:
        s "Hey [player], happy Valentine's Day!"
        s aahbcaa "I actually have a little present for you.."
        
        call showpoem(poem_val, "paper_val", 200, 0.5, 360) from _call_showpoem
    
    elif get_now().date() > val_date:
        
        if first:
            s bbhemjb "I've never really given anyone a Valentine's day gift before, but..."
            s "I actually have something special for you right now! Just wait a second..."
        
        else:
            s gbhakpa "You missed Valentine's day!"
        s abhelab "But I made a special present for you..."
        
        call showpoem(poem_val, "paper_val", 200, 0.5, 360) from _call_showpoem_1
    
    s bbhecob "Ehehehe, I hope you like it, [player]! I know it's a bit sappy, but..."
    s "But I couldn't help it, I just wanted to make you something for the occasion!"
    s abfcaoa "And don't worry! You don't have to give me anything back..."
    s abfccqb "Cause, you know, spending time with you is already the best present I could ever receive!"
    return


init 5 python:
    chatReg(
        Chat(
            persistent._greet_db,
            label="s_greeting_7",
            unlocked=True
        ),
        chat_group=CHAT_GROUP_GREETING
    )

label s_greeting_7:

    #show sayori abhfaka at t11

    s abhfaka "Look who's back!"
    s abagaoa "It's [player], of course!"

    if persistent.gender == "F":
        s abagcaa "And it looks like she's ready to spend some time with her sunshine."
    elif persistent.gender == "M":
        s abagcaa "And it looks like he's ready to spend some time with his sunshine."
    else:
        s abagcaa "And it looks like they're ready to spend some time with their sunshine."
    return


init 5 python:
    chatReg(
        Chat(
            persistent._greet_db,
            label="s_greeting_8",
            unlocked=True
        ),
        chat_group=CHAT_GROUP_GREETING
    )

label s_greeting_8:

    #show sayori abgcaoa at t11

    s abgcaoa "Hi [player]!"
    s abgccaa "Are you here for your daily dose of sunshine?"
    s abfdcqa "I'll get you some right now then, ehehehe~"
    return


init 5 python:
    chatReg(
        Chat(
            persistent._greet_db,
            label="s_greeting_long_absence",
            unlocked=True
        ),
        chat_group=CHAT_GROUP_GREETING
    )

label s_greeting_long_absence:

    s "Hello"
    return


label s_greetings_long:

    # I'm going away for a while return checks & dialogue

    $ persistent._fae_long_absence = False

    # Normal long-absence greeting

    show desknote
    call fae_showpoem(long_wait) from _call_fae_showpoem

    menu:
        "Call out for Sayori":
            s "Hmmmm, wh-"
            s "Mmhhh, five more minutes pleeease-"
            pass
    
            menu: 
                "Call out for Sayori again":
                    pass
                "...":
                    pass
    
    s "Hnmmmn, wha-"
    s "{i}Wait, is that you, [player]?{/i}"
    s "Give me a second!! Lemme just-"
    s "waAAAAAAAaaaH!!"

    show screen tear(20, 0.1, 0.1, 0, 40)

    play sound "sfx/s_kill_glitch1.ogg"

    show sayori cahberj at t11

    pause 1
    
    s bahbejaj "Ouch! Sorry, I tripped."
    s cahblpbj "{i}*sigh*{/i}"
    s fbfbmjaj "Where were you? You left for so long!!"
    s aahbbba "I'm not blaming you, though."
    s ebbbaha "You may be just a quite busy person..."
    s ebhfaaa "And that could be why you haven't visited for so long."
    s abhaloa "That was a nice nap and all..."
    s cbhaira "BUT!"
    s fbhamdb "Try to visit me more often next time, okay?"
    s "It gets lonely in here!"
    s bbfdlja "If I get too bored, I might start playing with code, and might not be able to guarantee the privacy of your shady internet history!"
    s abfccia "...just kidding!"
    s gahdbika "Or am I?"
    return


#TODO: EXPS HERE
init 5 python:
    chatReg(
        Chat(
            persistent._greet_db,
            label="s_greeting_9_ptbr",
            unlocked=True,
            affection_range=(fae_affection.ENAMOURED, None)
        ),
        chat_group=CHAT_GROUP_GREETING
    )

label s_greeting_9_ptbr:
    s "Oi, [player]!"
    s "Eu te amo!"
    s "Ehehehe, did you by any chance understand what I just said?"
    s "I said 'hi' and 'I love you' in Portuguese!"
    s "It's such a different language in my experience, but I think it's very beautiful."
    s "Well, let's have another wonderful day together~"
    $ persistent.language_greeting_seen = True

    return
