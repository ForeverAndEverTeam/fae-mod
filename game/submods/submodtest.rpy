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
            random=True,
            category=["submods"]
        ),
        chat_group=CHAT_GROUP_NORMAL
    )

label submod_test:

    s "I'm testing the submod."
    
    s "My affection is [persistent.affection]"

    if player_has_time_travelled:
        s "And they have time travelled"
    
    else:
        s "No time travel detected."

    s "Looks like it worked."

    s "Good job!"

    return