default persistent.fae_player_music_allowed = False
default persistent.fae_player_music_explained = False

define music.sn = "mod_assets/bgm/Slepyori_-_Loop.ogg"

init -1 python in fae_music:

    import os
    import store

    MUSIC_DIR_PLAYER = os.path.join(renpy.config.basedir, "game/custom_bgm/").replace("\\", "/")

    _ALLOWED_FILE_EXT = ["mp3", "ogg", "wav"]

    _now_playing = None
    
    def mute():

        renpy.music.stop
    

label music_menu:
    $ Sayori.setInChat(True)
    $ music_title = "Why didn't this change?"

    python:

        success = False

        if not fae_utilities.makedirifnot(fae_music.MUSIC_DIR_PLAYER):

            player_music_options = fae_utilities.getDirFile(
                path=fae_music.MUSIC_DIR_PLAYER,
                ext_list=fae_music._ALLOWED_FILE_EXT
            )
            player_music_options.sort()

            player_music_options.insert(0, ("Sayonara", "mod_assets/bgm/Sayonara_Acoustic_Medley.ogg"))
            
            player_music_options.append(("No music", "no_music"))
            success = True
    
    if not success:

        show sayori at t11
        s "Ummm..."
        s "Something isn't right."
        $ location = fae_music.MUSIC_DIR_PLAYER
        s "If you don't remember, anything you want me to play has to be in {a=[location]}custom_bgm{/a} folder."
        $ Sayori.setInChat(False)
        jump ch30_loop
    
    elif preferences.get_volume("music") == 0:

        show sayori at t11

        s "[player]..."
        s "The sound is off, silly."

        menu:
            s "Shall I turn the sound on?"

            "Yes, please.":
                s "Give me a sec."
                $ preferences.set_volume("music", 1.0)
                s "There we go."
                "What did you want to listen to?"
                show sayori idle at t22
            
            "No thanks.":
                s "Okay."
                $ Sayori.setInChat(False)
                jump ch30_loop
    
    else:
        show sayori idle at t22
    
    call screen neat_menu_scroll(player_music_options, ("Nevermind.", False))

    show sayori idle at t11

    if not _return:
        $ Sayori.isInChat(False)
        jump ch30_loop
    

    if _return == "no_music":
        $ music_title = "No music"

        stop music fadeout 3
        s "There you go."

    elif _return == "random":

        $ possible_player_music = fae_utilities.getDirFile(
            path=fae_music.MUSIC_DIR_PLAYER,
            extension_list=[".mp3", ".wav", ".ogg"]
        )

        python:
            if len(possible_player_music) > 1:
                music_title_and_file = random.choice(filter(lambda track: (fae_music._now_playing not in track), possible_player_music))
                music_title = music_title_and_file[0]
                renpy.play(filename=music_title_and_file[1], channel="music")
    
    elif _return is not None:

        $ music_title = _return.split('/')[-1]
        $ renpy.play(filename=_return, channel="music")
    
    $ fae_music._now_playing = music_title
    $ renpy.notify("Now playing: {0}".format(fae_music._now_playing))

    $ Sayori.isInChat(False)

    jump ch30_loop
        