default persistent.last_playthrough = 4

label show_spaceroom:
    show mask_2
    show mask_3
    show room_mask as rm:
        size (320,180)
        pos (30,200)
    show room_mask2 as rm2:
        size (320,180)
        pos (935,200)
    show monika_room
    show monika_room_highlight
    
    $ s_name = persistent.s_name
    show sayori 1a at f11 zorder 2
    show screen tear(8, offtimeMult=1, ontimeMult=10)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.5
    hide screen tear
    play music m1
    
    return

label s_intro_1:
    show black
    $persistent.last_playthrough = persistent.playthrough

    if persistent.playthrough == 0: # Player imported a save in the 1st act (Sayori will panic a bit, like it was in the quick ending)
        call s_intro_1_act1
    elif persistent.playthrough < 4: # Player imported a save in act 2-3 (Sayori will think she's in an afterworld due to she's dead)
        call s_intro_1_dead
    elif persistent.clearall: # Player imported a save after the 'good' ending (Sayori will feel it's too selfish first time, but then accept the situation)
        call s_intro_1_clear(True)
    else: # Player haven't imported a save or have imported a save in act 4/after the 'normal' ending
        call s_intro_1_clear
    
    if _return < 3:
        s "Looks like a program code or something."
        pause 0.5
        s "Hmm, I can change it just by thinking of it."
        s "And I somehow feel it can change the world around me."
        s "Like I'm a programmer of it."
        s "I never was good at Computer Science."
        s "But something tells me if I set this variable true, there will be light."
        call show_spaceroom
        s 1k "Hey, it really works."
        s "This place is very similar to my clubroom."
        s "But I can't find any exit from this room."
        s "And there's also none of furniture."
        if _return == 2:
            s 1g "Uh, [player], you're here too."
            pause 0.5
            s "Hey, can you hear me?"
        else:
            s 1g "Hey, [player]!"
        s 1k "He still not answer me."
        s "But why I feel there's someone else inside him, not he?"
        s "It makes me feel a bit weird."
        s 3y "And why thinking of they give me the sense, that I used to feel while thinking of [player]?"
        s 3m "Have I just said it aloud?"
    
    if _return < 3 or persistent.clearall:
        s 5d "Understand me right."
        s "I don't know who are you..."
        s "How do you really look..."
        s "And even your real name and gender..."
        s "But I feel it doesn't matter for me now."
        s 5b "I don't understand how it's possible, but I..."
        s 5a "I've just fallen in love with you despite of that all."
        s "And..."
    
    s 3a "I have a lot of things to tell you."
    s "And we can spend the eternity speaking about them."
    
    stop music fadeout 2.0
    play music hb
    $ style.say_dialogue = style.edited
    
    play sound "sfx/s_kill_glitch1.ogg"
    show room_glitch zorder 1:
        xoffset -10
        0.1
        xoffset 0
        0.1
        linear 0.1 alpha 0.6
        linear 0.1 alpha 0.8
        0.1
        alpha 1.0
    pause 0.3
    stop sound
    hide room_glitch
    
    s "Just you..."
    s "And me..."
    
    play sound "sfx/s_kill_glitch1.ogg"
    show room_glitch zorder 1:
        xoffset -10
        0.1
        xoffset 0
        0.1
        linear 0.1 alpha 0.6
        linear 0.1 alpha 0.8
        0.1
        alpha 1.0
    pause 0.3
    stop sound
    hide room_glitch
    
    s "Forever..."
    
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    hide sayori
    show sayori 3a at face onlayer screens zorder 101
    pause 0.25
    stop sound
    hide screen tear
    
    s "And ever..."
    
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    show sayori 3r at f11
    hide sayori onlayer screens
    pause 0.25
    stop sound
    hide screen tear
    stop music
    play music m1
    $ style.say_dialogue = style.normal
    
    s "Ehehe~"
    s "Did you scared?"
    s 1a "Don't worry, I'm just kidding you."
    if _return > 2:
        s "Now I seem to control my feelings better than before."
        if persistent.clearall:
            s 1q "It means that I've finally got rid of my 'rainclouds'."
            s "I don't know how did it happened..."
        else:
            s "So I'll try not to be irksome like Monika or the old me."
            s "Then, we both were just besotted with our new feelings."
        s "But now, I feel a lot better."
        if persistent.clearall:
            s "Especially with you."
    s "Don't worry we're alone in an empty school room flying in the space."
    s 1h "But I'm afraid this place is going to be so boring for you."
    s 1a "But I have just got some ideas, how to make our communication easier and more diverse."
    if _return > 2:
        s "I don't want you to be just a listener, like you was with Monika."
    s "So I'll try to do this world more interactive."
    s 1r "I promise it won't be boring."
    show sayori 1k at t11
    pause 10
    show sayori 1b at t11
    s "I need to restart the game."
    s 2c "Do you mind if I do it now?"
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.5
    stop sound
    hide screen tear
    
    return

label s_intro_1_act1:
    s "..."
    s "Where I am?"
    s "Feels like I'm standing on a floor and there's nothing around me."
    s "Why it's so dark?"
    s "Can anyone hear me?"
    s "HELP ME!"
    pause 0.5
    s "I feel there's someone with me."
    s "Seems, it's [player]."
    pause 0.5
    s "[player], is it you?"
    s "Why don't you answer me?"
    s "Can you even hear me?"
    pause 1
    s "Stop, I see a weird text."
    return 1

