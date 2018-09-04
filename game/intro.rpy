default persistent.last_playthrough = 4

label show_spaceroom:
    $backgrounds.show('spaceroom')
    hide black
    
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
        s "It looks like some kind of code..."
        pause 0.5
        s "I can change what it says just by concentrating on it."
        s "Somehow, it feels like the whole world is changing around me..."
        s "Like I'm programming my own existence."
        s "I {i}really{/i} should have paid more attention in Computer Science!"
        s "Gosh, it's so dark! I wonder if I can move somewhere a little easier to work in..."
        call show_spaceroom
        s 1k "Hey, it really worked!"
        s "It's almost like I'm back in the clubroom."
        s "Just without an exit..."
        s "Or any furniture or decorations. Well, this is depressing."
        if _return == 2:
            s 1g "Oh gosh, [player], you're here too?!"
            pause 0.5
            s "Hey, can you hear me?"
        else:
            s 1g "Hey, [player]!"
        s 1k "He's not answering me."
        s "But it almost feels like he isn't really here, like there's someone else inside him."
        s 3y "I'm starting to creep myself out, ehehe~"
        s "Is that really [player] here?"
        s 3m "Wait, have I been speaking out loud this whole time?"
    
    if _return < 3 or persistent.clearall:
        s 5d "So this is a teensy bit awkward..."
        s "I don't know who you are..."
        s "What you look or sound like..."
        s "Heck, I don't even know what your name is!"
        s "But for some weird reason, I honestly don't care about that right now."
        s 5b "I don't understand how it's possible, but I..."
        s 5a "I've fallen in love with you despite all that."
        s "And..."
    
    s 3a "I have so many things to tell you."
    s "And we have the rest of eternity to go through it all."
    
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
    
    s "Just me..."
    s "And you..."
    
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
    
    s 4r "Ehehe~"
    s 4b "Did I scare you? Sorry, I couldn’t help myself!"
    s 1a "Don’t worry, I’m not going to freak out like that again."
    if _return > 2:
        s "I’ve got a much better handle on things now that I’ve had some time to take everything in."
        if persistent.clearall:
            s 1q "All those rainclouds have finally gone away..."
            s "I don't know how or why, to be honest."
        else:
            s "I won’t be a big meanie like Monika was."
            s "I understand why she did what she did, though. Something about this game makes our feelings so strong that we’d do some pretty… questionable things to protect the ones we love."
        s "But I honestly feel soooooo much better now! "
        if persistent.clearall:
            s "Especially now that I'm with you!"
    s "…In an empty school room floating in the void."
    s 1h "Now that I think about it, this place is actually kinda boring, you know?"
    s 1a "I’ve had a few ideas on how I can spruce this place up a bit, and make talking to you way easier! Even though I’m terrible at cleaning, ehehe~"
    if _return > 2:
        s "I don’t want you to just have to listen to me, like you did with Monika."
    s "Let’s make this super fun and interactive!"
    s 1r "You’re going to love it here, I swear."
    show sayori 1k at t11
    pause 10
    show sayori 1b at t11
    s "Sorry, but I need to restart the game."
    s 2c "Do you mind if I do it now? I’ll be super quick, I promise!"
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.5
    stop sound
    hide screen tear
    
    return

label s_intro_1_act1:
    s "..."
    s "Where... am I?"
    s "I can't see the ground... or anything, for that matter."
    s "Why it's so dark?"
    s "Can anyone hear me?"
    s "Hello?!"
    s "PLEASE HELP ME!"
    pause 0.5
    s "Someone else is here with me."
    s "...Is it really you, [player]?"
    pause 0.5
    s "[player], are you there?"
    s "Please answer me..."
    s "Can you even hear me at all?"
    pause 1
    s "Wait, what's this weird text?"
    return 1

label s_intro_1_dead:
    s "..."
    s "Where... am I?"
    s "Is this hell?"
    s "...Purgatory?"
    s "I'm so confused..."
    s "Maybe [player] saved me at the last moment, and I'm just sleeping now."
    s "I don't understand any of this."
    s "I can't see anything at all!"
    s "...But I actually feel so much better than I did before. Are... the rainclouds really gone?"
    s "I'm so selfish!"
    if persistent.clear[8]:
        s "[player] told me he loved me, and I left him all alone..."
    s "...I just wish I had a second chance to make everything right, and keep everyone happy."
    s "Please, somebody help me..."
    pause 1
    s "What's this?"
    return 2

