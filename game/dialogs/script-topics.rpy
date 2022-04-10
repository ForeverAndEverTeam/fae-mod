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



