
default persistent._fae_player_bday = None

default peristent._fae_player_confirmed_bday = False

init 5 python:
    chatReg(
        Chat(
            persistent._chat_db,
            label="s_player_birthday",
            unlocked=True,
            prompt="My birthday",
            category=["Holidays", "You"],
            random=True
        ),
        chat_group=CHAT_GROUP_NORMAL
    )

label s_player_birthday:
    s abhfaoa "Hey [player], I was wondering."
    s abgbaaa "You know I’m not too sure when my birthday is, {w=0.5}{nw}"
    extend abgbcoa "but I’m sure you know when yours is! Ehehehe~"
    s abhfaaa "When’s your birthday, [player]?"
    menu:
        "Sure!":
            s "Alright!"
            jump fae_bday_player_select_select


label fae_bday_player_select_select:
    call fae_start_calendar_select_date from _call_fae_start_calendar_select_date

    $ selected_date_t = _return

    if not selected_date_t:
        s "Try again!"
        jump fae_bday_player_select_select
    
    $ selected_date = selected_date_t.date()
    $ _today = datetime.date.today()

    if selected_date > _today:
        s "You couldn't have been born in the future!"
        jump fae_bday_player_select_select

    elif selected_date == _today:
        s "You couldn't have been born today!"

        jump fae_bday_player_select_select
    
    elif _today.year - selected_date.year < 5:
        s "No way!"

        jump fae_bday_player_select_select
    
    if _today.year - selected_date.year < 13:
        s "No way you're that young."
    
    else:
        s "Alright!"

    s "Just to double check..."
    $ new_bday_str, diff = store.fae_calendar.genFormalDispDate(selected_date)

    s "Your birthdate is [new_bday_str]?{nw}"
    $ _history_list.pop()
    menu:
        s "Your birthdate is [new_bday_str]?{fast}"

        "Yes":
            s "Are you sure it's [new_bday_str]? I'm never going to forget this date.{nw}"
            $ _history_list.pop()
            # one more confirmation
            menu:
                s "Are you sure it's [new_bday_str]? I'm never going to forget this date.{fast}"
                "Yes, I'm sure!":
                    s abbbaoa "Alright, I’ll mark [new_bday_str] on the calendar!"
                    s abgbcaa "I’ll be sure to throw an amazing party for you as soon as I figure out how to get some decorations in here! Ehehehe~"

                "Actually...":
                    s "Aha! I figured you weren't so sure."
                    s "Try again~"
                    jump fae_bday_player_select_select

        "No.":
            s "Oh, that's wrong?"
            s "Then try again!"
            jump fae_bday_player_select_select
    
    if persistent._fae_player_bday is not None:
        python:
            store.fae_calendar.removeRepeatable_d(
                "player-bday",
                persistent._fae_player_bday
            )
            store.fae_calendar.addRepeatable_d(
                "player-bday",
                "Your Birthday",
                selected_date,
                range(selected_date.year,store.FAECALENDAR.MAX_VIEWABLE_YEAR)
            )

    else:
        python:
            store.fae_calendar.addRepeatable_d(
                "player-bday",
                "Your Birthday",
                selected_date,
                range(selected_date.year,FAECALENDAR.MAX_VIEWABLE_YEAR)
            )
    
    $ persistent._fae_player_bday = selected_date
    $ renpy.save_persistent()
    jump birthdate_set


label birthdate_set:
    
    $ persistent._fae_player_confirmed_bday = True

    $ get_chat("s_player_birthday").lock()
    return


