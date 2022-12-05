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
            s bbaaaoa "That's alright, we can do something else."
            s fbaalhaj "Hmmmm... Lemme think..."
            pause 0.5
            s ebbcaea "Oh, I know! Do you want to play a game with me? It will help distract you from whatever is making you feel like this, even if just for a little while."
            menu:
                "Yes":
                    s fbgciea "Alright, give me your best!"
                    call screen minigame_ui
                "No":
                    s abfcaca "Not in the mood? That's okay too."
                    s bbhfmoaj "In that case, I have one last suggestion, but it might sound a bit silly..."
                    s ebbbcoaj "Have you had the time to do one biiiiiig stretch today yet?"
                    s fbgcipbj "Hey, I know it sounds silly, but it works!!!" 
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
    s bbfcaa "Aw… Well, I wish I could give you a cookie right now!"
    s bbhemma "I'm sure it would be super tasty, ehehe!" 
    s bbfdmoaj "Though…{nw} "
    extend bbfcaaa "That wouldn’t be a very good meal now, would it?{w=1.5}{nw}" 
    extend bbfcmoa " Sorry, ehehehe~" 
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
    s ebfbnsa "Ohhhh! Now that's the kind of news I like to hear!"
    s ebagkoa "I hope that it's because you have something fun coming up soon!"
    s eahdada "Is there anything in particular you're looking forward to?"
    s ebhhcqa "Ooooor~"
    s ebbddia "Maybe, you're just excited to spend some time with me today, ehehehe~" 
    s bbheijb "Can you tell me a little bit about it? I'm curious~"
    menu:
        "Yes":
            s ebgcnea "Yayyy! Thank you!"
            s ebbccqa "Go on~"
            show sayori idle
            s "{w}"
            s abbcnea "Ohhh, that does sound really nice!"
            s abgccea "I'm already excited for you, [player]!" 
            s abhfaoa "Thank you for telling me about it!"
        "It's a secret":
            s bahcjga "Whaaaat??? Not fair!!"
            s gbhajja "I wanna know too! You're such a meanie..."
            pause 1.0
            s abhadia "Just kidding!"
            s abhfboa "It's alright if you don't feel like telling anyone."
            s abhfcaa "Whatever it is that made you excited, I am glad it did! I like seeing you happy!"
    s abhhcoa "Knowing that you're having a good day always makes me happy, too!"
    s abgccoa "Well, I hope things keep going well for you, and that today gets even better, [player]!" 
    return

init 5 python:

    chatReg(
        Chat(
            persistent._mood_db,
            label="s_mood_happy",
            unlocked=True,
            prompt="Happy"
        ),
        chat_group=CHAT_GROUP_MOOD
    )

#Reactions
label s_mood_happy: #Happy player
    s abgccoa "That's wonderful, [player]!"
    s abgcaoa "You know how important it is to me that you're happy."
    s bbfcaaa "And I feel happy too when you’re around!"
    s abgccaa "So I’ll try my best to keep it that way!"
    return

init 5 python:

    chatReg(
        Chat(
            persistent._mood_db,
            label="s_mood_sad",
            unlocked=True,
            prompt="Sad"
        ),
        chat_group=CHAT_GROUP_MOOD
    )

label s_mood_sad:  #Sad player
    s bbhfifa "Oh, I'm so sorry, [player]."
    s "I wish I knew what was bothering you."
    s "So I hope this doesn't sound like I'm placating you with empty words, but..."
    s bbbbiaa "Remember that the rainclouds will always go away."
    s "Some may be bigger and darker than others, but they always give way to light."
    s "It might help to do something you enjoy to take your mind away from the problem."
    s bbbbica "Or you could tell someone about how you feel."
    s "Don't be afraid to share your emotions with other people. I’m sure there’s lots of people around who care for you."
    s "They could consider and understand your problem and find a way to cheer you up!"
    s abhfaaa "Whatever it is, know that I'll always be here for you too."
    s bbhfaca "And if you're sad because you feel worthless, or alone, or that nobody cares..."
    s bbhfaaa "There's always going to be one person that believes in you."
    s abhfcaa "And that person is me, [player]."
    return

init 5 python:

    chatReg(
        Chat(
            persistent._mood_db,
            label="s_mood_bored",
            unlocked=True,
            prompt="Bored",
            affection_range=(fae_affection.HAPPY, None)
        ),
        chat_group=CHAT_GROUP_MOOD
    )

label s_mood_bored: #Bored player
    $ random_mg = renpy.random.choice(store.fae_games.mg_list).name
    s abhfmja "Hmm…{w=0.5}{nw}"
    extend abhfaaa " if you're bored, would you like to play [random_mg] with me?"
    s abbbaoa "You can start a game in the {i}'Play'{/i} menu!"
    s abbcaaa "And I'm always working on making other games for us to play too!"
    return 

init 5 python:

    chatReg(
        Chat(
            persistent._mood_db,
            label="s_mood_tired",
            unlocked=True,
            prompt="Tired"
        ),
        chat_group=CHAT_GROUP_MOOD
    )

label s_mood_tired: #Tired player 
    s abhfaca "Oh, you’re feeling tired, [player]? I think you should rest for a little while, okay?"
    s abbbaaa "Perhaps you could take a nap or listen to your favorite music, that helps me whenever I feel burnt out."
    s bbgciaa "Don't worry about me, I completely understand if you need to spend some time away from the computer."
    s abgccaa "See you soon, [player]!"
    s abgccaa "Rest well."
    jump confirm_quit
    return 

init 5 python:

    chatReg(
        Chat(
            persistent._mood_db,
            label="s_mood_sleepy",
            unlocked=True,
            prompt="Sleepy"
        ),
        chat_group=CHAT_GROUP_MOOD
    )

