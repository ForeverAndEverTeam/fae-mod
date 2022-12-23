init -990 python in fae_submod_utilities:
    Submod(
        author="Z",
        name="Submod test",
        description="A simple testing submod.",
        version="0.0.1",
        dependencies={},
        settings_pane=None,
        version_updates={}
    )
init 5 python:

    chatReg(
        Chat(
            persistent._chat_db,
            label="s_topic_testing",
            unlocked=True,
            prompt="Submod test",
            random=False,
            category=["Submod"]
        ),
        chat_group=CHAT_GROUP_NORMAL
    )
label s_topic_testing:

    s abbbbs "Ooh, did Z figure out submodding?"
    s ebhade "Good job, Z!"

    return