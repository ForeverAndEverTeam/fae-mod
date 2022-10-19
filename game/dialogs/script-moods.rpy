default persistent._mood_db = dict()

default persistent.fae_mood_on_quit = None

init -1 python in fae_moods:

    import random
    import store

    MOOD_DEFS = dict()

    ANGRY = 0
    ANXIOUS = 1
    BORED = 2
    EXCITED = 3
    HAPPY = 4
    HUNGRY = 5
    LONELY = 6
    SAD = 7
    SICK = 8
    TIRED = 9

    previous_mood = None

    def load_all_moods():

        return store.Chat.chat_filt(
            MOOD_DEFS.values(),
            affection=store.Affection._getAffectionStatus(),
            unlocked=True
        )

label mood_init:

    python:
        mood_options = [
            (_mood.prompt, _mood.label)
            for _mood in fae_moods.load_all_moods()
        ]
        mood_options.sort()
    
    call screen neat_menu_scroll(mood_options, ("Nevermind", None))

    if _return:
        $ ats(_return)
        jump cnc
    
    return

init 5 python:

    chatReg(
        Chat(
            persistent._mood_db,
            label="s_mood_angry",
            unlocked=True,
            prompt="Angry"
        ),
        chat_group=CHAT_GROUP_MOOD
    )

label s_mood_angry: #Angry player
    s bbaaaca "Awh, [player]."
    s "I think you should try to breathe slowly, so you calm down a little bit."
    s "I promise, no matter what's wrong, being angry won't solve the problem."
    s bbaacoa "It's easy to make impulsive decisions when you're mad, so let's make sure not to do that first!"
    s "That way, you don't end up doing something you'll regret when you've calmed down."
    s bbaacoa "Do you need to vent for a bit? I'm here for you if you need to."
    menu:
        "Yes":
            s abhfcoa "Alright, I'm listening."
            show sayori idle
            s "{w}"
            s gbhabfa "Yeah, I can see why that would make you angry." 
            s bbhaica "I'm sorry that happened, [player]."
        "No":
            s bbaaaoa "That's Alright, we can do something else."
            s fbaalhaj "Hmmmm...lemme think..."
            pause 0.5
            s ebbcaea "Oh, I know! Do you want to play a game with me? It will help distract you from whatever is making you feel like this, even if just for a little while."
            menu:
                "Yes":
                    s fbgciea "Alright, give me your best!"
                    call screen mglist
                "No":
                    s abfcaca "Not in the mood? That's ok too."
                    s bbhfmoaj "In that case, I have one last suggestion, but it might sound a bit silly..."
                    s ebbbcoaj "Have you had the time to do one biiiiiig stretch today yet?"
                    s fbgcipbj "Hey- I know it sounds silly, but it works!!!" 
                    s ebgccaa "Try getting one of those good stretches that make all the right places pop~" 
                    s gbgcmjaj "It really does help!"
    s bbhaaoa "I hope you're feeling a little better, [player]."
    s ebhacoa "Remember, you can always come talk to me."
    return

init 5 python:

    chatReg(
        Chat(
            persistent._mood_db,
            label="s_mood_hungry",
            unlocked=True,
            prompt="Hungry"
        ),
        chat_group=CHAT_GROUP_MOOD
    )


label s_mood_hungry: #Hungry player
    s bbfcaa "Aw… well I wish I could give you a cookie right now!"
    s bbhemma "I'm sure it would be super tasty ehehe!" 
    s bbfdmoaj "Though…{nw}"
    extend bbfcaaa "That wouldn’t be a very good meal now, would it?{w=1.5}{nw}" 
    extend bbfcmoa "Sorry, ehehe~" 
    s abhfaaa "You should go eat something, [player]."
    s abbcaaa "If you have to cook something yourself, I can wait till you're done!" 
    s abfcaca "After all, skipping meals is a bad idea!" 
    s "Take as long as you need, and then let me know when you’re back!" 
    s abhfaoa "I'll be waiting for you, [player]." 
    return


init 5 python:

    chatReg(
        Chat(
            persistent._mood_db,
            label="s_mood_excited",
            unlocked=True,
            prompt="Excited"
        ),
        chat_group=CHAT_GROUP_MOOD
    )


label s_mood_excited: #Excited player
    s ebfbbnsa "Ohhhh! Now that's the kind of news I like to hear!"
    s ebagbkoa "I hope that's it's because you have something fun coming up soon!"
    s eahdbada "Is there anything in particular you're looking forward to?"
    s ebhhcqa "Ooooor~"
    s ebbdbdia "Maybe, you're just excited to spend some time with me today, ehehe~" 
    s bbhebijb "Can you tell me a little bit about it? I'm curious~"
    menu:
        "Yes":
            s ebgcbnea "Yayyy! Thank you!"
            s ebbccqa "Go on~"
            show sayori idle
            s "{w}"
            s abbcbnea "Ohhh, that does sound really nice!"
            s abgcbcea "I'm already excited for you, [player]!" 
            s abhfaoa "Thank you for telling me about it!"
        "It's a secret":
            s bahcbjga " Whaaaat??? Not fair!!"
            s gbhabjja "I wanna know too! You're such a meanie..."
            pause 1.0
            s abhabdia "Just kidding!"
            s abhfboa "It's alright if you don't feel like telling anyone."
            s abhfcaa "Whatever it is that made you excited, I am glad it did! I like seeing you happy!"
    s abhhcoa "Knowing that you're having a good day always makes me happy, too!"
    s abgccoa "Well, I hope things keep going well for you, and that today gets even better, [player]!" 
    return
