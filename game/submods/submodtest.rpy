init -990 python in fae_submod_utilities:

    Submod(
        author="Nathan",
        name="Test Submod",
        description="This is a test submod",
        version="0.1",
        dependencies={},
        settings_pane=None,
        version_updates={}
    )

init 5 python:
    chatReg(
        Chat(
            persistent._chat_db,
            label="submod_test",
            unlocked=True,
            prompt="Submod Test",
            random=False,
            category=["submods"]
        ),
        chat_group=CHAT_GROUP_NORMAL
    )

label submod_test:

    s "I'm testing the submod."
    
    s "My affection is [persistent.affection]"

    s "Looks like it worked."

    s "Good job!"

    return


init 5 python:
    chatReg(
        Chat(
            persistent._chat_db,
            label="submod_chess",
            unlocked=True,
            prompt="Submod Chess",
            random=False,
            category=["Game"]
        ),
        chat_group=CHAT_GROUP_NORMAL
    )

label submod_chess:

    call game_chess from _call_game_chess

    return


init 5 python:
    chatReg(
        Chat(
            persistent._chat_db,
            label="submod_pong",
            unlocked=True,
            prompt="Submod Pong",
            random=False,
            category=["Game"]
        ),
        chat_group=CHAT_GROUP_NORMAL
    )

label submod_pong:

    call game_pong from _call_game_pong
    return