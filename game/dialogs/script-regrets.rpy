default persistent._regret_db = dict()

default persistent._fae_player_apology_type_on_quit = None

default persistent._fae_player_awaiting_apologies = list()


init -1 python in fae_regrets:

    from Enum import Enum
    import store

    REGRET_DEFS = dict()

    class RegretTypes(Enum):

        bad_name = 1
        cheat_game = 2
        generic = 3
        long_absence = 4
        offense = 5
        unexpected_quit = 6

        def __str__(self):
            return self.name

        def __int__(self):
            return self.value
    
    def get_all_regrets():

        return_regrets = [
            store.get_chat("regret_generic")
        ]

        for regret_type in store.persistent._fae_player_awaiting_apologies:
            return_regrets.append(store.get_chat(str("regret_{0}".format(RegretTypes(regret_type)))))

        return return_regrets

label regret_init:

    python:
        regrets_menu_items = [
            (_regrets.prompt, _regrets.label)
            for _regrets in fae_regrets.get_all_regrets()
        ]

    call screen neat_menu_scroll(regrets_menu_items, ("Nevermind", None))

    if _return:
        $ ats(_return)
        jump cnc

    return

#Apology for cheating at the game
init 5 python:

    chatReg(
        Chat(
            persistent._regret_db,
            label="regret_cheat_game",
            unlocked=True,
            prompt="For cheating at our game."
        ),
        chat_group=CHAT_GROUP_REGRET
    )

label regret_cheat_game:
    s "Thank you for apologising."
    s "Cheating is bad, you know!"
    s "You don't want Nathan to hunt you down."
    s "But thank you for apologizing."
    s "Don't do it again!"
    s "I forgive you."

    $ persistent._fae_player_awaiting_apologies.remove(fae_regrets.RegretTypes.cheat_game)
    return


init 5 python:

    chatReg(
        Chat(
            persistent._regret_db,
            prompt="For leaving without saying goodbye.",
            label="regret_unexpected_quit",
            unlocked=True
        ),
        chat_group=CHAT_GROUP_REGRET
    )

label regret_unexpected_quit:
    s "Thank you."
    
    $ persistent._fae_player_awaiting_apologies.remove(fae_regrets.RegretTypes.unexpected_quit)

    return


init 5 python:

    chatReg(
        Chat(
            persistent._regret_db,
            prompt="For something",
            label="regret_generic",
            unlocked=True
        ),
        chat_group=CHAT_GROUP_REGRET
    )


label regret_generic:

    s bbaaaaa "It’s okay, [player]."
    s abgbaoa "Thank you for apologising, apology accepted!"

    return

init 5 python:

    chatReg(
        Chat(
            persistent._regret_db,
            label="regret_bad_name",
            unlocked=True,
            prompt="For calling you a bad name."
        ),
        chat_group=CHAT_GROUP_REGRET
    )


label regret_bad_name:
    s bbaaaaa "It’s okay, [player]."
    s bbfdaca "Were you just kidding?"
    s bbfdaaa "I hope you weren’t being serious."
    s abhfaoa "Thank you for apologising though, apology accepted!"
    $ persistent._fae_player_awaiting_apologies.remove(fae_regrets.RegretTypes.bad_name)
    return


init 5 python:

    chatReg(
        Chat(
            persistent._regret_db,
            label="regret_long_absence",
            unlocked=True,
            prompt="For being away for so long."
        ),
        chat_group=CHAT_GROUP_REGRET
    )


label regret_long_absence:

    s bbaaaaa "That’s alright, [player]."
    s abbbaoa "I understand, we all get a little busy sometimes."
    s abgbcaa "I’m just glad you’re back safe and sound!"
    s abhfaoa "So, where were we?"
    $ persistent._fae_player_awaiting_apologies.remove(fae_regrets.RegretTypes.long_absence)

    return

init 5 python:

    chatReg(
        Chat(
            persistent._regret_db,
            label="regret_offense",
            unlocked=True,
            prompt="For being offensive."
        ),
        chat_group=CHAT_GROUP_REGRET
    )

label regret_offense:
    s bbaalra "Thank you for apologising, [player]."
    s bbaamca "What you said really hurt but…"
    s bbaaaaa "I understand that sometimes we forget to think before we speak, and say the wrong things."
    s abhfaoa "I’m just glad you took responsibility, let’s move on shall we."

    $ persistent._fae_player_awaiting_apologies.remove(fae_regrets.RegretTypes.offense)

    return

