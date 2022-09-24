
init python:
    def dumpPersistentToFile(dumped_persistent, dumppath):

        dumped_persistent = vars(dumped_persistent)

        fo = open(dumppath, "w")

        for key in sorted(dumped_persistent.keys()):
            fo.write(str(key) + ' - ' + str(type(dumped_persistent[key])) + ' >>> '+ str(dumped_persistent[key]) + '\n\n')
        
        fo.close()

label import_ddlc_persistent_in_settings:

    call import_ddlc_persistent from _call_import_ddlc_persistent_1 #from _call_import_ddlc_persistent_1

    $ enable_esc()

    return

label import_ddlc_persistent:

    $ quick_menu = False
    scene black
    with Dissolve(1.0)

    if persistent._fae_imported_saves:
        menu:
            "Save data from DDLC has already been merged. Stopping."

            "Okay.":
                pass

        pause 0.3
        return

    python:
        from glob import glob

        if renpy.macintosh:
            rv = "~/Library/RenPy/"
            check_path = os.path.expanduser(rv)

        elif renpy.windows:
            if 'APPDATA' in os.environ:
                check_path = os.environ['APPDATA'] + "/RenPy/"
            
            else:
                rv = "~/RenPy/"
                check_path = os.path.expanduser(rv)
        
        else:
            rv = "~/RenPy/"
            check_path = os.path.expanduser(rv)
        
        ddlc_save_path = glob(check_path + 'DDLC/persistent')
        if not ddlc_save_path:
            ddlc_save_path = glob(check_path + 'DDLC-*/persistent')
    
    if ddlc_save_path:
        $ ddlc_save_path = ddlc_save_path[0]

        "Save data for DDLC was found at [ddlc_save_path]."
        menu:
            "Would you like to import Doki Doki Literature Club save data into [config.name]?\n(DDLC will not be affected)"

            "Yes, import DDLC save data.":
                pause 0.3

            "No, do not import.":
                pause 0.3
                return
        
    else:

        "Save data from DDLC could not be found."

        menu:
            "Save data will not be imported at this time."

            "Okay":
                pause 0.3
                return
    

    python:
        #Open the persistent save file at ddlc_save_path
        ddlc_persistent = None
        try:
            with open(ddlc_save_path, "rb") as ddlc_pfile:
                ddlc_persistent = fae_dockstat.pickle.loads(ddlc_pfile.read().decode("zlib"))
        
        except Exception as e:
            store.fae_utilities.fae_log.error("FAILED TO READ/DECODE DDLC PERSISTENT: {0}".format(e))
        
        else:

            store.fae_versions.init()
            ddlc_persistent = updateTopicIDs("v030", ddlc_persistent)
            ddlc_persistent = updateTopicIDs("v031", ddlc_persistent)
            ddlc_persistent = updateTopicIDs("v032", ddlc_persistent)
            ddlc_persistent = updateTopicIDs("v033", ddlc_persistent)
            fae_versions.clear()
    
    if ddlc_persistent is None:
        menu:
            "Couldn't read/decode save data from Doki Doki Literature Club. Aborting."

            "Okay.":
                pass

        pause 0.3
        return

    #Check if previous MAS data exists
    if not persistent.first_run:
        label .save_merge_or_replace:
        menu:
            "PREVIOUS FAE SAVE DATA HAS BEEN FOUND.\nWOULD YOU LIKE TO MERGE WITH DDLC SAVE DATE?"

            "Merge save data.":
                pass

            "Cancel.":
                "DDLC DATA CAN BE IMPORTED LATER IN THE SETTINGS MENU"
                return
    python:
        def _updatePersistentDict(key, old_persistent, new_persistent):
                """
                Merges the old persistent dict at the key provided into the new persistent
                IN:
                    key - key to update
                    old_persistent - persistent to copy data from
                    new_persistent - persistent to copy data to
                NOTE: Should only be used to update dicts
                """
                if key not in old_persistent.__dict__:
                    return

                if old_persistent.__dict__[key] is not None:
                    if (
                        key in new_persistent.__dict__
                        and new_persistent.__dict__[key] is not None
                    ):
                        new_persistent.__dict__[key].update(old_persistent.__dict__[key])

                    else:
                        new_persistent.__dict__[key] = old_persistent.__dict__[key]

        def _updatePersistentBool(key, old_persistent, new_persistent):
            """
            Merges bools from the old persistent at the key provided into the new persistent
            IN:
                key - key to update
                old_persistent - persistent to copy data from
                new_persistent - persistent to copy data to
            NOTE: Should only be used to update bools
            """
            if key not in old_persistent.__dict__:
                return

            if old_persistent.__dict__[key] is not None:
                new_persistent.__dict__[key] = old_persistent.__dict__[key]

            #START: Transfers
            #_seen_ever: A dict storing all the labels we've seen through the game
            _updatePersistentDict("_seen_ever", ddlc_persistent, persistent)

            #_seen_audio: A dict storing all the audio we've heard through the game
            _updatePersistentDict("_seen_audio", ddlc_persistent, persistent)

            #_seen_images: A dict storing all images the player has seen
            _updatePersistentDict("_seen_images", ddlc_persistent, persistent)

            #clearall: Whether or not the player has achieved the perfect ending
            _updatePersistentBool("clearall", ddlc_persistent, persistent)

            #monika_kill: Whether or not the player has deleted Monika's character file in act 3
            _updatePersistentBool("monika_kill", ddlc_persistent, persistent)

            #tried_skip: Whether or not the player has tried to skip Monika's dialogue in act 3
            _updatePersistentBool("tried_skip", ddlc_persistent, persistent)

            if ddlc_persistent.clear is not None:
                if persistent.clear is not None:
                    for index in range(len(persistent.clear)-1):
                        persistent.clear[index] = persistent.clear[index] or ddlc_persistent.clear[index]

                else:
                    persistent.clear = ddlc_persistent.clear

            #playername: Player's name for the MC in ddlc
            if ddlc_persistent.playername:
                if persistent.playername and persistent.playername != ddlc_persistent.playername:
                    renpy.call_in_new_context("merge_unmatched_names")

                else:
                    persistent.playername = ddlc_persistent.playername

            player = persistent.playername

            #playthrough: What act did we leave off on? (0: intro, 1: act 1, 2: act 2, 3: act 3, 4: act 4)
            #NOTE: We only carry this over if we've gone farther on the ddlc persist than the current persist
            if ddlc_persistent.playthrough is not None:
                if (
                    persistent.playthrough is None
                    or persistent.playthrough < ddlc_persistent.playthrough
                ):
                    persistent.playthrough = ddlc_persistent.playthrough
            

            __fae__memoryCleanup()

            persistent._fae_imported_saves = True
        
    return

label merge_unmatched_names:
    menu:
        "Player names do not match. Which would you like to keep?"
        "[ddlc_persistent.playername]":
            $ persistent.playername = ddlc_persistent.playername
        "[persistent.playername]":
            $ persistent.playername
    return
