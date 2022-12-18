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
        
        if store.persistent._fae_absence_choice is not None:
            return "s_greeting_long_absence"
        
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

    s abgcaoa "Hi [player]!"
    s abgccaa "Are you here for your daily dose of sunshine?"
    s abfdcqa "I'll get you some right now then, ehehehe~"
    return


init 5 python:
    chatReg(
        Chat(
            persistent._greet_db,
            label="s_greetings_long",
            unlocked=True
        ),
        chat_group=CHAT_GROUP_GREETING
    )

label s_greetings_long:

    $ persistent._fae_long_absence = False

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


init 5 python:
    chatReg(
        Chat(
            persistent._greet_db,
            label="s_greeting_ptbr",
            unlocked=True,
            affection_range=(fae_affection.ENAMOURED, None)
        ),
        chat_group=CHAT_GROUP_GREETING
    )

label s_greeting_ptbr:
    s abaacoa "Oi, [player]!"
    s bbaaaaa "Eu te amo!"
    s abaaaoa "Ehehehe, did you by any chance understand what I just said?"
    s abbcaoa "I said 'hi' and 'I love you' in Portuguese!"
    s abbcaaa "It's such a different language in my experience, but I think it's very beautiful."
    s abgccaa "Well, let's have another wonderful day together~"
    $ persistent.language_greeting_seen = True


    return

init 5 python:
    chatReg(
        Chat(
            persistent._greet_db,
            label="s_greeting_french",
            unlocked=True,
            affection_range=(fae_affection.NORMAL, None)
        ),
        chat_group=CHAT_GROUP_GREETING
    )

label s_greeting_french:
    s abgbaoa "Salut, [player]!"
    s abgbcaa "Je suis tellement contente de te revoir!"
    s abbbaoa "Ehehehe, that was just some French!"
    s dbbbiaa "Don’t I sound classy, huh? {w=0.5}{nw}"
    extend abgbcaa "Ehehehe~"
    s abhfaoa "That meant {i}Hey, [player]! I’m so glad to see you again!{/i}"
    s abhecaa "I figured out how to use Google Translate, if you couldn’t tell!"
    s abheeebj "And for once I’m glad that you can’t hear me, because I completely butchered the pronunciation of that in my head, ehehehe~"
    s abheeabj "I can barely speak English sometimes!"
    s abgbcoa "But who knows, maybe some smart cookie could make me a translation someday, ehehehe~"
    s abhfaaa "Do you speak any other languages, [player]?"
    s abhfaoa "I’ve always wanted to learn one! {w=0.5}{nw}"
    extend abfccaa "Maybe you could teach me, if you do?"
    s abfcaoa "Ehehehe, anyways."
    s abhfaaa "Where were we, [player]?"
    $ persistent.language_greeting_seen = True
    return

