init python:
    def extra_menu():

        renpy.jump("fae_extra_menu")


init -2 python in fae_extras:

    import store

    menu_visible = False

label fae_extra_menu:

    $ store.fae_extras.menu_visible = True

    $ prev_zoom = store.fae_sprites.zoom_level

    show screen fae_extra_menu
    jump ch30_loop

label fae_extra_menu_close:

    $ store.fae_extras.menu_visible = False

    hide screen fae_extra_menu

    if store.fae_sprites.zoom_level != prev_zoom:
        call fae_extra_menu_zoom_return from _call_fae_extra_menu_zoom_return
    
    show sayori idle

    jump ch30_loop

label fae_extra_menu_zoom_return:

    $ import store.fae_sprites as fae_sprites
    
    if fae_sprites.zoom_level < fae_sprites.default_zoom_level:

        if not persistent._fae_zoomed_out:
            $ persistent._fae_zoomed_out = True
    
    elif fae_sprites.zoom_level == fae_sprites.max_zoom:
        
        if not persistent._fae_zoomed_in_max:

            $ persistent._fae_zoomed_in_max = True
            $ persistent._fae_zoomed_in = True
    
    elif fae_sprites.zoom_level > fae_sprites.default_zoom_level:

        if not persistent._fae_zoomed_in:

            $ persistent._fae_zoomed_in = True
        
    return

style fae_extra_menu_frame:
    background Frame("mod_assets/images/Frames/trans_pink2pxborder100.png", Borders(2, 2, 2, 2, pad_top=2, pad_bottom=4))

style fae_adjust_vbar:
    xsize 18
    base_bar Frame("gui/scrollbar/vertical_poem_bar.png", tile=False)
    thumb "gui/slider/horizontal_hover_thumb.png"
    bar_vertical True

style fae_adjustable_button is generic_button_light:
    xysize (None, None)
    padding (3, 3, 3, 3)

style fae_adjustable_button_text is generic_button_text_light:
    kerning 0.2

screen fae_extra_menu():

    zorder 52

    key "e" action Jump("fae_extra_menu_close")
    key "E" action Jump("fae_extra_menu_close")

    frame:
        area (0, 0, 1280, 720)
        background Solid("#0000007F")

        # close button
        textbutton _("Close"):
            area (60, 596, 120, 35)
            style "t_m_button"
            action Jump("fae_extra_menu_close")

        
        