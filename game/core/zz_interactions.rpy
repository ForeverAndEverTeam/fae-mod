init -1 python:

    def init_qabs():

        config.keymap["dlg"] = ["t", "T"]
        config.keymap["music"] = ["m", "M"]
        config.keymap["games"] = ["g", "G"]
        config.keymap["Mute"] = ["shift_m", "shift_M"]
        config.keymap["inc_musicvol"] = [
            "shift_K_PLUS","K_EQUALS","K_KP_PLUS"
        ]
        config.keymap["dec_musicvol"] = [
            "K_MINUS","shift_K_UNDERSCORE","K_KP_MINUS"
        ]

        config.underlay.append(
            renpy.Keymap(dlg=dlg)
        )

        config.underlay.append(
            renpy.Keymap(music=select_music)
        )

        config.underlay.append(
            renpy.Keymap(games=mg)
        )

        config.underlay.append(
            renpy.Keymap(Mute=mute)
        )
        config.underlay.append(
            renpy.Keymap(inc_musicvol=inc_vol)
        )
        config.underlay.append(
            renpy.Keymap(dec_musicvol=red_vol)
        )