# Small affection gain for being like a hero    

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
    $ persistent._fae_long_absence = False
    $ fae_ret_long_absence = True
    if persistent._fae_absence_time >= datetime.timedelta(weeks=5):
        if persistent._fae_absence_choice == "days":
            s ebgchca "[player]!"
            s gbgbara "You said you’d only be gone a few days!"
            s bbgbaca "It’s been such a long time…"
            s bbgblrag "I thought something bad happened…"
            s bbhfaca "Well… at least you’re okay."
        elif persistent._fae_absence_choice == "week":
            s ebgchca "[player]!"
            s gbgbara "You told me you’d only be gone a week!"
            s bbgbaca "It’s been ages…"
            s bbgblrag "I was worried sick about you…"
            s bbhfaca "Well… at least you’re back."
        elif persistent._fae_absence_choice == "month":
            s abgbaoa "Back again [player]?"
            s abgbaaa "It’s been a little longer than you said you’d be, ehehehe~"
            s abgbcaa "But that’s okay!"
            s abhfaoa "Let’s spend some more time together."
        elif persistent._fae_absence_choice == "unknown":
            s abgbkca "Oh! [player]!"
            s abgbaoa "You’re back!"
            s abhfcaa "You {i}really{/i} weren’t sure, were you? Ehehehe~"
            s bbheaoa "I was a little worried about you, {w=0.5}{nw}"
            extend abgbcaa "but I’m glad you’re back now!"
            s abgbaoa "Let’s spend some more time together."

    elif persistent._fae_absence_time >= datetime.timedelta(weeks=4):
        if persistent._fae_absence_choice == "days":
            s ebgchca "[player]!"
            s gbgbara "You told me you’d only be gone for a few days!"
            s gbgbaca "And it’s been four weeks!"
            s bbgblrag "I was getting worried about you…"
            s bbhfaca "Well… at least you’re here now."
        elif persistent._fae_absence_choice == "week":
            s ebgchca "[player]!"
            s gbgbara "You told me you’d only be gone for a week!"
            s gbgbaca "And it’s almost been an entire month!"
            s bbgblrag "I was getting worried about you…"
            s bbhfaca "Well… at least you’re back now."
        elif persistent._fae_absence_choice == "month":
            s abgccoa "Welcome back, [player]!"
            s abgcaoa "I missed you!"
            s bbgcaaa "A month goes by so slowly without you, ehehehe~"
            s abgccaa "Let’s spend some more time together."
        elif persistent._fae_absence_choice == "unknown":
            s ebgchca "Oh! [player]!"
            s ebbccoa "Welcome back!"
            s abbcaoa "It’s been a while, hasn’t it? Ehehehe~"
            s bbfcaaa "I was a little worried about you, {w=0.5}{nw}"
            extend bbfccaa "but I’m glad you’re okay!"
            s abfcaoa "Let’s spend some more time together."

    elif persistent._fae_absence_time >= datetime.timedelta(weeks=2):
        if persistent._fae_absence_choice == "days":
            s ebgchca "[player]!"
            s bbgbara "You’ve been gone a while…"
            s bbgbaca "I was starting to worry about you…"
            s bbfcaaa "But nevermind that,"
            extend abfcaoa "I’m glad you’re back."
            s abgccoa "Let's spend some more time together."
        elif persistent._fae_absence_choice == "week":
            s abfcaoa "Hey, [player]!"
            s abfcaca "You’ve been gone a bit longer than a week."
            s abfcaca "But that’s okay, {w=0.5}{nw}"
            extend bbgcaaa "you came back eventually!"
            s bbgcmoaj "Though you’re a little late, ehehehe~"
            s abgccoa "Let’s spend some more time together."
        elif persistent._fae_absence_choice == "month":
            s ebgchca "Oh! {w=0.5}{nw}"
            extend abgccoa "Back already, [player]?"
            s bbhemoaj "Not that I’m complaining, ehehehe~"
            s abheaaaj "You’re a little early, but that’s okay!"
            s abfccaa "Let’s spend some more time together."
        elif persistent._fae_absence_choice == "unknown":
            s ebfchsa "Oh! [player]!"
            s abfcaoa "I didn’t expect you back {i}this{/i} soon."
            s bbfcmoaj "I’m not complaining though, ehehehe~"
            s abfccoa "Let’s spend some more time together."

    elif persistent._fae_absence_time >= datetime.timedelta(weeks=1):
        if persistent._fae_absence_choice == "days":
            s cbaahca "[player]!"
            s cbaaapa "You’re late!"
            s cbbbaca "You said you’d only be a few days!"
            s cbbbaha "And it’s been a whole week!"
            s abgbcoa "Ehehehe, just kidding, [player]!"
            s bbhfaaa "I’m just glad to see you again."
            s bbhfaoa "I understand if you find yourself a little busier than you expected to be from time to time."
            s cbaamc "Ugh!"
            if persistent.gender == "M":
                s cbaamp "Boys. Honestly."
            s abgbcaa "Let’s spend some more time together."
        elif persistent._fae_absence_choice == "week":
            s abgccoa "Welcome back, [player]!"
            s abgcaoa "I missed you!"
            s abgccaa "Right on time too, ehehehe~"
            s abgcaaa "Let’s spend some more time together!"
        elif persistent._fae_absence_choice == "month":
            s abgcaoa "Oh, hi [player]!"
            s abgcaaa "I wasn’t expecting to see you so soon!"
            s abfccaa "I’m glad you’re back though!"
            s abfcaaa "Let’s spend some more time together."
        elif persistent._fae_absence_choice == "unknown":
            s abfcaaa "Oh, hey [player]!"
            s bbfccoaj "Back so soon? Ehehehe~"
            s abfcaoa "Well I’m not complaining!"
            s abfcaaa "Let’s spend some more time together."
    else:
        if persistent._fae_absence_choice == "days":
            s abfcaaa "Welcome back, [player]!"
            s bbfcaaa "Thanks for telling me how long you’d be out."
            s abgccaa "I’m glad you’re back!"
            s abgcaaa "Let’s spend some more time together."
        elif persistent._fae_absence_choice == "week":
            s abgccoa "[player]!"
            s abgcmoaj "You’re a little early! Ehehehe~"
            s abgcmoaj "But I’m not complaining!"
            s abfcaaa "I guess you didn’t expect to be gone for such a short time ehehehe~"
            s abfccoa "Let’s spend some more time together."
        elif persistent._fae_absence_choice == "month":
            s abgcaoa "Oh! Hi [player]!"
            s "I didn’t expect you to return so soon!"
            s "But that’s fine by me! Ehehehe~"
            s abgccoa "Let’s spend some more time together."
        elif persistent._fae_absence_choice == "unknown":
            s abgchsa "Oh! [player]!"
            s bbgcaaa "I didn’t expect you to return so soon!"
            s bbgcmoaj "But I guess you didn’t either, ehehehe~"
            s abfcaaaj "Let’s spend some more time together."
    $ persistent._fae_absence_choice = None
    return 

