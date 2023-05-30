default persistent._event_db = dict()
default persistent._fae_holiday_list = list()
default persistent._fae_holiday_completion_status = dict()

default persistent._fae_player_anniversary = None
#default persistent._fae_holiday_list = dict()
#default persistent._fae_holiday_completion_states = dict()

image asset mr_cow = "mod_assets/images/EVENT/mr_cow.png"
image asset spe1 = "mod_assets/images/EVENT/spe1.png"
image asset spe2 = Image("mod_assets/images/EVENT/spe2.png", yoffset=-100)
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

    
    EVENT_DEFS = dict()
    EVENT_RETURN_OUTFIT = None

    
    FAE_EVENT_DECOR_ZORDER = 2
    FAE_EVENT_ASSET_ZORDER = 4

    

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


        renpy.show("sayori {0}".format(sayori_sprite_code), at_list=[store.fae_center], zorder=store.fae_sprites.FAE_SAYORI_ZORDER)
        renpy.hide("black")

        renpy.play(filename=bgm, channel="music")

        renpy.hide("black")
    
label event_interlude:
    s "..."
    return
 


init 5 python:
    chatReg(
        Chat(
            persistent._event_db,
            label="fae_event_mr_cow_transform",
            unlocked=False,
            affection_range=(fae_affection.NORMAL, None)
        ),
        chat_group=CHAT_GROUP_EVENT
    )

label fae_event_mr_cow_transform:

    hide black

    $ fae_globals.allow_force_quit = False

    show asset mr_cow_desk as mr_cow_desk zorder fae_sprites.FAE_SAYORI_ZORDER
   
    s "[player], heeeeeeelp!!!"
    s "I was messing with the code and accidentally turned myself into Mr. Cow!"
    s "Noooooooo!!!!"
    
    pause 1.5
    
    s "Pffffftt-"
    
    show asset spe1 zorder 2
    
    s "Bwahahahahah- I'm sorry, [player]!"
    s "I'm fine- I just couldn't resist that one!"
    s "I'll go put him away now, I'll be back in a sec!"

    hide asset spe1

    hide mr_cow_desk

    show emptydesk

    pause 2.0
    
    #pause 2.0

    $ fae_events.show_visuals("abhfcqa")

    #show sayori idle at t11 zorder fae_sprites.SAYO_ZORDER
    
    s abhfcqa "There we go, ehehehe~"
    s abhfcoa "Welcome back, [player]!" 
    s abhabsa "I was just kinda starting to miss you so..."
    s abhacea "I dug in the code until I could rescue Mr. Cow!"
    s abbbloa "It was hard work, buuuuut!"
    s abgcdoa "Now I'll always have someone to cuddle with, and it'll never get {i}too{/i} lonely in here!"
    s abhfcaa "Anyways, I'm glad you're here now!" 
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

    #$ fae_events.show_visuals("abbcckc")

    hide black

    #$ fae_events.show_visuals("idle")

    show sayori idle at fae_center zorder fae_sprites.FAE_SAYORI_ZORDER

    show asset knife as knife at fae_center zorder fae_sprites.FAE_SAYORI_ZORDER

    s abbcckc "Hi, [player]! Ready to chop up some bitches?"
    s "Does this look like the face of mercy, [player]?"
    s bbfceea "AHAHAHA...{nw}"
    extend bbfcdia "Just kidding!"
    s abbciia "Sorry about that!"
    
    menu:
        "Where did you even get that???":
            pass
    
    s eahcbsa "Great question!{w=1.0} {nw}"
    extend eahcada "I've been doing some more digging into the code to recover as much stuff as possible!"
    s ebbccqa "I managed to get this knife back today!"
    s fbfckdaj "Not really sure if I'll ever need it for anything, but I figured I might as well have it."
    s bbfcmoaj "But maybe it's better if I put this away now."
    s bbbcciaj "I wouldn't want anything bad to happen, ehehehe~"
    
    hide knife 
    
    s abhaaoa "Hope you're doing good today, [player]~" 
    s abhaiia "Did I make you nervous?"
    s ebhhcoa "Sorry for scaring you, ehehehe~"
    
    return

init 5 python:
    chatReg(
        Chat(
            persistent._event_db,
            label="fae_event_sayori_desk_hide",
            unlocked=True,
            affection_range=(fae_affection.NORMAL, None)
        ),
        chat_group=CHAT_GROUP_EVENT
    )

label fae_event_sayori_desk_hide:
    hide sayori
    window hide
    hide black
    show asset spe2 at s11 zorder fae_sprites.FAE_SAYORI_ZORDER
    show emptydesk at t11 zorder 4
    pause 0.5
    $ style.say_dialogue = style.whisper
    window hide
    s "Ehehehe, [player] will never see this coming, Mr. Cow!"
    s "Oh! I think they're here! Shhh, get down!" 
    s "Ready? 3... 2... 1..."
    hide asset spe2
    hide emptydesk
    $ style.say_dialogue = style.normal
    show sayori at t11 zorder fae_sprites.FAE_SAYORI_ZORDER
    s ebbccoa "Boo!"
    s bbbcaoa "Ehehehe! Did I scare you [player]?"
    s abgbaoa "I wish I could have seen the look on your face, ehehehe~"
    s cbgbaoa "You better always be on your toes around me!"
    s abaacoa "Anyways! Ehehehe~"
    return

init 5 python:
    chatReg(
        Chat(
            persistent._event_db,
            label="fae_event_door_open",
            unlocked=True,
            affection_range=(fae_affection.NORMAL, None)
        ),
        chat_group=CHAT_GROUP_EVENT
    )

label fae_event_door_open:
    scene black
    menu:
        "...":
            pause 2.0
            jump fae_event_door_open
        "Gently open the door":
            $ main_background.form()
            $ fae_sky.reload_sky()
            hide black
            show sayori at t11 zorder fae_sprites.FAE_SAYORI_ZORDER
            s bbegmoajj "Whoops! Sorry about that!"
            s abegaoaj "Welcome back, [player]! {w=0.5}{nw}"
            extend gbaamoj "Sorry if I scared you!"
            s abfccoaj "I've been learning how to use menus, and thought I'd give it a go.{w=0.5}{nw}"
            extend abfcaoaj " But never mind that."
            s abegcoaj "I'm so glad you're back!"
    return
