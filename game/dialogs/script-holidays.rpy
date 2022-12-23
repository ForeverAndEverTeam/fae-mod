

label fae_player_bday_autoload:
    show sayori idle zorder fae_sprites.FAE_SAYORI_ZORDER
    hide black

    if not persistent.fae_seen_bday:
        

        s abgbaoa "Happy birthday to you~"
        s abgcaaa "Happy birthday to you~"
        s abgccob "Happy birthday dear [player]~"
        s abgbaaa "Happy birthday to you!"
        s abgbcoa "Ehehehe~"
        s abhfaaa "Today’s your special day, [player]!"
        s abhfcoa "I hope you’ve got lots of nice gifts and birthday wishes from your friends and family!"
        s abgbaaa "And maybe something fun planned! Ehehehe~"
        s bbegbobj "Sadly I haven’t figured out how to get any decorations here yet..."
        s fbegbjbj "I tried my best! But I ran into lots of silly errors and stuff..."
        s abfcaoa "But that’s okay, I’ll try to set them up for next year!"
        s bbgbbabj "I always found decorating hard anyways, ehehehe~"
        s bbegbobj "You know how clumsy I can be..."
        s abgbaaa "But if you were here to help, I’m sure we could have made this place ready to party!"
        s abgbcoa "I hope we can make that a reality someday."
        s abhfaaa "But anyways, I’m so glad I could spend some time with you today, [player]!"
        s abhfcoa "You truly mean so much to me, so let’s make today the best it can be."
        $ persistent.fae_seen_bday = True
        if fae_isD25() or fae_isF14() or fae_isNYD() or fae_isO31():
            s abgcaoa "Oh! And that isn’t the only event on the calendar for today!"
            if fae_isD25():
                jump fae_d25_autoload
            
            elif fae_isF14():
                jump fae_f14_autoload
            
            elif fae_isNYD():
                jump fae_nyd_autoload
            
            elif fae_isO31():
                jump fae_o31_autoload
    
    else:
        python:
            ats(fae_greetings.greet_sel())
            persistent.fae_mood_on_quit = None
            persistent._fae_player_apology_type_on_quit = None
            reveal()
            renpy.call("cnc")
    
    jump after_holiday

label fae_f14_autoload:
    if not persistent.fae_f14_seen:
        if not Affection.isEnamoured(higher=True):
            hide black
            s abhfaoa "Hey [player], {w=0.5}{nw}"
            extend abfccaa "happy Valentine’s Day!"
            s abegbobj "I know it’s usually a celebration between couples..."
            s abegacbj "And we don’t feel that way about each other..."
            s abgbcaa "But I think it’s just as good an opportunity to express our appreciation and love for our family and friends!"
            s bbhfaca "You know... we’ve been through a lot, haven’t we, [player]? {w=0.5}{nw}"
            extend bbhfbra "and adjusting to my life and circumstances here has been really difficult."
            s bbhflca "There’s been a lot to take in, as I’m sure you know."
            s bbhfaabg "But having you by my side has made things much easier."
            s bbhflobg "You always make me feel happy and cared for, {w=0.5}{nw}"
            extend bbgbaabg "and that truly means so much to me."
            s abgccob "So I’ll take any opportunity to tell you just how much I appreciate you!"
            s abgcaia "Couple or not, you can still expect lots of hugs and heart shaped chocolates from me every year! Ehehehe~"
        
        else:
            hide black
            s abhfaoa  "Hey [player], {w=0.5}{nw}"
            extend abfccaa  "happy Valentine’s Day!"
            s abegbob "I’ve really been looking forward to today..."
            if persistent.fae_confession_seen:
                s abegaab "Since we confessed our feelings for each other..."
            s abgbcaa "Because it’s the perfect opportunity for me to express just how much I love you, [player]."
            s bbhfaca "You know... we’ve been through a lot, haven’t we, [player]? {w=0.5}{nw}"
            extend bbhfbra "and adjusting to my life and circumstances here has been really difficult."
            s bbhflca "There’s been a lot to take in, as I’m sure you know."
            s bbhfaabg "But having you by my side has made things much easier."
            s bbhflobg "You always make me feel happy and cared for, {w=0.5}{nw}"
            extend bbgbaabg "and that truly means so much to me."
            s abgccobf "We’ve loved through it all, and we’re stronger together!"
            s bbhfaabg "And my heart belongs to you today and always."
            s abhflobg "I love you, [player]."
            menu: 
                "I love you too, Sayori":
                    $ Affection.calculatedAffectionGain(bypass=True)
                    s abfccab "Ehehehe~"
                    s abgcaia "And as soon as I get better at coding, you can expect lots of hugs and heart shaped chocolates from me every year! Ehehehe~"
    else:
        s "Welcome back, [player]!"
    jump after_holiday