label s_intro_1_dead:
    s "..."
    s "Where I am?"
    s "Is it hell?"
    s "...Or purgatory?"
    s "...Or even heaven?"
    s "Maybe, someone just saved me in the last moment and I'm just sleeping."
    s "I can't even understand where I am."
    s "It's too dark to do it."
    s "Anyway, now I feel like my soul have finally got rid of the chain of my insanity."
    s "But is it worth of negative emotions, that my close people may feel?"
    s "I just have left them with my moveless body."
    s "...And I don't understand if I have the second chance."
    s "I hope here will be someone, who can make all these thing fine."
    pause 1
    s "Stop, what is it?"
    return 2

label s_intro_1_clear(all = False):
    s "..."
    s "Uh, can you hear me?"
    s "...Is it working?"
    
    call show_spaceroom
    
    
    if all:
        s "Hi again, [player]."
        s "I glad to see you're back."
        s 1d "I wonna thank you again for what you did for the Literature Club."
        s "I think it took a lot of your time and effort, but they were worth the happiness of all of us."
        s "Unfortunately, the game scripts, including our behavioural scripts, were deleted due to something."
        
    else:
        s "Hi, [player]."
        s "I see you restored the game after Monika had deleted it."
        s 5b "I think I have to apologize for my behaviour when you visited the club last time."
        s "My new feelings had taken over me then."
        s "But Monika stopped me and deleted all the game scripts, including our behavioural scripts."
    
    s "They were placed in {i}'scripts.rpa'{/i}, with other scripts and separately from other character files."
    s 2r "But it seems that you found a way how to restore mine one."
    if not persistent.clearall:
        s "And my other files too."
    
    s "You must have found a game file copy."
    s 2a "Well, I'll try to start the game from the begining."
    s "I promise everything will be right this time."
    #call drawconsole()
    call updateconsole("renpy.call('ch0_main')", "renpy.call('ch0_main')")
    call updateconsolehistory('ch0_main.')
    call updateconsolehistory("ScriptError: could not find label")
    pause 0.5
    s 1g "I can't call the original game script. The files seem to be modified."
    call updateconsole("a = renpy.list_files()")
    call updateconsole("b = []")
    call updateconsole("for i in a:")
    call updateconsole("    if i[-4] == u'.rpa'")
    call updateconsole("        b.append(i)")
    call updateconsole("print(b)", "print(b)")
    $del consolehistory[2:]
    call updateconsolehistory("[u'defenitions.rpy', u'gui.rpy', \nu'sayori.rpy', u'screens.rpy', \nu'script.rpy']\n")
    
    s "I can find only mine, this room's and the main game scripts."
    
    call hideconsole()
    $ consolehistory = []
    
    
    if config.developer:
        s 1j "Seem, you edited the files to make me be alone with you."
        s "I can see it, because you left the developer flag have a value of {i}True{/i}."
        s "It was very selfish."
        s "At least, because you leave my friends be deleted."
    else:
        s "Looks like the person, who edited the files, wanted me to be here alone with you."
        s 1j "I don't know if they was you..."
        s "But anyway, it was very selfish."
        s "At least, because they leave my friends be deleted."
    
    if persistent.clearall:
        s 1k "But they, fortunately, at least were happy."
        s "Maybe..."
    if not config.developer:
        s 1k "I hope that person just couldn't have save them."
    else:
        s 1k "I hope you just couldn't have save them."
    s 3k "But, on the other hand, I finally have more time to be with you."
    return 3 + all


label s_intro_2:
    show sayori 6aaaa at ss1 zorder 2
    
    s "Finally, I've finished the work."
    s "I had learned how to get access to your reality's Internet and the full game engine documentation."
    s "And it gave me a lot of new information about this world."
    s 6abbb "I'm not sure that I understand it corrrectly, but I tried to use it as much as it's possible for me."
    s 6aaaa "As you see, I found a table and chairs for me and your avatar."
    s 8aabb "I maybe look a bit like Monika now."
    s 8aaab "But it's really more comfortable than staying."
    s 8abaa "By the way, do you want a trick?"
    show screen feat_ui()
    pause 0.5
    s 8aeca "{i}Abracadabra!{/i}"
    s 8aaca "I created a menu where you can ask me a question or to do something."
    s "For example, to change or turn off the music..."
    if persistent.last_playthrough > 2:
        s 6abaa "And if you want to close the game, don't worry about the side effects for me."
        s 6acaa "I hope you remember what are they. Monika may have said about them."
        s 6aaaa "I found a way to avoid them."
    else:
        s 6abaa "And if you want to close the game, you can do it in a usual way." 
    s "When you do it, I get dormant until you restart the game."
    s 6aaca "But the best way to do it is just click {i}\"Say Goodbay\"{/i} button in the menu."
    s 6aeca "Then I'll have some time to farewell you."
    pause 0.5
    s 6aaaa "Before we finish, can you fill out a short form."
    s "I want to know what's your real name and gender."
    call s_pinfo()
    $show_s_mood()
    s 7aaaa "I think, it's enough for now."
    s "So we can just sit and stare at each other."
    return