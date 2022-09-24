## Styles
################################################################################

style default:
    font gui.default_font
    size gui.text_size
    color gui.text_color
    outlines [(2, "#000000aa", 0, 0)]
    line_overlap_split 1
    line_spacing 1

style default_monika is normal:
    slow_cps 30

style edited is default:
    font "gui/font/VerilySerifMono.otf"
    kerning 8
    outlines [(10, "#000", 0, 0)]
    xpos gui.text_xpos
    xanchor gui.text_xalign
    xsize gui.text_width
    ypos gui.text_ypos
    text_align gui.text_xalign
    layout ("subtitle" if gui.text_xalign else "tex")

style whisper is default:
    font gui.default_font
    size 20

style normal is default:
    xpos gui.text_xpos
    xanchor gui.text_xalign
    xsize gui.text_width
    ypos gui.text_ypos

    text_align gui.text_xalign
    layout ("subtitle" if gui.text_xalign else "tex")

style input:
    color gui.accent_color

style hyperlink_text:
    color gui.accent_color
    hover_color gui.hover_color
    hover_underline True

style splash_text:
    size 24
    color "#000"
    font gui.default_font
    text_align 0.5
    outlines []

style poemgame_text:
    yalign 0.5
    font "gui/font/Halogen.ttf"
    size 30
    color "#000"
    outlines []

    hover_xoffset -3
    hover_outlines [(3, "#fef", 0, 0), (2, "#fcf", 0, 0), (1, "#faf", 0, 0)]

style gui_text:
    font gui.interface_font
    color gui.interface_text_color
    size gui.interface_text_size


style button:
    properties gui.button_properties("button")
    xysize (None, 36)
    padding (4, 4, 4, 4)

style button_dark:
    properties gui.button_properties("button_dark")
    xysize (None, 36)
    padding (4, 4, 4, 4)

style button_text is gui_text:
    properties gui.button_text_properties("button")
    font gui.interface_font
    size gui.interface_text_size
    idle_color gui.idle_color
    hover_color gui.hover_color
    selected_color gui.selected_color
    insensitive_color gui.insensitive_color
    align (0.0, 0.5)


style button_text_dark is gui_text:
    properties gui.button_text_properties("button_dark")
    font gui.interface_font
    size gui.interface_text_size
    idle_color gui.idle_color
    hover_color gui.hover_color
    selected_color gui.selected_color
    insensitive_color gui.insensitive_color
    align (0.0, 0.5)

style label_text is gui_text:
    color gui.accent_color
    size gui.label_text_size

style label_text_dark is gui_text:
    size gui.label_text_size
    color gui.accent_color

style prompt_text is gui_text:
    color gui.text_color
    size gui.interface_text_size

style tm_vbox is choice_vbox:
    xcenter 960

style tm_button is choice_button:
    #xysize (215, 35)
    padding (5, 5, 5, 5)
    #background Frame("mod_assets/buttons/[prefix_]bg2.png", Borders(5, 5, 5, 5), tile=False)
    #insensitive_color sayo_utilities.button_text_insensitive_color

style tm_button_text is choice_button_text:
    kerning 0.2


style tc_vbox is choice_vbox:
    xcenter 960

style tc_button is choice_button:
    xysize (215, 35)
    padding (5, 5, 5, 5)
    background Frame("mod_assets/buttons/[prefix_]bg2.png", Borders(5, 5, 5, 5), tile=False)
    #insensitive_color sayo_utilities.button_text_insensitive_color

style tci_vbox is choice_vbox:
    xcenter 960

style tci_button is choice_button:
    xysize (5, 5)
    padding (5, 5, 5, 5)

style tci_button_text is choice_button_text:
    kerning 0.2

style tc_button_text is choice_button_text:
    kerning 0.2

style tcs_b_vbox is choice_vbox:
    xcenter 960

style tcs_b_button is choice_button:
    background Frame("mod_assets/buttons/[prefix_]bg2.png", Borders(5, 5, 5, 5), tile=False)

style tcs_b_button_text is choice_button_text


style minigame_button is choice_button:
    xpadding 0 
    xsize 200