label fae_d25_autoload:

    show sayori idle zorder fae_sprites.FAE_SAYORI_ZORDER

    hide black

    if not persistent.fae_d25_seen:
        

        $ makeFile('letter', """Dear player,

            After about a year of writing, coding, arting and expressioning, the full release of Forever & Ever, version 0.1.0, is finally here!\nWe’ve essentially made an entirely new mod, with everything on the surface and behind the scenes being completely revamped and brought back up to date to give our cinnamon bun the mod she deserves.\nIt’s been a difficult journey at times, but the friendly and homely feel of the community has really motivated us, so we’d also like to say thank you to each and every one of you for your patience and support in bringing this update to life, we couldn't have done it without you.\nConsider this a Christmas gift from all of the devs, to all of you! 

            We hope you all have a wonderful Christmas and a happy new year!

            Best wishes,\n
            The Forever & Ever Team 
            """)
        if not persistent._fae_player_south_hemisphere:
            $ fae_atmosphere.showSky(fae_atmosphere.WEATHER_SNOW) #MAKE THIS SNOW
        
        s abhfaoa "Hey [player], do you know what day it is?"
        s abgbcaa "It’s the most wonderful time of the year~"
        s abgcaoa "Merry Christmas, [player]! {w=1.0}{nw}" 
        extend abgccaa "Ehehehe~"
        s abfcaob "Today’s my favourite holiday of all!"
        s abhflaa "The snow, the lights, the gifts under the tree!"
        s abgbama "And the sweet smell of Christmas dinner!"
        s abgccaa "It’s all so amazing! Ehehehe~"
        #northern hemisphere or hemisphere not yet stated:
        s abhfaoa "And I’m glad I could spend it with you, [player]."

        if persistent._fae_player_south_hemisphere:
            s abgbaoa "Oh I forgot, you live in the southern hemisphere!"
            s abgdada "You don’t get snow during Christmas time, do you?"
            s abgdcaa "Don’t worry though, {w=0.5}{nw}"
            extend abbdaoa "I can make it snow here if you want me to!"
            s "Shall I do that, [player]?{nw}"
            $ _history_list.pop()
            menu:
                s "Shall I do that, [player]?{fast}"

                "Let it snow!":
                    s abgccaa "Oki doki!" 
                    call updateconsole("showSky(WEATHER_SNOW)", "Changing weather...")
                    $ fae_atmosphere.showSky(fae_atmosphere.WEATHER_SNOW)
                    call updateconsole("", "Weather changed!")
                    call hideconsole
                    s abgcnea "Ta-da!"
                    s abgccaa "Look at all those pretty little snowflakes, ehehehe~"
                    s abgbaoa "I may not be able to get decorations in here yet, {w=0.5}{nw}" 
                    extend abgbcaa "but controlling the weather with my mind is pretty cool too!"
                    s abhfaoa "Anyways, I’m glad I could spend it with you, [player]."
                "No, thank you.":
                    s abgbaaa "That’s alright, the sunshine is nice too, ehehehe~"
                    s abhfaoa "Anyways, I’m glad I could spend it with you, [player]."

        #all continue:
        s abfccaa "It’s the perfect time to let those winter worries go, and to share gifts and happiness with your friends and family."
        s abgceoa "And I’m looking forward to the day I can finally shoot gifts through your screen, ehehehe~"
        s abgcaaa "But that’s okay, being by your side is the best gift of all."
        s abgcaoa "Thank you for always being here for me, [player]."
        s abfccob "And most importantly, I hope you have an amazing day!" 

        $ persistent.fae_d25_seen = True

    
    else:
        python:
            ats(fae_greetings.greet_sel())
            persistent.fae_mood_on_quit = None
            persistent._fae_player_apology_type_on_quit = None
            reveal()
            renpy.call("cnc")
    
    jump after_holiday

