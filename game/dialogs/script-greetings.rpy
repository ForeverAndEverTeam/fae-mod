default persistent._g_db = dict()
default persistent.first = True

init -2 python in greetings:
    import random
    import store
    import store.farewells as farewells
    import store.sayo_utilities as sayo_utilities

    GREETING_DEFS = dict()

    def greet_sel():

        if store.persistent.first:
            return "first_greet"
        
        kwargs = dict()

        #TODO: ADD "IF" STATEMENTS FOR LEAVE CONDITIONS

        #RETURN GREETING

        return random.choice(
            store.Chat.chat_filt(
                GREETING_DEFS.values(),
                **kwargs
            )
        ).label

label first_greet:
    s "hello"
    $ persistent.first = False
    return "derandom"

init 5 python:
    Chatreg(
        Chat(
            persistent._g_db,
            label="s_1",
            unlocked=True
        ),
        chat_group=CHAT_GROUP_GREETING
    )

label s_1:
    return