style minigame_button_text is choice_button_text

style minigame_vbox is choice_vbox


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style bar:
    ysize 18
    base_bar Frame("gui/scrollbar/horizontal_poem_bar.png", tile=False)
    thumb Frame("gui/scrollbar/horizontal_poem_thumb.png", top=6, right=6, tile=True)

style scrollbar:
    ysize 18
    base_bar Frame("gui/scrollbar/horizontal_poem_bar.png", tile=False)
    thumb Frame("gui/scrollbar/horizontal_poem_thumb.png", top=6, right=6, tile=True)
    unscrollable "hide"
    bar_invert True

style scrollbar_dark:
    ysize 18
    base_bar Frame("gui/scrollbar/horizontal_poem_bar_d.png", tile=False)
    thumb Frame("gui/scrollbar/horizontal_poem_thumb.png", top=6, right=6, tile=True)
    unscrollable "hide"
    bar_invert True

style vscrollbar:
    xsize 18
    base_bar Frame("gui/scrollbar/vertical_poem_bar.png", tile=False)
    thumb Frame("gui/scrollbar/vertical_poem_thumb.png", left=6, top=6, tile=True)
    unscrollable "hide"
    bar_invert True

style vscrollbar_dark:
    xsize 18
    base_bar Frame("gui/scrollbar/vertical_poem_bar_d.png", tile=False)
    thumb Frame("gui/scrollbar/vertical_poem_thumb.png", left=6, top=6, tile=True)
    unscrollable "hide"
    bar_vertical True
    bar_invert True

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize 18
    base_bar Frame("gui/scrollbar/horizontal_poem_bar.png", tile=False)
    thumb "gui/slider/horizontal_hover_thumb.png"

style slider_dark:
    ysize 18
    base_bar Frame("gui/scrollbar/horizontal_poem_bar_d.png", tile=False)
    thumb "gui/slider/horizontal_hover_thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)
    # background Frame(recolorize("gui/frame.png"), gui.frame_borders, tile=gui.frame_tile)

style frame_dark:
    padding gui.frame_borders.padding
    background Frame("gui/frame_d.png", gui.frame_borders, tile=gui.frame_tile)




style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Transform("gui/textbox.png", xalign=0.5, yalign=1.0)

style window_dark is default:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height
    background Image("gui/textbox_d.png", xalign=0.5, yalign=1.0)

