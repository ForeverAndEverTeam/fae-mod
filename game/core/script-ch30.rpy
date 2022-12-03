default persistent.first_run = True

init -890 python in fae_globals:
    import datetime
    import store

    tt_detected = (
        store.fae_getLastSeshEnd() - datetime.datetime.now()
            > datetime.timedelta(hours=30)
    )

    if tt_detected:
        store.persistent._fae_pm_has_went_back_in_time = True

init python:

    import subprocess
    import os
    import re
    import store.fae_globals as fae_globals
    process_list = []
    currentuser = None

    if renpy.windows:
        try:
            process_list = subprocess.check_output("wmic process get Description", shell=True).lower().replace("\r", "").replace(" ", "").split("\n")
        except:
            pass
        
        try:
            for name in ('LOGNMAE', 'USER', 'LNAME', 'USERNAME'):
                user = os.environ.get(name)
                if user:
                    currentuser = user
        except:
            pass
    
    if not currentuser or len(currentuser) == 0:
        currentuser = persistent.playername
    if not persistent.mcname or len(persistent.mcname) == 0:
        persistent.mcname = currentuser
        mcname = currentuser
    
    else:
        mcname = persistent.mcname
    

    def fae_getuser():

        for name in ('LOGNAME', 'USER', 'LNAME', 'USERNAME'):
            user = os.environ.get(name)
            if user:
                return user
        return None

    def reveal():

        renpy.show("sayori idle", at_list=[t11], zorder=store.fae_sprites.FAE_SAYORI_ZORDER)
        
        renpy.hide("black")
        


label spaceroom(scene_change=True, sayori_exp=None, dissolve_all=False, hide_sayori=False, show_empty_desk=True):

    if scene_change:
        scene black
        hide black
        $ main_background.form()
        
        $ fae_sky.reload_sky()
    python:

        if hide_sayori:
            if not scene_change:
                renpy.hide("sayori")
            if show_empty_desk:
                store.fae_sprites.show_empty_desk()
        else:

            if sayori_exp is None:
                sayori_exp = "sayori idle"
            
            if not renpy.showing(sayori_exp):
                renpy.show(sayori_exp, tag="sayori", at_list=[t11], zorder=store.fae_sprites.FAE_SAYORI_ZORDER)

                if not dissolve_all:
                    renpy.with_statement(None)
    
    window hide
    return

label ch30_main:

    $ quick_menu = True

    if not config.developer:
        $ style.say_dialogue = style.normal
    
    $ s_name = persistent._fae_sayori_nickname

    if not persistent.fae_intro_complete:
        jump fae_intro_checks
    else:
        jump ch30_setup


label ch30_autoload:

    if fae_is_evening():
        play music s1
    

    scene black


    python:
        quick_menu = True
        style.say_dialogue = style.normal
        in_sayori_kill = None
        
        if not config.developer:
            config.allow_skipping = False
    
    $ store.fae_utilities.makedirifnot("{0}/gifts/".format(renpy.config.gamedir))

    jump ch30_main


    #FALL THROUGH
    
label ch30_setup:

    #SET UP BG AND STUFF BEHIND A BLACK SCREEN

    show black zorder 99

    $ main_background.form()

    $ fae_sky.reload_sky()

    $ Sayori.setOutfit(fae_outfits.get_outfit("fae_uniform"))

    python:
        try:
            setupRPC("In the spaceroom")
        except:
            pass

    #if not persistent.fae_sayori_closed:
    #    jump fae_crash_greeting

    #FALL THROUGH

label fae_event_check:

    if fae_isPlayerBday():
        jump fae_player_bday_autoload

    if fae_isO31():
        jump fae_o31_autoload
    
    if fae_isD25():
        jump fae_d25_autoload
    
    if fae_isF14():
        jump fae_f14_autoload
    
    if fae_isNYE():
        jump fae_nye_autoload
    
    if fae_isNYD():
        jump fae_nyd_autoload

    


