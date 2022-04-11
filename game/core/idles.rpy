
label sayo_autoload:
    #Start with black screen
    scene black

    python:
        quick_menu = True
        style.say_dialogue = style.normal
        in_sayori_kill = None
        allow_skipping = True
        config.allow_skipping = False

    #Do all the things for initial setup flow

    #TODO: FINAL FAREWELL MODE

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
        
    #show sayori acbaba with moveinleft
    hide black with Dissolve(2)
    scene bg spaceroom with Dissolve(2)
    

    #FALL THRouGH




label idle_loop:
    #show sayori idle
    show screen hidden
    #show screen hidden
    
    show sayori acbaba with moveinleft
    
    while persistent._event_list:
        call cnc



label idle_wait:
    window hide

    $ renpy.pause(delay=5.0, hard=True)
    jump idle_loop

    #jump idle_loop
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