style window_monika is window:
    background Transform("gui/textbox_monika.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style namebox_dark is default:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height
    background Frame("gui/namebox_d.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    color gui.accent_color
    font gui.name_font
    size gui.name_text_size
    xalign gui.name_xalign
    yalign 0.5
    outlines [(3, text_outline_color, 0, 0), (1, text_outline_color, 1, 1)]
    #outlines [(3, "#b59", 0, 0), (1, "#b59", 1, 1)]

style say_label_dark is default:
    font gui.name_font
    size gui.name_text_size
    xalign gui.name_xalign
    yalign 0.5
    color "#dad9ff"
    outlines [(3, "#3636de", 0, 0), (1, "#3636de", 1, 1)]

style say_dialogue:
    xpos gui.text_xpos
    xanchor gui.text_xalign
    xsize gui.text_width
    ypos gui.text_ypos

    text_align gui.text_xalign
    layout ("subtitle" if gui.text_xalign else "tex")

style input_prompt is default

style input_prompt:
    xmaximum gui.text_width
    xalign gui.text_xalign
    text_align gui.text_xalign

style input:
    caret "input_caret"
    xmaximum gui.text_width
    xalign 0.5
    text_align 0.5


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 270
    yanchor 0.5

    spacing gui.choice_spacing

#style choice_button is default:
style choice_button is generic_button_light:
    properties gui.button_properties("choice_button")
    hover_sound gui.hover_sound
    activate_sound gui.activate_sound
    idle_background Frame("gui/button/choice_idle_background.png", gui.choice_button_borders)
    hover_background Frame("gui/button/choice_hover_background.png", gui.choice_button_borders)

style choice_button_dark is generic_button_dark:
    xysize (420, None)
    padding (100, 5, 100, 5)


#style choice_button_text is default:
style choice_button_text is generic_button_text_light:
    properties gui.button_text_properties("choice_button")
    outlines []

style choice_button_text_dark is generic_button_text_dark:
    text_align 0.5
    layout "subtitle"

style quick_button:
    properties gui.button_properties("quick_button")
    activate_sound gui.activate_sound

style quick_button_dark:
    properties gui.button_properties("quick_button_dark")
    activate_sound gui.activate_sound


style quick_button_text:
    properties gui.button_text_properties("quick_button")
    outlines []

style quick_button_text_dark:
    properties gui.button_text_properties("quick_button_dark")
    xysize (205, None)
    font gui.default_font
    size 14
    idle_color "#e999ff"
    selected_color "#ebf1ff"
    hover_color "#d8ccff"
    kerning 0.2
    outlines []

style navigation_button is gui_button
style navigation_button_text is gui_button_text

#style navigation_button:
style navigation_button is gui_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")
    hover_sound gui.hover_sound
    activate_sound gui.activate_sound

style navigation_button_dark is gui_button:
    properties gui.button_properties("navigation_button_dark")
    hover_sound gui.hover_sound
    activate_sound gui.activate_sound


#style navigation_button_text:
style navigation_button_text is gui_button_text:
    properties gui.button_text_properties("navigation_button")
    font "gui/font/RifficFree-Bold.ttf"
    color "#fff"
    outlines [(4, text_outline_color, 0, 0), (2, text_outline_color, 2, 2)]
    #outlines [(4, "#b59", 0, 0), (2, "#b59", 2, 2)]
    hover_outlines [(4, "#fac", 0, 0), (2, "#fac", 2, 2)]
    insensitive_outlines [(4, "#fce", 0, 0), (2, "#fce", 2, 2)]

style navigation_button_text_dark is gui_button_text_dark:
    properties gui.button_text_properties("navigation_button_dark")
    font "gui/font/RifficFree-Bold.ttf"
    color "#FFD9E8"
    outlines [(4, "#4136de", 0, 0), (2, "#3936de", 2, 2)]
    hover_outlines [(4, "#8f80ff", 0, 0), (2, "#8880ff", 2, 2)]
    insensitive_outlines [(4, "#bab2ff", 0, 0), (2, "#b6b2ff", 2, 2)]

style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text:
    color "#000000"
    size 16
    outlines []

style main_menu_version_dark is main_menu_text:
    color fae_ui.dark_button_text_idle_color
    size 16
    outlines []

style main_menu_frame:
    xsize 310
    yfill True

    background "menu_nav"

style main_menu_frame_dark is empty:
    xsize 310
    yfill True
    background "menu_nav"


style main_menu_vbox:
    xalign 1.0
    xoffset -20
    xmaximum 800
    yalign 1.0
    yoffset -20

style main_menu_text:
    xalign 1.0

    layout "subtitle"
    text_align 1.0
    color gui.accent_color

style main_menu_title:
    size gui.title_text_size



style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 30
    top_padding 120

    background "gui/overlay/game_menu.png"
    # background recolorize("gui/overlay/game_menu.png")

style game_menu_outer_frame_dark is empty:
    bottom_padding 30
    top_padding 120
    background "gui/overlay/game_menu_d.png"

style game_menu_navigation_frame:
    xsize 280
    yfill True

style game_menu_content_frame:
    left_margin 40
    right_margin 20
    top_margin 10

style game_menu_viewport:
    xsize 920

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 10

style game_menu_label:
    xpos 50
    ysize 120

style game_menu_label_dark is gui_label:
    xpos 50
    ysize 120

style game_menu_label_text:
    font "gui/font/RifficFree-Bold.ttf"
    size gui.title_text_size
    color "#fff"
    outlines [(6, text_outline_color, 0, 0), (3, text_outline_color, 2, 2)]
    #outlines [(6, "#b59", 0, 0), (3, "#b59", 2, 2)]
    yalign 0.5

style game_menu_label_text_dark is gui_label_text:
    font "gui/font/RifficFree-Bold.ttf"
    size gui.title_text_size
    color "#d9daff"
    outlines [(6, "#3c36de", 0, 0), (3, "#363cde", 2, 2)]
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -30

style return_button_dark is navigation_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -30

style return_button_text_dark is navigation_button_text_dark


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 50
    ypadding 3

style page_label_text:
    color "#000"
    outlines []
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.button_text_properties("page_button")
    outlines []

style slot_button:
    properties gui.button_properties("slot_button")
    idle_background Frame("gui/button/slot_idle_background.png", gui.choice_button_borders)
    hover_background Frame("gui/button/slot_hover_background.png", gui.choice_button_borders)

style slot_button_text:
    properties gui.button_text_properties("slot_button")
    color "#666"
    outlines []


style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 2

style pref_label_text:
    font "gui/font/RifficFree-Bold.ttf"
    size 24
    color "#fff"
    outlines [(3, "#b59", 0, 0), (1, "#b59", 1, 1)]
    yalign 1.0

style pref_vbox:
    xsize 225

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style radio_button_text:
    properties gui.button_text_properties("radio_button")
    font "gui/font/Halogen.ttf"
    outlines []

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.button_text_properties("check_button")
    font "gui/font/Halogen.ttf"
    outlines []

style slider_slider:
    xsize 350

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 10

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 450



style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5



style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame("gui/frame.png", gui.confirm_frame_borders, tile=gui.frame_tile)
    # background Frame(recolorize("gui/frame.png"), gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    color "#000"
    outlines []
    text_align 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")
    hover_sound gui.hover_sound
    activate_sound gui.activate_sound

style confirm_button_text is navigation_button_text:
    properties gui.button_text_properties("confirm_button")



style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    # We have to use a font that has the BLACK RIGHT-POINTING SMALL TRIANGLE
    # glyph in it.
    font "DejaVuSans.ttf"



style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    size gui.notify_text_size



style bsod_win7_text is gui_text
style bsod_win7_text:
    font "C:/Windows/Fonts/lucon.ttf"
    antialias False
    size 13
    line_leading 15
    line_spacing -14
    xsize 1279
    outlines []

style bsod_win8_text is gui_text
style bsod_win8_text:
    font "C:/Windows/Fonts/segoeuil.ttf"
    size 25
    line_spacing 5
    xsize 600
    outlines []

style bsod_win8_sad_text is gui_text
style bsod_win8_sad_text is bsod_win8_text:
    size 128
    xpos -8

style bsod_win8_sub_text is gui_text
style bsod_win8_sub_text is bsod_win8_text:
    size 11

style bsod_win10_text is bsod_win8_text
style bsod_win10_text:
    font "C:/Windows/Fonts/segoeuil.ttf"
    size 24
    line_leading 3
    line_spacing 0
    xsize 800
    outlines []

style bsod_win10_info_text is bsod_win10_text
style bsod_win10_info_text:
    size 16

style bsod_win10_sad_text is bsod_win10_text
style bsod_win10_sad_text:
    size 136
    xpos -8

style bsod_win10_sub_text is bsod_win10_text
style bsod_win10_sub_text:
    size 11

style bsod_mac_text is gui_text
style bsod_mac_text:
    font gui.default_font
    size 28
    outlines []
    line_spacing -30

style bsod_linux_text is gui_text
style bsod_linux_text:
    font "gui/font/F25_Bank_Printer.ttf"
    size 15
    outlines []
    line_leading 5


style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.button_text_properties("nvl_button")

default persistent._fae_dark_mode_enabled = False

style scrollable_menu_vbox is vbox:
    xalign 0.5
    ypos 260
    yanchor 0.5
    spacing 5

style scrollable_menu_button is choice_button:
    xysize (240, None)
    padding (25, 5, 25, 5)



style scrollable_menu_button_text is choice_button_text:
    text_align 0.0
    align (0.0, 0.0)



style scrollable_menu_new_button is scrollable_menu_button


style scrollable_menu_new_button_text is scrollable_menu_button_text:
    italic True


style scrollable_menu_special_button is scrollable_menu_button

style scrollable_menu_special_button_text is scrollable_menu_button_text:
    bold True


style scrollable_menu_crazy_button is scrollable_menu_button


style scrollable_menu_crazy_button_text is scrollable_menu_button_text:
    italic True
    bold True

init -1 python in fae_globals:

    dark_mode = None

    change_textbox = True

    button_text_hover_color = None
    button_text_idle_color = None


init -201 python in fae_ui:

    dark_suffix = "_dark"

    # confirm
    CNF_BG = "gui/overlay/confirm.png"

    # selector
    SEL_SB_FRAME = "mod_assets/frames/black70_pinkborder100_5px.png"


init -200 python in fae_ui:

    style_storage = {}

    dark_button_text_idle_color = "#665bfd"
    dark_button_text_hover_color = "#abb1ff"
    dark_button_text_insensitive_color = "#8C8C8C"

    light_button_text_idle_color = "#000"
    light_button_text_hover_color = "#fa9"
    light_button_text_insensitive_color = "#8C8C8C"

    button_text_idle_color = "#000"
    button_text_hover_color = "#fa9"
    button_text_insensitive_color = "#8C8C8C"

    SCROLLABLE_MENU_X = 70
    SCROLLABLE_MENU_Y = 50

    SCROLLABLE_MENU_W = 250

    SCROLLABLE_MENU_TALL_H = 640
    SCROLLABLE_MENU_MEDIUM_H = 572
    SCROLLABLE_MENU_LOW_H = 528
    SCROLLABLE_MENU_VLOW_H = 484

    SCROLLABLE_MENU_TXT_TALL_H = 528
    SCROLLABLE_MENU_TXT_MEDIUM_H = 440
    SCROLLABLE_MENU_TXT_LOW_H = 396

    SCROLLABLE_MENU_XALIGN = -0.05

    # HOW TO CHOOSE:
    #    TXT for menus w/ the dlg box
    #    TALL for menus w/o final buttons
    #    MEDIUM for menus w/ one final button
    #    LOW for menus w/ 2 final buttons
    #    VLOW for menus w/ 3 final buttons

    SCROLLABLE_MENU_TALL_AREA = (SCROLLABLE_MENU_X, SCROLLABLE_MENU_Y, SCROLLABLE_MENU_W, SCROLLABLE_MENU_TALL_H)
    SCROLLABLE_MENU_MEDIUM_AREA = (SCROLLABLE_MENU_X, SCROLLABLE_MENU_Y, SCROLLABLE_MENU_W, SCROLLABLE_MENU_MEDIUM_H)
    SCROLLABLE_MENU_LOW_AREA = (SCROLLABLE_MENU_X, SCROLLABLE_MENU_Y, SCROLLABLE_MENU_W, SCROLLABLE_MENU_LOW_H)
    SCROLLABLE_MENU_VLOW_AREA = (SCROLLABLE_MENU_X, SCROLLABLE_MENU_Y, SCROLLABLE_MENU_W, SCROLLABLE_MENU_VLOW_H)

    SCROLLABLE_MENU_TXT_TALL_AREA = (SCROLLABLE_MENU_X, SCROLLABLE_MENU_Y, SCROLLABLE_MENU_W, SCROLLABLE_MENU_TXT_TALL_H)
    SCROLLABLE_MENU_TXT_MEDIUM_AREA = (SCROLLABLE_MENU_X, SCROLLABLE_MENU_Y, SCROLLABLE_MENU_W, SCROLLABLE_MENU_TXT_MEDIUM_H)
    SCROLLABLE_MENU_TXT_LOW_AREA = (SCROLLABLE_MENU_X, SCROLLABLE_MENU_Y, SCROLLABLE_MENU_W, SCROLLABLE_MENU_TXT_LOW_H)


init python:
    
    import store.fae_globals as fae_globals
    import store.fae_ui as fae_ui
    

    def fae_getTimeFile(filestring):

        if not fae_globals.dark_mode:
            return filestring
        
        else:

            if '.' in filestring:
                extension = filestring[filestring.index('.'):]
                path = filestring[:filestring.index('.')]
                return path + "_d" + extension
            # If that fails then we just return the normal one
            return filestring
    
    def fae_swapStyle(base_name, dark_name, is_morning):


        if base_name not in fae_ui.style_storage:
            fae_ui.style_storage[base_name] = getattr(style, base_name)
        
        if is_morning:
            stored_style = fae_ui.style_storage[base_name]
            setattr(style, base_name, fae_ui.style_storage[base_name])
        
        else:
            dark_style = getattr(style, dark_name)
            setattr(style, base_name, dark_style)
    
    def fae_hasDarkStyle(style_name):
        """
        Check if selected style has a dark alternative.
        """
        dark_style_name = style_name + fae_ui.dark_suffix

        for other_tuple in renpy.style.styles:
            other_name = other_tuple[0]
            if other_name == dark_style_name:
                return True

        return False

    def fae_isDarkStyle(style_name):
        """
        Check if selected style is a dark style.
        """
        return style_name.endswith(fae_ui.dark_suffix)

    def fae_isTextDarkStyle(style_name):
        """
        Check if selected style is a text_dark style.
        """
        text_dark_suffix = "_text" + fae_ui.dark_suffix
        return style_name.endswith(text_dark_suffix)

    def fae_darkMode(is_morning=False):
        """
        Swaps all styles to dark/light mode provided on the input

        IN:
            morning_flag - if True, light mode, if False, dark mode
        """
        # Create aliases
        # FIXME: could be done on startup for some speedup
        new_aliases = {}

        for style_tuple, style_ptr in renpy.style.styles.items():
            style_name = style_tuple[0]
            if fae_isTextDarkStyle(style_name):
                text_dark_suffix = "_text" + fae_ui.dark_suffix
                suffix_len = len(text_dark_suffix)
                alias_name = style_name[:-suffix_len] + fae_ui.dark_suffix + "_text"
                if not style.exists(alias_name):
                    new_aliases[alias_name] = style_ptr

        for alias_name, alias_style_ptr in new_aliases.items():
            setattr(style, alias_name, alias_style_ptr)

        # Automagically switch every style which has a dark variant
        for style_tuple in renpy.style.styles.keys():
            style_name = style_tuple[0]
            if not fae_isDarkStyle(style_name) and fae_hasDarkStyle(style_name):
                dark_style_name = style_name + fae_ui.dark_suffix
                fae_swapStyle(style_name, dark_style_name, is_morning)

        if not is_morning:
            # Handle the global swaps
            fae_globals.dark_mode = True

            fae_globals.button_text_idle_color = fae_ui.dark_button_text_idle_color
            fae_globals.button_text_hover_color = fae_ui.dark_button_text_hover_color
            fae_globals.button_text_insensitive_color = fae_ui.dark_button_text_insensitive_color

            # Textbox
            if fae_globals.change_textbox:
                style.say_window = style.window_dark

        else:
            # Handle the global swaps
            fae_globals.dark_mode = False

            fae_globals.button_text_idle_color = fae_ui.light_button_text_idle_color
            fae_globals.button_text_hover_color = fae_ui.light_button_text_hover_color
            fae_globals.button_text_insensitive_color = fae_ui.light_button_text_insensitive_color

            # Textbox
            if fae_globals.change_textbox:
                style.say_window = style.window

        # Timefile changes
        fae_ui.cm_bg = fae_getTimeFile(fae_ui.CNF_BG)
        fae_ui.sel_sb_frame = fae_getTimeFile(fae_ui.SEL_SB_FRAME)

        # Reset the global flag
        fae_globals.change_textbox = True

        style.rebuild()

init python in fae_settings:
    _persistent = renpy.game.persistent

    ui_changed = False
    dark_mode_clicked = False

    import store
    
    def _dark_mode_toggle():
        """
        Handles the toggling of fields so the menu options become mutually exclusive
        """
        if _persistent._fae_dark_mode_enabled:
            _persistent._fae_dark_mode_enabled = False

        else:
            _persistent._fae_dark_mode_enabled = True
            _persistent._fae_auto_mode_enabled = False

        global dark_mode_clicked
        dark_mode_clicked = True

    def _ui_change_wrapper(*args):
        """
        Wrapper around UI changes

        IN:
            *args - values to pass to dark mode
        """
        global ui_changed
        ui_changed = True
        store.fae_darkMode(*args)


style generic_button_base:
    hover_sound gui.hover_sound
    activate_sound gui.activate_sound

style generic_button_light is generic_button_base:
    background Frame("mod_assets/buttons/generic/[prefix_]bg.png", Borders(5, 5, 5, 5), tile=False)

style generic_button_dark is generic_button_base:
    background Frame("mod_assets/buttons/generic/[prefix_]bg_d.png", Borders(5, 5, 5, 5), tile=False)

style generic_button_text_base:
    font gui.default_font
    size gui.text_size
    align (0.5, 0.1)
    outlines []

style generic_button_text_light is generic_button_text_base:
    idle_color fae_ui.light_button_text_idle_color
    hover_color fae_ui.light_button_text_hover_color
    insensitive_color fae_ui.light_button_text_insensitive_color

style generic_button_text_dark is generic_button_text_base:
    idle_color fae_ui.dark_button_text_idle_color
    hover_color fae_ui.dark_button_text_hover_color
    insensitive_color fae_ui.dark_button_text_insensitive_color

image generic_fancy_check_button_fg = Image("mod_assets/buttons/checkbox/fancy_check.png", yoffset=4)
image generic_fancy_check_button_fg_insensitive = Image("mod_assets/buttons/checkbox/insensitive_fancy_check.png", yoffset=4)
image generic_fancy_check_button_fg_selected = Image("mod_assets/buttons/checkbox/selected_fancy_check.png", yoffset=4)
image generic_fancy_check_button_fg_selected_insensitive = Image("mod_assets/buttons/checkbox/selected_insensitive_fancy_check.png", yoffset=4)

# fancy checkbox buttons lose the box when selected
# and the entire frame gets colored
style generic_fancy_check_button:
    properties gui.button_properties("check_button")
    foreground "generic_fancy_check_button_fg"
    selected_foreground "generic_fancy_check_button_fg_selected"
    selected_insensitive_foreground "generic_fancy_check_button_fg_selected_insensitive"
    hover_background Solid("#ffe6f4")
    selected_background Solid("#FFBDE1")

style generic_fancy_check_button_dark:
    properties gui.button_properties("check_button_dark")
    foreground "generic_fancy_check_button_fg"
    selected_foreground "generic_fancy_check_button_fg_selected"
    selected_insensitive_foreground "generic_fancy_check_button_fg_selected_insensitive"
    hover_background Solid("#7673d9")
    selected_background Solid("#4a4ece")

style generic_fancy_check_button_disabled is generic_fancy_check_button:
    properties gui.button_properties("check_button")
    foreground "generic_fancy_check_button_fg_insensitive"
    selected_foreground "generic_fancy_check_button_fg_selected_insensitive"
    selected_background Solid("1b1b1b")

style generic_fancy_check_button_text is gui_button_text:
    properties gui.button_text_properties("generic_fancy_check_button")
    font "gui/font/Halogen.ttf"
    color "#BFBFBF"
    hover_color "#000000"
    selected_color "#000000"
    insensitive_color fae_ui.light_button_text_insensitive_color
    outlines []
    yoffset 3

style generic_fancy_check_button_text_dark is gui_button_text_dark:
    properties gui.button_text_properties("generic_fancy_check_button_dark")
    font "gui/font/Halogen.ttf"
    color "#BFBFBF"
    hover_color "#FFAA99"
    selected_color "#FFAA99"
    insensitive_color fae_ui.dark_button_text_insensitive_color
    outlines []
    yoffset 3

style generic_fancy_check_button_disabled_text is generic_fancy_check_button:
    properties gui.button_text_properties("generic_fancy_check_button")
    font "gui/font/Halogen.ttf"
    color "#8C8C8C"
    outlines []
    yoffset 3