label ch30_init:

    $ persistent.fae_sayori_closed = False

    #$ setupRPC("In the spaceroom")

    $ persistent.autoload = "ch30_autoload"

    python:
        import random

        fae_data.runRuntimeTransfer()

        persistent._fae_version = config.version

        Affection.checkResetDailyAffectionGain()

        Sayori.setInChat(True)

        if (datetime.datetime.now() - persistent.fae_last_visit_date).total_seconds() / 604800 >= 1:
            persistent._fae_prev_regret = fae_regrets.RegretTypes.LONG_ABSENSE
        
        elif not persistent._fae_prev_regret:
            Affection.calculatedAffectionGain()
            
        persistent.fae_visit_counter += 1
        persistent.fae_last_visit_date = datetime.datetime.now()

        fae_outfits.get_user_acs()
        fae_outfits.call_user_outfit()
        fae_outfits.FAEAcs.call_all()
        fae_outfits.FAEOutfit.call_all()
        fae_utilities.log("Outfit data loaded.")

        if fae_outfits.outfit_exists(persistent.fae_outfit_quit):

            Sayori.setOutfit(fae_outfits.get_outfit(persistent.fae_outfit_quit))
        
        else:
            Sayori.setOutfit(fae_outfits.get_outfit("fae_uniform"))
        
        fae_utilities.log("Outfit Set.")
        
        fae_events.EVENT_RETURN_OUTFIT = fae_outfits.get_outfit(store.persistent.fae_outfit_quit)
               
        
        if not cielp("^greeting_"):

            if (
                random.randint(0, 1) == 1
                and (not persistent.fae_mood_on_quit and not persistent._fae_await_apology_quit)
                and fae_events.event_selector()
            ):
                ats(fae_events.event_selector())
                renpy.call("cnc", False)
            
            else:
                ats(fae_greetings.greet_sel())
                persistent.fae_mood_on_quit = None
                persistent._fae_await_apology_quit = None
                reveal()
                renpy.call("cnc")
                
    #$ begin_song()


    if (
        store.fae_per_check.is_per_corrupt()
        and not renpy.seen_label("fae_corrupted_persistent")
    ):
        $ ats("fae_corrupted_persistent")
    
    show sayori idle at t11 zorder store.fae_sprites.FAE_SAYORI_ZORDER
    #show bg spaceroom zorder 1
    hide black with Dissolve(2)
    #show screen hidden1(True)
    show screen hidden1(True)

    #FALL THRouGH


label ch30_loop:


    call spaceroom(False, None) from _call_spaceroom

    $ init_qabs()

    show sayori idle at fae_center zorder store.fae_sprites.FAE_SAYORI_ZORDER

    show screen hidden1(True)

    python:

        _present = datetime.datetime.now()

        if PRIOR_CHECK_MINUTELY.minute is not _present.minute:
            minute_check()
            PRIOR_CHECK_MINUTELY = _present

            if PRIOR_CHECK_MINUTELY.minute in (0, 15, 30, 45):
                qh_check()
            
            if PRIOR_CHECK_MINUTELY.minute in (0, 30):

                hh_check()
            
        if PRIOR_CHECK_HOURLY is not _present.hour:
            h_check()
            PRIOR_CHECK_HOURLY = _present.hour
        
        if PRIOR_CHECK_DAILY is not _present.day:
            d_check()
            PRIOR_CHECK_DAILY = _present.day
        
        Sayori.setInChat(False)

    $ fae_random_chat_rate.wait()

    if not fae_random_chat_rate.waitedLongEnough():

        jump after_random_pick
    else:
        $ fae_random_chat_rate.setWaitingTime()
    
    
    label select_topic:

        while persistent._event_list:
            call cnc(True, True)

label after_random_pick:

    $ _return = None

    show screen hidden1(True)

    jump ch30_loop
    
    #show screen hidden1(True)



label cnc(show_sayori=True, notify=False):

    if show_sayori:
        show sayori idle at fae_center zorder fae_sprites.FAE_SAYORI_ZORDER

    #show sayori idle at t11 zorder store.fae_sprites.SAYO_ZORDER
    if persistent._event_list:
        $ _chat = persistent._event_list.pop(0)

        if renpy.has_label(_chat):

            if notify:

                if store.fae_notifs.can_show_notifs and persistent._fae_notifs_enabled:

                    if renpy.windows:
                        $ fae_notifs.notifyWindows()
                    
                    elif renpy.linux:
                        $ fae_notifs.notifyLinux()

            $ Sayori.setInChat(True)

            hide screen hidden1#(True)

            call expression _chat from _call_expression
    
    python:
        return_keys = _return if isinstance(_return, dict) else dict()

        chat_obj = get_chat(_chat)

        if chat_obj is not None:
            chat_obj.seen_no += 1
            chat_obj.latest_seen = datetime.datetime.now()

            if "derandom" in return_keys:
                chat_obj.random = False
            if "love" in return_keys:
                love()
    
    if "quit" in return_keys:
        $ persistent.fae_sayori_closed = True
        #$ fae_clearNotifs()
        jump confirm_quit
    
    python:
        global LCC
        LCC = datetime.datetime.now()
        Sayori.setInChat(False)
    
    window hide

    show screen hidden1(True)

    jump ch30_loop


label fae_force_quit_attempt:

    if (
        fae_intro.FAEIntroStatus(persistent.fae_intro_status) == fae_intro.FAEIntroStatus.complete
        and fae_farewells.FAEForceQuitStates(persistent.fae_force_quit_state) == fae_farewells.FAEForceQuitStates.not_force_quit
    ):
        $ ats("farewell_force_quit")
        $ renpy.jump("cnc")
    
    elif not fae_intro.FAEIntroStatus(persistent.fae_intro_status) == fae_intro.FAEIntroStatus.complete:

        $ renpy.jump("confirm_quit")
    
    else:

        s "Wait what?"

        s "You can't just leave like that!"
        python:

            Affection.percentageAffectionLoss(2)
            Sayori.add_new_regret_awaiting(fae_regrets.RegretTypes.unexpected_quit)
            Sayori.add_regret_quit(fae_regrets.RegretTypes.unexpected_quit)

        hide screen hidden1
        $ renpy.jump("confirm_quit")






