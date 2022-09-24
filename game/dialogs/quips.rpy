init 15 python in fae_quips:

    import store

    persistent = renpy.game.persistent
    layout = store.layout

    talk_menu_quips = dict()

    def _init_talk_quips():

        global talk_menu_quips
        def save_quips(_aff, quiplist):
            fae_ql = store.FAEQuipList(allow_label=False)

            for _quip in quiplist:
                fae_ql.addLineQuip(_quip)
            talk_menu_quips[_aff] = fae_ql
        

        quips = [
            _("What would you like to talk about?"),
            _("What are you thinking of?"),
            _("Is there something you'd like to talk about?"),
            _("Something on your mind?"),
            _("Yes, [player]?"),
        ]
        save_quips(NORMAL, quips)

        ## HAPPY quips
        quips = [
            _("What would you like to talk about?"),
            _("What are you thinking of?"),
            _("Is there something you'd like to talk about?"),
            _("Something on your mind?"),
            _("Up to chat, [player]?"),
            _("Yes, [player]?"),
            _("What's on your mind, [player]?"),
            _("What's up, [player]?"),
            _("Ask away, [player]."),
            _("Don't be shy, [player]."),
        ]
        save_quips(HAPPY, quips)

        ## AFFECTIONATE quips
        quips = [
            _("What would you like to talk about?"),
            _("What would you like to talk about, [fae_get_player_nickname()]?"),
            _("What are you thinking of?"),
            _("Is there something you'd like to talk about, [fae_get_player_nickname()]?"),
            _("Something on your mind?"),
            _("Something on your mind, [fae_get_player_nickname()]?"),
            _("Up to chat, [fae_get_player_nickname()]?"),
            _("Yes, [fae_get_player_nickname()]?"),
            _("What's on your mind, [fae_get_player_nickname()]?"),
            _("What's up, [fae_get_player_nickname()]?"),
            _("Ask away, [fae_get_player_nickname()]."),
            _("Don't be shy, [fae_get_player_nickname()]~"),
            _("I'm all ears, [fae_get_player_nickname()]~"),
            _("Of course we can talk, [fae_get_player_nickname()]."),
        ]
        save_quips(AFFECTIONATE, quips)

        ## ENAMORED quips
        quips = [
            _("What would you like to talk about? <3"),
            _("What would you like to talk about, [fae_get_player_nickname()]? <3"),
            _("What are you thinking of?"),
            _("Is there something you'd like to talk about, [fae_get_player_nickname()]?"),
            _("Something on your mind?"),
            _("Something on your mind, [fae_get_player_nickname()]?"),
            _("Up to chat, I see~"),
            _("Yes, [fae_get_player_nickname()]?"),
            _("What's on your mind, [fae_get_player_nickname()]?"),
            _("What's up, [player]?"),
            _("Ask away, [fae_get_player_nickname()]~"),
            _("I'm all ears, [fae_get_player_nickname()]~"),
            _("Of course we can talk, [fae_get_player_nickname()]~"),
            _("Take all the time you need, [player]."),
            _("We can talk about whatever you'd like, [fae_get_player_nickname()]."),
        ]
        save_quips(ENAMORED, quips)

        ## LOVE quips
        quips = [
            _("What would you like to talk about? <3"),
            _("What would you like to talk about, [fae_get_player_nickname()]? <3"),
            _("What are you thinking of?"),
            _("Something on your mind?"),
            _("Something on your mind, [fae_get_player_nickname()]?"),
            _("Up to chat, I see~"),
            _("Yes, [fae_get_player_nickname()]?"),
            _("What's on your mind, [fae_get_player_nickname()]?"),
            _("<3"),
            _("What's up, [fae_get_player_nickname()]?"),
            _("Ask away, [fae_get_player_nickname()]~"),
            _("I'm all ears, [fae_get_player_nickname()]~"),
            _("We can talk about whatever you'd like, [fae_get_player_nickname()]."),
            _("Of course we can talk, [fae_get_player_nickname()]~"),
            _("Take all the time you need, [fae_get_player_nickname()]~"),
            _("I'm all yours, [fae_get_player_nickname()]~"),
            _("Oh? Something...{w=0.3}{i}important{/i} on your mind, [fae_get_player_nickname()]?~"),
        ]
        save_quips(LOVE, quips)


    def _dict_quip(_quips):

        quipper = _quips.get(store.Affection._getAffectionStatus(), None)
        if quipper is not None:
            return quipper.quips()

        return ""

    def talk_quip():

        quip = _dict_quip(talk_menu_quips)
        if len(quip) > 0:
            return quip
        return _("What would you like to talk about?")


