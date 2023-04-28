init python:

    def enable_esc():

        global quick_menu
        quick_menu = True

    def disable_esc():
        """
        disables the escape key so you cant go to game menu
        NOTE: this also disables opening the game menu from other means
        """
        global quick_menu
        quick_menu = False

init python:

    
    def init_qabs():

        config.keymap["dialogue"] = ["t", "T"]
        config.keymap["music"] = ["m", "M"]
        config.keymap["games"] = ["g", "G"]
        config.keymap["Mute"] = ["shift_m", "shift_M"]
        #config.keymap["inc_musicvol"] = [
        #    "shift_K_PLUS","K_EQUALS","K_KP_PLUS"
        #]
        #config.keymap["dec_musicvol"] = [
        #    "K_MINUS","shift_K_UNDERSCORE","K_KP_MINUS"
        #]

        config.underlay.append(
            renpy.Keymap(dialogue=dlg)
        )

        if persistent.fae_player_music_allowed:
            config.underlay.append(
                renpy.Keymap(music=music_init)
            )

        config.underlay.append(
            renpy.Keymap(games=mg)
        )

        config.underlay.append(
            renpy.Keymap(Mute=fae_music.mute())
        )
    
    def remove_qabs():
        config.keymap["dialogue"] = ["t", "T"]
        config.keymap["music"] = ["m", "M"]
        config.keymap["games"] = ["g", "G"]
        config.keymap["Mute"] = ["shift_m", "shift_M"]

        config.underlay.append(
            renpy.Keymap(dialogue=None)
        )

        config.underlay.append(
            renpy.Keymap(music=None)
        )

        config.underlay.append(
            renpy.Keymap(games=None)
        )

        config.underlay.append(
            renpy.Keymap(Mute=fae_music.mute())
        )
