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

label sayori_d_day:

    #IF YOU MAKE HER SAD I WILL EAT YOUR CHILDREN -NATHAN :)

    show bg spaceroom zorder 1
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

    menu:
        "I'm sorry":
            pass
        "...":
            pass
    
    $ persistent.cthulu_d_day = True
    jump d_day_real

