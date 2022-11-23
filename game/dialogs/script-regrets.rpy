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

    @staticmethod
    def add_new_regret_awaiting(regret_type):

        if not isinstance(regret_type, int) and not isinstance(regret_type, fae_regrets.RegretTypes):
            raise TypeError("regret_type must be of types int of fae_regrets.RegretTypes")
        
        if not int(regret_type) in store.persistent._fae_await_regret:
            store.persistent._fae_await_regret.append(int(regret_type))
    
    @staticmethod
    def add_regret_quit(regret_type):

        if not isinstance(regret_type, int) and not isinstance(regret_type, fae_regrets.RegretTypes):
            raise TypeError("regret_type must be of types int or fae_regrets.RegretTypes")
        
        store.persistent._fae_await_regret_quit = int(regret_type)
    
    @staticmethod
    def deleteRegret(regret_type):

        if not isinstance(regret_type, int) and not isinstance(regret_type, fae_regrets.RegretTypes):
            raise TypeError("regret_type must be of types int or fae_regrets.RegretTypes")
        
        if int(regret_type) in store.persistent._fae_await_regret:
            store.persistent._fae_await_regret.remove(int(regret_type))



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
            conditional="fae_regrets.load_regret_awaiting(fae_regrets.CHEATING)"
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

    $ persistent.fae_await_regret.remove(fae_regrets.CHEATING)
    return


init 5 python:

    chatReg(
        Chat(
            persistent._regret_db,
            prompt="For leaving without saying goodbye.",
            label="regret_sudden_quit",
            unlocked=True,
            conditional="fae_regrets.load_regret_awaiting(fae_regrets.UNEXPECTED_QUIT)"
        ),
        chat_group=CHAT_GROUP_REGRET
    )

label regret_sudden_quit:

    s "Thank you."
    
    $ persistent.fae_await_regret.remove(fae_regrets.UNEXPECTED_QUIT)

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

    if len(persistent.fae_await_regret) == 0:

        s "Huh?"

        s "For what?"

    else:

        "You know what you did."

        return
