init python:
    def dlg():
        renpy.hide_screen('overlay')
        renpy.call_screen('talk')
    
    def select_music():
        renpy.jump('music')

    def mg():
        renpy.jump('mglist')

label main_idle:
    window auto
    #Start with black scene
    scene black
    python:
        quick_menu = True
        style.say_dialogue = style.normal
        in_sayori_kill = None
        allow_skipping = True
        config.allow_skipping = False
    image bg spaceroom = "/mod_assets/images/spaceroom.png"


label prep:
    $ renpy.pause(5.0, hard=True)
    #scene spaceroom
    scene bg spaceroom with dissolve_cg
    

label idle_loop:
    #show sayori idle

    show screen overlay
    
    show sayori acbaba

    call hello

    $ quick_menu = True
    $ persistent.autoload = "main_idle"


    $ renpy.pause(0.5)


label idle_wait:
    window hide
    #$ renpy.pause(delay=5.0, hard=True)
    jump idle_loop

    #jump idle_loop