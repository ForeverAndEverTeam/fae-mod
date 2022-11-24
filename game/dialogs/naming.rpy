init 5 python:
    """
    
    chatReg(
        Chat(
            label="sayori_nickname",
            prompt="Nickname Sayori",
            category=["sayori"],
            random=True,
            unlocked=True,
            affection_range=(fae_affection.AFFECTIONATE, None)
        ),
        chat_group=CHAT_GROUP_NORMAL
    )

default persistent._fae_gave_sayo_bad_name = False

default persistent._fae_offered_name = False

default persistent._fae_awkward_name = None

label sayori_nickname:

    python:

        good_nickname_comp = re.compile('|'.join(fae_good_sayori_name_list), re.IGNORECASE)

    if not persistent._fae_offered_name:
        s "You know..."
        s "Why don't you give me a nickname?"
        s "What do you think?"

    else:
        jump fae_nickname_yes

    $ _history_list.pop()

    menu:
        s "What do you think?{fast}"
        "Yes":
            label fae_nickname_yes:
                pass
            
            show sayori abaabaa at t11 zorder sayo_zorder

            $ done = False

            while not done:
                python:
                    inputname = fae_input(
                        _("So what do you want to call me?"),
                        allow=name_characters_only,
                        length=10,
                        screen_kwargs={"use_return_button": True, "return_button_value": "nevermind"}
                    ).strip(' \t\n\r')

                    lowername = inputname.lower()
                
                if lowername == "nevermind":
                    s "Alright then!"

                    $ done = True
                
                elif not lowername:
                    s "You have to give me a nickname, silly."
                
                elif lowername != "sayori" and lowername == player.lower():
                    s "That's your name!"
                
                elif lowername == s_name.lower():
                    s "Choose a new name!"
                
                elif persistent._fae_awkward_name and lowername == persistent._fae_awkward_name.lower():

                    jump .neutral_accept
                
                elif fae_awk_name_comp.search(inputname):
                    s "I don't hate it..."
                    s "I'm not comfortable calling you that."
                
                else:
                    if not fae_bad_name_comp.search(inputname) and lowername not in ["yuri", "monika", "natsuki"]:
                        if lowername == "sayori":
                            $ inputname = inputname.capitalize()
                            s "Sticking to the classics, I see~"
                        elif good_sayori_nickname_comp.search(inputname):
                            s "I love it."
                        
                        else:
                            label .neutral_accept:
                                pass
                            
                            s "[inputname]... very nice."
                        
                        $ persistent._fae_sayori_nickname = inputname

                        $ s_name = inputname

                        s "Oki-doki"
                        if s_name == "Sayori":
                            s "I'll go back to my name then."
                            
                        else:
                            s "From now on, you can call me Al{nw}"
                            s "From now on, you can call me{fast} '[s_name].'"
                        
                        $ done = True
                    
                    else:

                        $ getAffectionLoss()

                        if lowername in ["yuri", "monika", "natsuki"]:
                            s "...!"
                            s "Why?!"

                            if seen_no("regret_bad_nickname") == 2:
                                call fae_nickname_lock
                            
                            pause 5.0
                        
                        else:
                            s "That's not nice!"

                            if seen_no("regret_bad_nickname") == 2:
                                call fae_nickname_lock
                            else:
                                s "Please don't do that."
                        
                        $ persistent._fae_gave_sayo_bad_name = True

                        if s_name.lower() != "sayori":
                            $ s_name = "Sayori"
                            $ persistent._fae_sayori_nickname = "Sayori"                        
    

init 5 python:

    chatReg(
        Chat(
            persistent._chat_db,
            label="sayori_give_nickname",
            unlocked=True,
            prompt="Nicknames",
            conditional="persistent.fae_allow_nicknames",
            category=["Sayori"],
            random=False,
            affection_range=(fae_affection.ENAMOURED, None)
        ),
        chat_group=CHAT_GROUP_NORMAL
    )

label sayori_give_nickname:

    if persistent.fae_allow_nicknames and persistent.fae_current_nickname == "Sayori":
        s "Sure!"
    
    else:
        if persistent.fae_gave_bad_name == 0:
            s "Another nickname?"
            s "Sure!"
        
        elif persistent.fae_gave_bad_name == 1:
            s "A new nickname?"
            s "Oki-doki."
        
        elif persistent.fae_gave_bad_name == 2:
            s "Alright."
            s "Please be respectful."
        
        elif persistent.fae_gave_bad_name == 3:
            s "Last chance."
    
    $ nickname = renpy.input(prompt="What do you want to call me?", allow=fae_globals.STANDARD_ALPHABETICAL_CHARACTERS, length=10).strip()

    if nickname.lower() == "nevermind":
        s "Change your mind?"
        s "Okay then!"
        return
    
    else:
        $ nickname_category = fae_nicknames.find_nickname_category(nickname)
    
    if nickname_category == fae_nicknames.CATEGORY_INVALID:
        s "That's not a name."
        return
    
    elif nickname_category == fae_nicknames.CATEGORY_LOVE:

        $ persistent.fae_nickname_current_nickname = nickname
        $ s_name = persistent.fae_nickname_current_nickname

        s "Oh."
        s "I love it."
        return
    
    elif nickname_category == fae_nicknames.CATEGORY_DISLIKED:
        s "I don't think so."
        return
    
    elif nickname_category == fae_nicknames.CATEGORY_HATED:
        s "WHAT?!"
        s "NO."

        $ persistent.fae_gave_bad_name += 1
    
    elif nickname_category == fae_nicknames.CATEGORY_PROFANE:
        s "EXCUSE ME?!"

        $ persistent.fae_gave_bad_name += 1
    
    elif nickname_category == fae_nicknames.CATEGORY_AMUSING:
        s "Ehehehe~"
        s "You certainly have a sense of humour."
        s "[nickname] it is."

        $ persistent.fae_nickname_current_nickname = nickname

        $ s_name = persistent.fae_nickname_current_nickname
        return
    
    else:
        $ neutral_allowed = False

        if nickname.lower() == "sayori":
            s "That's my name now!"

            $ neutral_allowed = True
       
        elif nickname.lower() == persistent.playername.lower():
            s "That's your name."

        else:
            s "Hmmm..."
            s "Sure!"

            $ neutral_allowed = True
        
        if (neutral_allowed):
            $ persistent.fae_nickname_current_nickname = nickname
            $ s_name = persistent.fae_nickname_current_nickname
        
        return
    
    if persistent.fae_gave_bad_name == 1:
        s "This isn't like you..."
        s "That hurt."

        $ fae_regrets.add_new_regret_awaiting(fae_regrets.BAD_NAME)
        $ Affection.AffectionLossPercentile(1)

    elif persistent.fae_gave_bad_name == 2:
        s "Again?"
        s "That hurts."

        $ fae_regrets.add_new_regret_awaiting(fae_regrets.BAD_NAME)
        $ Affection.AffectionLossPercentile(2.5)
    
    elif persistent.fae_gave_bad_name == 3:
        s "Seriously?"
        s "No more warnings."

        $ Affection.AffectionLossPercentile(5)
    
        $ fae_regrets.add_new_regret_awaiting(fae_regrets.BAD_NAME)
    
    elif persistent.fae_gave_bad_name == 4:
        s "No."
        s "No more."

        $ Affection.AffectionLossPercentile(25)

        $ persistent.fae_allow_nicknames = False

        $ persistent.fae_nickname_current_nickname = None

        $ s_name = "Sayori"
        $ fae_regrets.add_new_regret_awaiting(fae_regrets.BAD_NAME)
    
    return
    """
