init python:
    def dlg():
        renpy.hide_screen('hidden')
        renpy.jump('talk_menu_wip')
    
    def select_music():
        renpy.jump('music')

    def mg():
        renpy.jump('mglist')

    #def spmask(dis_masks=True):
    #    mask = sog.get_mask()

    #    renpy.show(mask, tag="rm")

    #    if dis_masks:
    #        renpy.with_statement(Dissolve(1.0))

label sayo_autoload:
    #Start with black screen
    scene black

    python:
        quick_menu = True
        style.say_dialogue = style.normal
        in_sayori_kill = None
        allow_skipping = True
        config.allow_skipping = False
    #Do all the things for initial setup flow

label sayo_init:
    python:
        import random

        if not cielp("^greeting_"):
            if (
                random.randint(1, 10) == 1
                and fae_events.event_selector()
            ):
                ats(fae_events.event_selector())
                renpy.call("cnc", False)
            else:
                ats(greetings.greet_sel())
    
    show sayori acbaba with moveinleft
    hide black with Dissolve(2)
    show screen hidden

label idle_loop:
    #show sayori idle

    #show screen hidden
    
    show sayori acbaba with moveinleft
    
    while persistent._event_list:
        call cnc



label idle_wait:
    window hide

    $ renpy.pause(delay=5.0, hard=True)
    jump idle_loop

    #jump idle_loop
label cnc:
    if persistent._event_list:
        $ _chat = persistent._event_list.pop(0)

        if renpy.has_label(_chat):

            call expression _chat
    
    python:
        return_keys = _return if isinstance(_return, dict) else dict()

        chat_obj = get_chat(_chat)

        if chat_obj is not None:
            chat_obj.seen_no += 1
            chat_obj.latest_seen = datetime.datetime.now()

            if "derandom" in return_keys:
                chat_obj.random = False
    
    if "quit" in return_keys:
        jump quit
    
    python:
        global LCC
        LCC = datetime.datetime.now()
    jump idle_loop