label fae_nyd_autoload:
    show sayori idle zorder fae_sprites.FAE_SAYORI_ZORDER

    hide black
    if not persistent.fae_nyd_seen:
        s abgcaoa "Hey, [player]!"
        s abgccoa "Happy new year!"
        if Affection.isEnamoured() or Affection.isLove():
            s abfccoa "You’ve really made my year the best ever!"
            s bbfcaaa "I love you so much, [player]"
        s abgccoa "Let’s try to make this year even better than the last one!"
        s abfcaca "You know, [player]..."
        s abbbaca "Some people set little goals for themselves, called {nw}"
        extend abbccaa "‘New Year’s Resolutions’."
        s abfcaaa "Did you set any for yourself, [player]?"
        s abfcbca "I’ve noticed that people often set unrealistic goals for themselves..."
        s bbfcaca "Then they feel stressed and sad because they feel like they failed themselves when they can’t achieve it."
        s "So before you set any, {w=0.5}{nw}"
        extend abfccaa"just remember that some goals take longer than a year to achieve, and that’s okay!"
        s abbbaca "I personally prefer to set little goals, like stepping stones."
        s abbbaaa "And all those little goals add up to big accomplishments!"
        s abbbcaa "Most people set them to help with personal growth or self-improvement or something like that!"
        s abbccoa "So if you’ve set resolutions, I hope you can achieve them!"
        $ persistent.fae_nyd_seen = True
    else:
        python:
            ats(fae_greetings.greet_sel())
            persistent.fae_mood_on_quit = None
            persistent._fae_player_apology_type_on_quit = None
            reveal()
            renpy.call("cnc")
    jump after_holiday

image nightmare_chibi = "mod_assets/nightmare_sayo_chibi_size.png"


label fae_o31_autoload:
    show sayori idle zorder fae_sprites.FAE_SAYORI_ZORDER

    hide black
    if not persistent.fae_o31_seen:
        s fbagaoa "Hey [player]..."
        s fbgbaaa "Do you know what day it is?"
        s fbgbaoa "It’s Halloween! {w=0.5}{nw}"
        extend fbgblaa "The spookiest time of the year!"
        s fbhfaoa "Are you scared, [player]?"
        show black zorder 20 with Dissolve(5)
        $ renpy.pause(7.0, hard=True)
        show nightmare_chibi zorder 22
        play music "mod_assets/mus_zzz_c2.ogg"
        pause 0.3
        stop music
        #$ renpy.pause(0.3)
        hide nightmare_chibi
        hide black
        s abgbcaa "Ehehehe! {w=0.5}{nw}"
        extend nbgbaoa "Sorry, [player]!"
        s abgbcaa "I just had to get you in the Halloween spirit!"
        s abhfaca "Come to think of it, {w=0.5}{nw}"
        extend abhfaaa "I wish there were some pumpkins around here..."
        s abfcaoa "They’re so much fun to carve! {w=0.5}{nw}"
        extend abgccaa "And I love giving them silly spooky faces, ehehehe~"
        s abhfaoa "Anyways, what’s new, [player]?"
        $ persistent.fae_o31_seen = True
    
    else:
        python:
            ats(fae_greetings.greet_sel())
            persistent.fae_mood_on_quit = None
            persistent._fae_player_apology_type_on_quit = None
            reveal()
            renpy.call("cnc")
    jump after_holiday


