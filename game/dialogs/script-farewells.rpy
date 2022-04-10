default persistent._f_db = dict()

default persistent.first_leave_reply = None


init -2 python in farewells:
    import random
    import store
    #import store.fae_globals as fae_globals
    import store.sayo_utilities as sayo_utilities

    FAREWELL_DEFS = dict()

    
    def gfo():
        """
        List of options for saying goodbye to our beloved Sayori
        """
        
        return [
            ("I'm going to sleep.", "leave_sleep"),
            ("I'm going to get something to eat.", "leave_eat"),
            ("I'm going school.", "leave_school")
        ]

    def leave_picker():

        if store.persistent.first_leave_reply is None:
            return "First_leave"

        kwargs = dict()

        leave_group = store.Chat.chat_filt(
            FAREWELL_DEFS.values(),
            no_categories=["Failsafe"],
            **kwargs
        )

        return random.choice(leave_group).label

label farewell_init:
    $ ats(farewells.leave_picker())
    jump cnc

label First_leave:
    s "Bye player"
    return { "quit": None}