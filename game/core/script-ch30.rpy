default persistent.first_run = True

default persistent.s_name = "Sayori"

#init -890 python in fae_globals:
#    import datetime
#    import store

#    tt_detected = (
#        store.fae_getLastSeshEnd() - datetime.datetime.now()
#            > datetime.timedelta(hours=30)
#    )

#    if tt_detected:
#        store.persistent._fae_pm_has_went_back_in_time = True

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


label ch30_autoload:

    if fae_is_evening():
        play music s1
    
    

    #the real start of the game

    #config.rollback_enabled = False

    #Start with black screen
    scene black


    python:
        quick_menu = True
        style.say_dialogue = style.normal
        in_sayori_kill = None
        
        if not config.developer:
            config.allow_skipping = False

    #Do all the things for init setup

    

    #FALL THROUGH
    
label ch30_setup:

    #SET UP BG AND STUFF BEHIND A BLACK SCREEN

    show black zorder 99

    #$ fae_notifutilities._setFAEWindow()
    
    #$ fae_updateFilterDict()
    $ Sayori.setOutfit(fae_outfits.get_outfit("uniform"))

    $ main_background.form()

    $ fae_sky.reload_sky()

    $ setupRPC("In the spaceroom")

        #while True:
        #    time.sleep(15)
    
    

    #FALL THROUGH

label ch30_init:

    #$ setupRPC("In the spaceroom")

    $ persistent.autoload = "ch30_autoload"

    python:
        import random

        fae_data.runRuntimeTransfer()

        persistent._fae_version = config.version

        Affection.DayAffectionGainChecker()

        Sayori.setInChat(True)

        if (datetime.datetime.now() - persistent.fae_last_visit_date).total_seconds() / 604800 >= 1:
            persistent._fae_prev_regret = fae_regrets.RegretTypes.LONG_ABSENSE
        
        elif not persistent._fae_prev_regret:
            Affection.getAffectionGain()
            
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
            Sayori.setOutfit(fae_outfits.get_outfit("uniform"))
        
        fae_utilities.log("Outfit Set.")
        
        fae_events.EVENT_RETURN_OUTFIT = fae_outfits.get_outfit(store.persistent.fae_outfit_quit)
        """
        available_holiday_list = fae_events.selectHolidays()

        
        if available_holiday_list:
            fae_events.EVENT_RETURN_OUTFIT = fae_outifts.get_outfit(store.persistent.fae_outfit_quit)
            available_holiday_list.sort(key = lambda holiday: holiday.priority)
            queued_holiday_types = list()

            while len(available_holiday_list) > 0:
                holiday = available_holiday_list.pop()

                if not holiday.holiday_type in queued_holiday_types:
                    queued_holiday_types.append(holiday.holiday_type)
                    atq(holiday.label)
                    if len(available_holiday_list) > 0:
                        queue("event_interlude")

                    else:
                        queue("ch30_loop")
            
            renpy.jump("cnc")

        """

        


        #init_qabs()
        #renpy.save_persistent()
        
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
    #$ begin_song()


    if (
        store.fae_per_checker.is_per_corrupt()
        and not renpy.seen_label("fae_corrupted_persistent")
    ):
        $ ats("fae_corrupted_persistent")
    
    show sayori idle at t11 zorder store.fae_sprites.SAYO_ZORDER
    #show bg spaceroom zorder 1
    hide black with Dissolve(2)
    #show screen hidden1(True)
    show screen hidden1(True)

    #FALL THRouGH

label ch30_loop:

    $ init_qabs()
    
    show sayori idle at fae_center zorder store.fae_sprites.SAYO_ZORDER


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
            
    #$ calendar = Calendar(5, 2, 2014, 2016)
    while persistent._event_list:
        call cnc(True, True) from _call_cnc
    


    show screen hidden1(True)

label loop_wait:
    window hide

    $ renpy.pause(delay=5.0, hard=True)
    jump ch30_loop

label cnc(show_sayori=True, notify=False):

    if show_sayori:
        show sayori idle at fae_center zorder fae_sprites.SAYO_ZORDER

    #show sayori idle at t11 zorder store.fae_sprites.SAYO_ZORDER
    if persistent._event_list:
        $ _chat = persistent._event_list.pop(0)

        if renpy.has_label(_chat):

            #if (persistent.taskbar_alerts
            #    and fae_time.present_sesh_length().seconds() > 60
            #    and not fae_notifications.get_fae_window_active()):
            #        play audio attention
            #        $ fae_notifications.flash_taskbar()
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
        #$ fae_clearNotifs()
        jump confirm_quit
    
    python:
        global LCC
        LCC = datetime.datetime.now()
        Sayori.setInChat(False)
    
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
        
        $ Affection.AffectionLossPercentile(2)
        $ fae_regrets.add_new_regret_awaiting(fae_regrets.RegretTypes.UNEXPECTED_QUIT)
        $ persistent._fae_await_apology_quit = fae_regrets.RegretTypes.UNEXPECTED_QUIT

        hide screen hidden1
        $ renpy.jump("confirm_quit")



label ch30_main:

    $ quick_menu = True

    if not config.developer:
        $ style.say_dialogue = style.default_sayori
    
    $ s_name = persistent._fae_sayori_nickname

    $ persistent.clear[9] = True

    call fae_intro_checks from _call_fae_intro_checks

    jump ch30_setup