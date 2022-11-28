default persistent._regret_db = dict()

default persistent._fae_await_regret_quit = None

default persistent._fae_await_regret = list()

init -1 python in fae_regrets:

    import store
    from Enum import Enum

    REGRET_DEFS = dict()

    class RegretTypes(Enum):

        BAD_NAME = 0
        DEFAULT = 1
        LONG_ABSENSE = 2
        OFFENSE = 3
        UNEXPECTED_QUIT = 4
        CHEATING = 5

        def __str__(self):
            return self.name

        def __int__(self):

            return self.value

    def load_all_regrets():

        return_regrets = [
            store.get_chat("regret_generic")
        ]
        for regret_type in store.persistent._fae_await_regret:
            return_regrets.append(store.get_chat(str("regret_{0}".format(RegretTypes(regret_type)))))
        
        return return_regrets

label regret_init:
    python:
        regrets_menu_items = [
            (_regrets.prompt, _regrets.label)
            for _regrets in fae_regrets.load_all_regrets()
        ]
        regrets_menu_items.sort()
    
    call screen neat_menu_scroll(regrets_menu_items, ("Nevermind.", None))

    if _return:

        $ ats(_return)
        jump cnc
    
    return

#Apology for cheating at the game
init 5 python:

    chatReg(
        Chat(
            persistent._regret_db,
            label="regret_cheating",
            unlocked=True,
            prompt="For cheating at our game.",
            conditional="fae_regrets.load_all_regrets(fae_regrets.CHEATING)"
        ),
        chat_group=CHAT_GROUP_REGRET
    )

label regret_cheating:
    s "Thank you for apologising."
    s "Cheating is bad, you know!"
    s "You don't want Nathan to hunt you down."
    s "But thank you for apologizing."
    s "Don't do it again!"
    s "I forgive you."

    $ persistent._fae_await_regret.remove(fae_regrets.CHEATING)
    return


init 5 python:

    chatReg(
        Chat(
            persistent._regret_db,
            prompt="For leaving without saying goodbye.",
            label="regret_sudden_quit",
            unlocked=True,
            conditional="fae_regrets.load_all_regrets(fae_regrets.UNEXPECTED_QUIT)"
        ),
        chat_group=CHAT_GROUP_REGRET
    )

label regret_sudden_quit:
    s "Thank you."
    
    $ persistent._fae_await_regret.remove(fae_regrets.UNEXPECTED_QUIT)

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
            prompt="For calling you a bad name.",
            conditional="fae_regrets.load_all_regrets(fae_regrets.BAD_NAME)"
        ),
        chat_group=CHAT_GROUP_REGRET
    )


label regret_bad_name:
    s bbaaaaa "It’s okay, [player]."
    s bbfdaca "Were you just kidding?"
    s bbfdaaa "I hope you weren’t being serious."
    s abhfaoa "Thank you for apologising though, apology accepted!"
    return


init 5 python:

    chatReg(
        Chat(
            persistent._regret_db,
            label="regret_long_absence",
            unlocked=True,
            prompt="For being away for so long.",
            conditional="fae_regrets.load_all_regrets(fae_regrets.LONG_ABSENCE)"
        ),
        chat_group=CHAT_GROUP_REGRET
    )


label regret_long_absence:

    s bbaaaaa "That’s alright, [player]."
    s abbbaoa "I understand, we all get a little busy sometimes."
    s abgbcaa "I’m just glad you’re back safe and sound!"
    s abhfaoa "So, where were we?"

    return

init 5 python:

    chatReg(
        Chat(
            persistent._regret_db,
            label="regret_offense",
            unlocked=True,
            prompt="For being offensive.",
            conditional="fae_regrets.load_all_regrets(fae_regrets.OFFENSE)"
        ),
        chat_group=CHAT_GROUP_REGRET
    )

label regret_offense:
    s bbaalra "Thank you for apologising, [player]."
    s bbaamca "What you said really hurt but…"
    s bbaaaaa "I understand that sometimes we forget to think before we speak, and say the wrong things."
    s abhfaoa "I’m just glad you took responsibility, let’s move on shall we."

    return