label s_mood_sleepy: #Sleepy player 
    s abhfaaa "Alright [player], you should head to bed soon so you feel well rested tomorrow." 
    s abgccma "And when you wake up, have a big hearty breakfast before you start the day! It'll make you feel much better."
    s abhfcoa "Good night, [player]!"
    s abhfcoa "Sweet dreams."
    jump confirm_quit
    return

init 5 python:

    chatReg(
        Chat(
            persistent._mood_db,
            label="s_mood_lonely",
            unlocked=True,
            prompt="Lonely"
        ),
        chat_group=CHAT_GROUP_MOOD
    )

label s_mood_lonely: #Lonely player
    s bbhfiaa "Awh… don't worry, [player]!"
    s abbccaa "You can always spend time with me."
    if persistent.fae_bnc_unlocked:
        s abbbaoa "We could play a game, chat, or read some poems if you want to!"
    else:
        s abbbaoa "We could chat, or read some poems if you want to!"
    s abhaaca "But if you still feel lonely, then perhaps you could try to find some people who like the same things you do!"
    s abhhaaa "Maybe you could catch up with an old friend?"
    s abhhcoa "Or make a new one!"
    s abbcaaa "If you don't like going out much, you could find people on the internet to chat with too!"
    s abbccaa "I'm sure they can help you just as much as I can!"
    return

init 5 python:

    chatReg(
        Chat(
            persistent._mood_db,
            label="s_mood_sick",
            unlocked=True,
            prompt="Sick"
        ),
        chat_group=CHAT_GROUP_MOOD
    )

label s_mood_sick: #Sick player
    s bbgcjca "Oh no… I'm so sorry that you feel sick [player]..." 
    s bbhajoa "I hope you’re feeling at least somewhat okay, maybe you should go rest for a little while?" 
    s abhaiaa "I’ll wait for you, that's not a problem for me." 
    s bbgbica "But I really care about your health, [player], {w=0.5}{nw}"
    extend bbgccoa "and I don't think sitting in front of a screen will get you healed up any quicker!" 
    s bbhfaaa "I'm not going anywhere, {w=0.5}{nw}"
    extend abhfcaa "and we can talk whenever you feel up to it again!" 
    s abhfaoa "Get well soon, [player]!" 
    return

init 5 python:

    chatReg(
        Chat(
            persistent._mood_db,
            label="s_mood_nervous",
            unlocked=True,
            prompt="Nervous"
        ),
        chat_group=CHAT_GROUP_MOOD
    )

label s_mood_nervous: #Nervous player
    s abhfica "Oh? You’re nervous about something [player]? Did something happen?"
    s abgbica "Whatever it is that’s stressing you, {w=0.5}{nw}"
    extend abgbcaa "we’re in this together!" 
    s abbbiaa "But try not to overthink things, {w=0.5}{nw}"
    extend abbbaca "we often judge ourselves too harshly."
    if Affection.isAffectionate():
        s abgccab "I truly love you [player], and no matter what happens, I’ll always support you."
    else:
        s abgccaa "No matter what happens, I’ll always support you."  
    return

init 5 python:

    chatReg(
        Chat(
            persistent._mood_db,
            label="s_mood_unmotivated",
            unlocked=True,
            prompt="Unmotivated"
        ),
        chat_group=CHAT_GROUP_MOOD
    )

label s_mood_unmotivated: #Unmotivated player
    s bbhaaab "Aww... I understand that feeling all too well, {w=0.5}{nw}"
    extend abbcaaa "but I'm sure you'll get your motivation back, [player]."
    s abbbaca "Maybe you could try to write a poem about your emotions, just like I always did?" 
    s abbcaca "I found it helpful to let it all out in some way and be honest with myself."
    s abgccoa "And it also might help you find some inspiration to get you motivated again!" 
    s abbbaaa "Just don't ever give up on anything you do!"
    s abhfaoa "Keep going, and with enough determination, I know you'll reach your goals!" 
    s abbbaaa "And If you need to, there's no shame in giving yourself some time to rest and take a break from things as well."
    s abgccoa "After a while, some motivation should pop back up into that unmotivated brain of yours!" 
    return

init 5 python:

    chatReg(
        Chat(
            persistent._mood_db,
            label="s_mood_depressed",
            unlocked=True,
            prompt="Depressed"
        ),
        chat_group=CHAT_GROUP_MOOD
    )

label s_mood_depressed: #Depressed player
    s bbhfjla "[player]... I'm so sorry to hear that."
    s bbhfica "Please remember that no matter what your mind tells you, you are an amazing, sweet and lovely person." 
    s bbhaila "Don't let those bad thoughts, those rainclouds, control you." 
    s bbbbaca "Trust me when I say that there are people who care about you and want to help you."
    s "You are not alone, never ever, okay?" 
    s bbbcjfag "Don't ever do the same horrible mistakes I did. Please reach out to someone and vent about your emotions… it really might help you feel better."
    if Affection.isAffectionate():
        s bbgbacb "[player]... I love you so, so much. I’m always here for you, through the good times and the not-so-good times, and I’ll try my best to help you as much as I can from here."
    s bbbbaaa "Just don't give up and keep going forward okay?" 
    s bbhfica "Because no matter how loud those rainclouds get and no matter how hard things seem to be… there is always a glimpse of hope. A light at the end of the tunnel."
    s bbhfifa "Giving up is the worst thing you can do… I learned that myself..." 
    s bbbbica "So if you ever need to spend some time with me then go ahead and we can just talk, alright?" 
    s bbgcaaa "Remember I am always here if you need anything, no matter how small." 
    if Affection.isAffectionate():
        s bbfcaab "I love you [player], forever and ever."
    return
