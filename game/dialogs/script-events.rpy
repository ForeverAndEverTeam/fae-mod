default persistent._event_db = dict()


init -2 python in sayo_events:
    import random
    import store
    import store


    EVENT_DEFS = dict()


    def event_selector():

        kwargs = dict()

        event_list = store.Chat.chat_filt(
            EVENT_DEFS.values(),
            unlocked=True,
            has_seen=False,
            **kwargs
        )

        if len(event_list) > 0:
            return random.choice(event_list).label
        
        else:
            return None