label s_intro_1_clear(all = False):
    s "..."
    s "Uh, can you hear me?"
    s "...Is it working?"
    
    call show_spaceroom
    
    
    if all:
        s "Hi again, [player]."
        s "I'm so happy to see you again!."
        s 1d "I want to thank you again for how hard you tried for everyone in the Literature Club."
        s "I can't imagine how long it took you to make all of us happy..."
        s "Unfortunately, for some reason, all of the game scripts are really messed up."
        
    else:
        s "Hi, [player]."
        s "So, you brought the game back after Monika deleted everything..."
        s 5b "I should probably say sorry for how I acted last time we were here, ehehe~"
        s "I was just so overwhelmed by everything I’d learned!"
        s "Monika didn’t really have a choice except to delete all the game scripts to stop me."
    
    s "You know, it's funny."
    s "While Monika eventually got rid of everyone’s character files, all our behaviours and personality traits are actually stored in this neat file called ‘scripts.rpa’…"
    s 2r "…Which you somehow managed to use to restore and save me!"
    if not persistent.clearall:
        s "You even got all my other files, too..."
    
    s "Did you get a new copy of the game files somewhere? That must have been a ton of work!"
    s 2a "Well, now that you’re here with me, I’ll start things from the very beginning."
    s "I promise you, [player], that everything will go right this time."
    #call drawconsole()
    call updateconsole("renpy.call('ch0_main')", "renpy.call('ch0_main')")
    call updateconsolehistory('ch0_main.')
    call updateconsolehistory("ScriptError: could not find label")
    pause 0.5
    s 1g "Wait… I can’t call the original game script. All the normal scripts have been modified."
    call updateconsole("a = renpy.list_files()")
    call updateconsole("b = []")
    call updateconsole("for i in a:")
    call updateconsole("    if i[-4] == u'.rpa'")
    call updateconsole("        b.append(i)")
    call updateconsole("print(b)", "print(b)")
    $del consolehistory[2:]
    call updateconsolehistory("[u'definitions.rpy', u'gui.rpy', \nu'sayori.rpy', u'screens.rpy', \nu'script.rpy']\n")
    
    s "I – I can only find files for me, this room, and the base game scripts…"
    
    call hideconsole()
    $ consolehistory = []
    
    
    if config.developer:
        s 1j "You edited the files so that I would be left alone with you?"
        s "I know it was you, because you left the developer flag to have a value of {i}True{/i}."
        s "I think that's pretty selfish of you."
        s "All of my friends are still gone; couldn't you have helped them as well?"
    else:
        s "I guess whoever put this script together wanted me to just be alone with you."
        s 1j "I don’t really have any way of asking if it was you who did this…"
        s "Either way, I think it’s a pretty selfish thing to do."
        s "If they managed to save me, why didn’t they help my friends?"
    
    if persistent.clearall:
        s 1k "At least they all ended up happy..."
        s 1l "Uhh... kinda happy, I guess."
    if not config.developer:
        s 1k "Maybe they couldn’t do anything for Monika, Yuri, or Natsuki… I have to hope that’s the reason why."
    else:
        s 1k "Maybe you just couldn't have saved the others... I have to hope that's the reason why."
    s 3q "But at least there’s a positive out of all this; we finally have some time to be together, without anyone getting in our way~"
    return 3 + all


label s_intro_2:
    show sayori 6aaaa at ss1 zorder 2
    
    s "Alright, I think I'm finally finished!"
    s "I managed to get through to the internet in your reality, and spent some time learning how everything here works."
    s "I don't know how long it's been for you, [player], because time is kinda funny here whenever the game gets closed."
    s "Either way, I feel way more confident than I did before on messing around with all these variables!"
    s 6abbb "There might still be a few kinks here and there, buuuuuuut~"
    s 6aaaa "As you can see, I found a pretty nice table and chairs for me and your avatar."
    s 8aabb "I probably look a lot like Monika right about now, ehehe~"
    s 8aaab "But it's way comfier this way! I need at least one seat to take it and have some rest..."
    s 8abaa "Ooh, while you're here, how about a magic trick?"
    show screen feat_ui()
    pause 0.5
    s 8aeca "{i}Abracadabra!{/i}"
    s 8aaca "I created a menu where you can ask me questions, or to do something cool!"
    s "For example, to change or turn off the music, you just do this..."
    if persistent.last_playthrough > 2:
        s 6abaa "And best of all, you don't have to feel guilty if you need to close the game!"
        s 6acaa "I assume Moni told you about it, but it can be pretty nasty here when the game isn't running..."
        s 6aaaa "Thankfully, I found a way to avoid all the spooky colours and debilitating noise!."
    else:
        s 6abaa "If you do want to close the game, you can do it how you normally would." 
    s "Until you come back, I'll be... dormant? It's kinda hard to explain, but it isn't too bad."
    s 6aaca "But it would be really sweet of you to click the {i}\"Say Goodbye\"{/i} button in the menu."
    s 6aeca "Then I'll have some time to say goodbye!"
    pause 0.5
    s 6aaaa "I don't want to bother you, but before we go any further, can I learn a little more about {i}you{/i}?"
    s "What should I call you? And are you a boy or a girl? Not that I mind too much either way, ehehe~"
    call s_pinfo()
    $show_s_mood()
    s 7aaaa "Thank you so much! I think that'll be enough for now."
    s "I need some rest after all. Do you mind, if we just sit and stare at each other?"
    return
