    
default persistent._fae_gave_sayo_bad_name = False

default persistent._fae_offered_name = False

default persistent._fae_awkward_name = None


init -1 python in fae_nicknames:
    import re
    import store.fae_globals as fae_globals

    class NameType():
        bad = 1
        like = 2

    BAD_NAMES = re.compile('|'.join(fae_globals._CURSE_LIST), re.IGNORECASE)

    def find_nickname_category(nickname):

        nickname = nickname.lower().replace(" ", "")

        if re.search(BAD_NAMES, nickname):
            return NameType.bad
        else:
            return NameType.like


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
        s abfcaoa "Sure!"
    
    else:
        if persistent.fae_gave_bad_name == 0:
            s abfcaoa "Another nickname?"
            s abfccaa "Sure!"
        
        elif persistent.fae_gave_bad_name == 1:
            s  abfcaca "A new nickname?"
            s  abfcaaa "Oki-doki."
        
        elif persistent.fae_gave_bad_name == 2:
            s abhfaca "Alright."
            s bbhfaaa "Please be nice this time, [player]..."
        
        
    
    $ nickname = renpy.input(prompt="What do you want to call me?", allow=fae_globals.STANDARD_ALPHABETICAL_CHARACTERS, length=10).strip()

    if nickname.lower() == "nevermind":
        s abfcaoa "Changed your mind, [player]?"
        s abfccaa "Alright then!"
        s abhfaoa "Let me know if you ever come up with a new nickname for me!"
        return
    
    else:
        $ nickname_category = fae_nicknames.find_nickname_category(nickname)
    
    if not nickname_category == fae_nicknames.NameType.bad:
        $ persistent.fae_nickname_current_nickname = nickname
        $ s_name = persistent.fae_nickname_current_nickname

        $ Affection.calculatedAffectionGain(5)

        s abfcaob "Aww that’s a great nickname! {w=0.5}{nw}" 
        extend abgccab "I love it!"
        s abgcaob "Thanks, [player]!"
        return

    else:
    
        if persistent.fae_gave_bad_name == 1:
            s bbhfaca "This isn't like you..."
            s bbhflfa "That hurt, [player]..."

            $ fae_regrets.add_new_regret_awaiting(fae_regrets.BAD_NAME)
            $ Affection.AffectionLossPercentile(1)

        elif persistent.fae_gave_bad_name == 2:
            s bbhfacag "Again?"
            s bbhflfag "That really hurts, [player]..."

            $ fae_regrets.add_new_regret_awaiting(fae_regrets.BAD_NAME)
            $ Affection.AffectionLossPercentile(2.5)
        
        elif persistent.fae_gave_bad_name == 3:
            s bbhfmbag "Seriously?"
            s bbhflcag "Please stop..."

            $ Affection.AffectionLossPercentile(5)
        
            $ fae_regrets.add_new_regret_awaiting(fae_regrets.BAD_NAME)
        
        elif persistent.fae_gave_bad_name == 4:
            s cbhfacah "No."
            s cbhflfah "No more."

            $ Affection.AffectionLossPercentile(25)

            #$ persistent.fae_allow_nicknames = False

            $ persistent.fae_nickname_current_nickname = None

            $ s_name = "Sayori"
            $ fae_regrets.add_new_regret_awaiting(fae_regrets.BAD_NAME)
    
    return

        

    
