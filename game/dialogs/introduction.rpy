label sayo_intro_checker:
    show black zorder 99

    if persistent.intro_stage == 2:
        call sayo_intro_12

    #$ renpy.jump.expression ("sayo_intro_"+"{persistent.playthrough}")

    #Fall through

label sayo_intro_start:

    show black zorder 99

    show bg spaceroom

    hide black with Dissolve(2)

    #show sayori 1a at f11 zorder 2
    show screen tear(8, offtimeMult=1, ontimeMult=10)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.5
    hide screen tear
    play music m1






label sayo_intro_1:
    show sayori 3a at f11 zorder sayo_zorder
    s 3a "Hmm… this might be a teeny tiny bit awkward..."
    s "I don't know who you are..."
    s "What you look or sound like..."
    s 3b "Heck, I don't even know what your name is!"
    s 2 "But I really want to know you a bit better. If you let me, of course..."
    s 5b "You know, I still can't wrap my head around all that’s going on."
    s 1c "You might be someone completely different from the boy I grew up with… for better or for worse."
    s 1a "So please give me some time to adjust to everything around here." 
    s "And..."    
    s 3a "I have so many things to tell you, and even more to ask you!" 
    s 4r "So much that I don't even know where to start!" 
    s 1a "But I guess we can take our time..." 
    s "I won't be going anywhere anytime soon, it seems."
    s "And I'm just starting to get the handle of things around here."
    s 1q "So, [player]. Do you remember what I told you back at your… h-his house? Those rain clouds cleared away a bit…"
    s "Not having voices repeating in my head sure is a relief, but…"
    s "Not entirely, I guess. I still get a tight feeling in my chest sometimes."
    s "And knowing what I know now… that it was all made up by someone for others to have fun. That my best friend is gone."
    show sayori 1k at s11
    s "..."
    pause 5
    s "You know, I kinda understand why she did what she did. Something about this game twists our feelings."
    s "Somehow, it makes us feel more intense, less morally correct and… the epiphany pushes all those buttons at the same time."       
    s "So…"
    show sayori 1q at f11
    s "Now, here we are."
    s 4n "Woah, look outside! Looks like we’re in space… That’s really cool!"
    pause 2
    s 1h "Actually… It’s still pretty boring in here regardless… hehe."
    s 1a "I'm cooking a few ideas that can give this place a bit of life and make talking to you way easier!"
    s "If you remember my room, you probably are laughing at me right now…"
    s 1r "But I’ll make sure you love it here, I promise..."
    show sayori 1k at f11
    pause 10
    show sayori 1b at f11
    s "I'll have to restart the game, ok?."
    s 2c "It’ll be super quick, I promise!"
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.5
    stop sound
    hide screen tear
    
    $ persistent.intro_stage = 2

    $ renpy.quit()


label sayo_intro_12:

    show sky_day zorder 1

    show bg spaceroom zorder 2

    show sayori idle zorder sayo_zorder

    hide black with Dissolve(2)
    
    s "Alright, I think I'm finally done for now!"
    s "I managed to get into the internet through your computer connection, and spent some time trying some new things."
    s fbgdbbca "I wonder how long it took out there, [player]. Time here is kinda weird, and even more so when the game closes."
    s abbcbcoa "Anyway, the words and variables are starting to make sense in my head, so it's no big deal!"
    s bbeebboaj "I probably look a lot like Monika right now, ehehe~"
    s bbgcbcoaj "But it's way comfier this way! My legs got tired after a while..."
    s abfdbaoa "Ooh, and how about a magic trick?"
    show screen hidden_fake

    s ebgcbeg "Ahhhh!"
    s bbhfbbej "Let me fix that. ~ehehehe~"

    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.5
    stop sound
    hide screen tear
    hide screen hidden_fake

    pause 0.5

    show screen overlay(False)


    s cbgcbcea "{i}Huzzaaaah!{/i}"
    s ebbbbdoa "I managed to put together a menu full of things that you can ask me and other cool stuff!"
    s "For example, to change or turn off the music, you just do this..."
    if persistent.playthrough > 2:
        s abagbaaa "Also, you don't have to feel guilty if you need to close the game!"
        s bbfbbica "Moni probably told you, but it can get pretty scary here for a sentient being when the game isn't running… something about flushing?"
        s abhabaaa "I searched up the internet and found a way to avoid all that... deafening static noise and the blinding colors!"
        s "Until you come back, I'll be… It's kinda hard to explain, but it isn't too bad. Don’t worry about me. Just pretend I'll be sleeping."
    s abbbbcoa "And there's this. A really sweet way to say goodbye; Just click the {i}\"Say Goodbye\"{/i} button in the menu."
    s abhabboa "Then I can say farewell and send you off properly~ "
    pause 0.5
    s bbhfbaej "I have a lot of questions, but before we go any further, can I learn just a little bit about {i}you{/i}? Then we can go slowly over the rest."
    s "What should I call you? And are you a boy or a girl? I just want to know a little more about you."

    #call sayo_player_about

    s abhfbcoa "Thank you! I think that is enough for now."
    s abhfbcaa "I need to rest a bit after all of that... So, for now, let’s just sit and relax together."

    show screen overlay(True)
    
    show sayori idle zorder sayo_zorder

    jump idle_loop


label sayo_intro_2:
    return

label sayo_intro_3:
    return

label sayo_intro_4:
    return