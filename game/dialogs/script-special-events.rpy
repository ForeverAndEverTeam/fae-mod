
default persistent._fae_player_bday = None

default peristent._fae_player_confirmed_bday = False

#init 5 python:
#    chatReg(
#        Chat(
#            persistent._chat_db,
#            label="s_player_birthday",
#            unlocked=True,
#            prompt="My birthday",
#            category=["Holidays", "You"],
#            random=True
#        ),
#        chat_group=CHAT_GROUP_NORMAL
#    )

label s_player_birthday:
    s abhfaoa "Hey [player], I was wondering."
    s abgbaaa "You know I’m not too sure when my birthday is, {w=0.5}{nw}"
    extend abgbcoa "but I’m sure you know when yours is! Ehehehe~"
    s abhfaaa "When’s your birthday, [player]?"
    


label birthdate_set:
    
    $ persistent._fae_player_confirmed_bday = True

    $ get_chat("s_player_birthday").lock()
    return


