default persistent._event_db = dict()


init -2 python in sayo_events:
    import random
    import store
    import store


    EVENT_DEFS = dict()


    def event_selector():

        kwargs = dict()

        event_list = store.Chat.chat_filt(
            EVENT_DEFS.values(),
            unlocked=True,
            has_seen=False,
            **kwargs
        )

        if len(event_list) > 0:
            return random.choice(event_list).label
        
        else:
            return None

label d_day_control:
    call sayo_d_day_death

    show bg spaceroom with flash

    call sayori_d_day



label sayori_d_day:

    #IF YOU MAKE HER SAD I WILL EAT YOUR CHILDREN -NATHAN :)

    #show bg spaceroom zorder 1
    #show sayori_d_day_note zorder 11

    $ persistent.d_day = True

    python:
        disable_esc()
        allow_dialogue = False
        layout.QUIT = glitchtext(20)
        #Console is not going to save you.
        #If you've got to this point, you've consiously tried to be an ass
        #Therefore you deserve what happens now
        config.keymap["console"] = []
    
    jump d_day_real

label d_day_real:
    
    #add(D_DAY_POEM_DISPLAY())
    
    call showpoem(poem_d_day)

    $ persistent.nwb = True

    menu:
        "I'm sorry":
            pass
        "...":
            pass
    
    $ persistent.cthulu_d_day = True
    jump d_day_real

label sayo_d_day_death:
    window hide(None)
    window auto
    play music td
    show s_kill_bg2
    show s_kill2
    show s_kill_bg as s_kill_bg at s_kill_bg_start
    show s_kill as s_kill at s_kill_start
    $ pause(3.75)
    show s_kill_bg2 as s_kill_bg
    show s_kill2 as s_kill
    $ pause(0.01)
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.25)
    stop sound
    hide screen tear
    hide s_kill_bg
    hide s_kill
    show s_kill_bg_zoom zorder 1
    show s_kill_bg2_zoom zorder 1
    show s_kill_zoom zorder 3
    show s_kill2_zoom zorder 3
    show s_kill as s_kill_zoom_trans zorder 3:
        truecenter
        alpha 0.5
        zoom 2.0 xalign 0.5 yalign 0.05
        pause 0.5
        dizzy(1, 1.0)
    $ pause(2.0)
    show noise zorder 3:
        alpha 0.0
        linear 3.0 alpha 0.25
    show vignette zorder 3:
        alpha 0.0
        linear 3.0 alpha 0.75
    $ pause(1.5)
    show white zorder 2
    show splash_glitch zorder 2
    $ pause(1.5)
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.2)
    stop sound
    hide screen tear
    $ pause(4.0)
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.2)
    stop sound
    hide screen tear
    hide splash_glitch
    show splash_glitch2 zorder 2
    show splash_glitch_m zorder 2
    show splash_glitch_n zorder 2
    show splash_glitch_y zorder 2
    $ pause(0.75)
    hide white
    hide splash_glitch2
    hide splash_glitch_m
    hide splash_glitch_n
    hide splash_glitch_y
    show exception_bg zorder 2
    show fake_exception zorder 2:
        xpos 0.1 ypos 0.05
    show fake_exception2 zorder 2:
        xpos 0.1 ypos 0.15
    python:
        try: sys.modules['renpy.error'].report_exception("Oh jeez...I didn't break anything, did I? Hold on a sec, I can probably fix this...I think...\nActually, you know what? This would probably be a lot easier if I just deleted her. She's the one who's making this so difficult. Ahaha! Well, here goes nothing.", False)
        except: pass
    $ pause(6.0)

    hide fake_exception
    hide fake_exception2
    hide exception_bg

    scene black with dissolve_cg

    return