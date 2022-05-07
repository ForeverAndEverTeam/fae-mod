init python:
    import subprocess
    import os
    import re
    #import store.sounds as sounds
    #import store.sayo_utilities as utilities

    renpy.music.register_channel(
        "background",
        mixer="amb",
        loop=True,
        stop_on_mute=True,
        tight=True
    )

    # also need another verison of background for concurrency
    renpy.music.register_channel(
        "backsound",
        mixer="amb",
        loop=False,
        stop_on_mute=True
    )



label sayo_autoload:

    #Start with black screen
    scene black

    # D DAY MODE CHECK

    $ persistent.d_day = True

    python:
        quick_menu = True
        style.say_dialogue = style.normal
        in_sayori_kill = None
        allow_skipping = True
        config.allow_skipping = False

    #Do all the things for initial setup flow

    
    #TODO: FINAL FAREWELL MODE

    if persistent.d_day:
        jump d_day_control

    #FALL THROUGH

label sayo_setup:

    #SET UP BG AND STUFF BEHIND A BLACK SCREEN

    show black zorder 99

    show bg spaceroom zorder 1

    #scene bg spaceroom zorder 1

    #FALL THROUGH

label sayo_init:

    python:
        import random
        init_qabs()
        renpy.save_persistent()
        
        if not cielp("^greeting_"):
            if (
                random.randint(1, 10) == 1
                and sayo_events.event_selector()
            ):
                ats(sayo_events.event_selector())
                renpy.call("cnc", False)
            else:
                ats(greetings.greet_sel())
    #$ begin_song()
    
    #show sayori idle zorder sayo_zorder with moveinleft 
    #show bg spaceroom zorder 1
    hide black with Dissolve(2)

    #FALL THRouGH

label idle_loop:
    
    show sayori idle zorder sayo_zorder with moveinleft 
    
    while persistent._event_list:
        call cnc

    show screen hidden

label idle_wait:
    window hide

    show sayori abaabaa

    $ renpy.pause(delay=5.0, hard=True)
    jump idle_loop

label cnc:
    if persistent._event_list:
        $ _chat = persistent._event_list.pop(0)

        if renpy.has_label(_chat):

            call expression _chat
    
    python:
        return_keys = _return if isinstance(_return, dict) else dict()

        chat_obj = get_chat(_chat)

        if chat_obj is not None:
            chat_obj.seen_no += 1
            chat_obj.latest_seen = datetime.datetime.now()

            if "derandom" in return_keys:
                chat_obj.random = False
    
    if "quit" in return_keys:
        jump quit
    
    python:
        global LCC
        LCC = datetime.datetime.now()
    jump idle_loop