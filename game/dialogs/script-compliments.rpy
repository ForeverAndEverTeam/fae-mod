default persistent._flatter_db = dict()

init -1 python in fae_flatter:

    import random
    import store

    FLATTERY_DEFS = dict()

    CUTE = 0
    ADORABLE = 1
    FUNNY = 2
    BEST_GIRL = 3

    prior_flattery = None

    def load_all_flatters():

        return store.Chat.chat_filt(
            FLATTERY_DEFS.values(),
            affection=store.Affection._getAffectionStatus(),
            unlocked=True
        )

label flattery_init:

    python:

        flattery_menu_items = [
            (_flattery.prompt, _flattery.label)
            for _flattery in fae_flattery.load_all_flatters()
        ]
        flattery_menu_items.sort()
    
    call screen neat_menu_scroll(flattery_menu_items, ("Nevermind.", None))

    if _return:
        $ ats(_return)
        jump cnc
    
    return


init 5 python:

    chatReg(
        Chat(
            persistent._flatter_db,
            prompt="I think you're cute",
            label="flattery_cute",
            unlocked=True,
            affection_range=(fae_affection.HAPPY, fae_affection.LOVE)
        ),
        chat_group=CHAT_GROUP_FLATTER
    )

label flattery_cute:

    $ Affection.getAffectionGain(bypass=get_chat("flattery_cute").seen_no == 0)

    return


    

