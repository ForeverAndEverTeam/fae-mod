default persistent._event_db = dict()
default persistent._fae_holiday_list = dict()
default persistent._fae_holiday_completion_states = dict()

image asset mr_cow = "mod_assets/images/EVENT/mr_cow.png"
image asset spe1 = "mod_assets/images/EVENT/spe1.png"
image asset spe2 = "mod_assets/images/EVENT/spe2.png"
image asset desk = "mod_assets/sayori/table/desk.png"
image asset chair = "mod_assets/sayori/table/chair.png"
image asset desk_shadow = "mod_assets/sayori/table/desk_sh.png"
image asset note = "mod_assets/sayori/table/note.png"
image asset knife = Image("mod_assets/images/EVENT/pointy_stick.png", yoffset=1)



image asset mr_cow_desk = Composite(
    (1280, 720),
    (0, 0), "mod_assets/sayori/table/chair.png",
    (0, 0), "mod_assets/images/EVENT/mr_cow.png",
    (0, 0), "mod_assets/sayori/table/desk.png",
    (0, 0), "mod_assets/sayori/table/desk_sh.png"
)


init -1 python in fae_events:
    import random
    import store
    #import store
    import datetime
    from Enum import Enum
    import store.fae_music as fae_music
    import store.fae_sky as fae_sky
    import store.fae_affection as fae_affection
    import store.fae_globals as fae_globals
    import store.fae_outfits as fae_outfits
    import store.fae_utilities as fae_utilities

    FAE_EVENT_DECOR_ZORDER = 2
    FAE_EVENT_ASSET_ZORDER = 4
    
    EVENT_DEFS = dict()
    EVENT_RETURN_OUTFIT = None

    




    def event_selector():

        kwargs = dict()

        event_list = store.Chat.chat_filt(
            EVENT_DEFS.values(),
            unlocked=True,
            affection=store.Affection._getAffectionStatus(),
            has_seen=False,
            **kwargs
        )

        if len(event_list) > 0:
            return random.choice(event_list).label
        
        else:
            return None
    

    
    
    
    def show_visuals(
        sayori_sprite_code,
        bgm="mod_assets/bgm/s1_ac.ogg"
    ):


        renpy.show("sayori {0}".format(sayori_sprite_code), at_list=[store.fae_center], zorder=store.fae_sprites.SAYO_ZORDER)
        renpy.hide("black")

        renpy.play(filename=bgm, channel="music")

        renpy.hide("black")
    
 

label event_new_years_eve:
    $ fae_events.getHoliday("event_new_years_eve").run()
    s "[player]!{w=1}{nw}"
    s "[player]!{w=0.5} [player]!"
    s "Look at the date!{w=0.5}{nw}"
    extend " Do you even know what day it is?!{w=1}{nw}"
    extend " It's almost the new year!"
    s "Man...{w=1}{nw}"
    extend " and about time too,{w=0.1} huh?"
    s "I don't know about you,{w=0.1} [player]...{w=1}{nw}"
    $ current_year = datetime.date.today().year
    extend " but I can't {i}WAIT{/i} to tell [current_year] where to stick it!"
    s "And what better way to do that...{w=0.75}{nw}" 
    extend " than a crap ton of explosions and snacks?"
    s "Ehehe.{w=0.5}{nw}"
    extend " It's gonna be great!"

    

    $ fae_events.getHoliday("event_new_years_eve").complete()

    return




init 5 python:
    chatReg(
        Chat(
            persistent._event_db,
            label="fae_event_mr_cow_transform20",
            unlocked=True,
            affection_range=(fae_affection.NORMAL, None)
        ),
        chat_group=CHAT_GROUP_EVENT
    )

label fae_event_mr_cow_transform20:

    hide black

    $ fae_globals.allow_force_quit = False

    show asset mr_cow_desk as mr_cow_desk zorder fae_sprites.SAYO_ZORDER
   
    s "[player] heeeeeeelp!!!"
    s "I was messing with the code and accidentally turned myself into Mr. Cow!"
    s "Noooooooo!!!!"
    
    pause 1.5
    
    s "Pffffftt-"
    
    show asset spe1 zorder 2

    
    s "Bwahahahahah- I'm sorry, [player]!"
    s "I'm fine- I just couldn't resist that one!"
    s "I'll go put him away now, I'll be back in a sec!"
    
    hide mr_cow_desk
    
    hide asset spe1

    $ fae_events.show_visuals("abhfbcqa")

    #show sayori idle at t11 zorder fae_sprites.SAYO_ZORDER
    
    s abhfbcqa "There we go, ehehe~"
    s abhfbcoa "Welcome back, [player]!" 
    s abhabbsa "I was just kinda starting to miss you so…"
    s abhabcea "I dug in the code until I could rescue Mr. Cow!"
    s abbbbloa "It was hard work, buuuuut!"
    s abgcbdoa "Now I'll always have someone to cuddle with, and it'll never get {i}too{/i} lonely in here!"
    s abhfbcaa "Anyways,I'm glad you're here now!" 
    return
    
init 5 python:
    chatReg(
        Chat(
            persistent._event_db,
            label="fae_event_pointy_stick_stabber_girl",
            unlocked=True,
            affection_range=(fae_affection.NORMAL, None)
        ),
        chat_group=CHAT_GROUP_EVENT
    )

label fae_event_pointy_stick_stabber_girl:

    #$ fae_events.show_visuals("abbcbckc")

    hide black

    #$ fae_events.show_visuals("idle")

    show sayori idle at fae_center zorder fae_sprites.SAYO_ZORDER


    show asset knife as knife at fae_center zorder fae_sprites.SAYO_ZORDER

    

    s abbcbckc "Hi, [player]! Ready to chop up some bitches?"
    s "Does this look like the face of mercy, [player]?"
    s bbfcbeea "AHAHAHA….{nw}"
    extend bbfcbdia"Just kidding!"
    s abbcbiia "Sorry about that!"
    
    menu:
        "Where did you even get that???":
            pass
    
    s eahcbbsa "Great question!{w=1.0} {nw}"
    extend eahcbada "I've been doing some more digging into the code to recover as much stuff as possible!"
    
    s ebbcbcqa "I managed to get this knife back today!"
    s fbfcbkdaj"Not really sure if I'll ever need it for anything, but I figured I might as well have it."
    s bbfcbmoaj "But maybe it's better if I put this away now."
    s bbbcbciaj "I wouldn't want anything bad to happen, ehehe~"
    
    hide knife 
    
    s abhabaoa "Hope you're doing good today, [player]~" 
    s abhabiia "Did I make you nervous?"
    s ebhhbcoa "Sorry for scaring you, ehehe~"
    
    return
