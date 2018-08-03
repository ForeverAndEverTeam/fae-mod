label s_farewell:
    show sayori 6aaaa at ss1 zorder 2
    hide screen talk_ui
    hide screen feat_ui
    
    $justIsSitting = False
    
    $ config.allow_skipping = True
    $ config.skip_indicator = True
    
    call expression "s_farewell_" + str(renpy.random.randint(1, 5))
    
    $persistent.lastLaunch = get_now()
    $renpy.quit()

#Farewells
label s_farewell_1: #The really first farewell of this mod
    show sayori 6acab at ss1 zorder 2
    s "Are you qiutting the game?" 
    s 6abab "Then see you later, [player]!"
    return

label s_farewell_2:
    show sayori 7aaaa at ss1 zorder 2
    s "Goodbye, [player]!"
    s "Come back when you feel alone."
    s 7aaca "I always can spend time with you."
    return

label s_farewell_3:
    show sayori 7aaaa at ss1 zorder 2
    s "Bye, honey!"
    s 7aaab "Don't forget to come back."
    return

label s_farewell_4:
    show sayori 7aaaa at ss1 zorder 2
    s "Bye-bye!"
    s "I wish you good luck and mood."
    s 7aaca "You can take some of mine now, if you need."
    return

label s_farewell_5:
    if get_time_of_day() == 0:
        s 7aaaa "Good night, [player]!"
        s 7acaa "You should sleep enough to be in a good temper and not tired."
    elif get_time_of_day() < 3:
        s 7aaaa "Have a good day, [player]!"
        s 7aaaa "I wish you successfully do everything you planned for today."
    else:
        s 7aaaa "See you later, [player]!"
        if get_time_of_day(launch_dt.hour) == 3:
            s "I'm glad you have spent at least some of this evening with me."
        else:
            s "I'm glad you have spent this day with me."
    return