default persistent._chat_db = dict()

#APPEARANCE-BASED SHIT

#EYE COLOUR
default persistent.ec = None

#HAIR LENGTH
default persistent.hl = None

#HAIR COLOUR
default persistent.hc = None

#HEIGHT 
default persistent.height = None

#Unit of measurement
default persistent.metric = True

init -2 python in chats:
    import store

    CHAT_DEFS = dict()



init 5 python:
    
    Chatreg(
        Chat(
            persistent._chat_db,
            label="testing",
            unlocked=True,
            prompt="testing",
            category=["DEV"]
        ),
        chat_group=CHAT_GROUP_NORMAL
    )


label testing:
    s "This is a test"
    return

