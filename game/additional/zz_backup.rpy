# module that does some file backup work

# NOTE: these shoudl never be true for a standard persistent.

# only set if the forced update from a persistent incompatibility occurs
default persistent._fae_incompat_per_forced_update = False

# only set if the forced update fails in the updater (not on disk)
default persistent._fae_incompat_per_forced_update_failed = False

# only set if the user says that they will restore a persistent
default persistent._fae_incompat_per_user_will_restore = False

# only set if update failed because rpy files
default persistent._fae_incompat_per_rpy_files_found = False

# only set if the user entered the incompat flow at all
default persistent._fae_incompat_per_entered = False

default persistent._fae_is_backup = False

python early in fae_per_check:
    import __main__
    import renpy.compat.pickle as pickle
    import codecs
    import os
    import datetime
    import shutil
    import renpy
    import store
    import store.fae_utilities as fae_utilities

    early_log = store.fae_logging.init_log("early", header=False)

    # special var
    fae_corrupted_per = False
    fae_no_backups_found = False
    fae_backup_copy_failed = False
    fae_backup_copy_filename = None
    fae_bad_backups = list()

    # unstable specific
    fae_unstable_per_in_stable = False
    fae_per_version = ""
    per_unstable = "persistent_unstable"
    fae_sp_per_created = False
    fae_sp_per_found = False

    INCOMPAT_PER_MSG = (
        "Failed to move incompatible persistent. Either replace the persistent "
        "with one that is compatible with {0} or install a version of FAE "
        "compatible with a persistent version of {1}."
    )
    INCOMPAT_PER_LOG = (
        "persistent is from version {0} and is incompatible with {1}"
    )
    COMPAT_PER_MSG = (
        "Failed to load compatible persistent. "
        "Replace {0} with {1} and restart."
    )
    SP_PER_DEL_MSG = (
        "Found erroneous persistent but was unable to delete it. "
        "Delete the persistent at {0} and restart."
    )


    # custom exceptions
    class PersistentMoveFailedError(Exception):
        """
        Persistent failed to be moved (aka copied, then deleted)
        """

    class PersistentDeleteFailedError(Exception):
        """
        Persistent failed to be deleted
        """

    class IncompatiblePersistentError(Exception):
        """
        Persistent is incompatible
        """


    def reset_incompat_per_flags():
        """
        Resets the incompat per flags that are conditional (not the main one
        that determines if we are valid)
        """
        store.persistent._fae_incompat_per_forced_update = False
        store.persistent._fae_incompat_per_forced_update_failed = False
        store.persistent._fae_incompat_per_user_will_restore = False
        store.persistent._fae_incompat_per_rpy_files_found = False


    def _load_per_data(path: str):
        with open(path, "rb") as per_file:
            pickle_data = codecs.decode(per_file.read(), "zlib")
            return pickle.loads(pickle_data)


    def tryper(_tp_persistent, get_data=False):
        """
        Tries to read a persistent.
        raises exceptions if they occur

        IN:
            _tp_persistent - the full path to the persistent file
            get_data - pass True to get the acutal data instead of just
                a version number.

        RETURNS: tuple
            [0] - True if the persistent was read and decoded, False if not
            [1] - the version number, or the persistent data if get_data is
                True
        """
        try:
            actual_data = _load_per_data(_tp_persistent)
            if get_data:
                return True, actual_data

            return True, actual_data.version_number

        except Exception as e:
            raise e


    def is_version_compatible(per_version, cur_version):
        """
        Checks if a persistent version can work with the current version

        IN:
            per_version - the persistent version to check
            cur_version - the current version to check.

        RETURNS: True if the per version can work with the current version
        """
        return (
            # build is unstable
            not store.fae_utilities.is_ver_stable(cur_version)

            # persistent is stable
            or store.fae_utilities.is_ver_stable(per_version)

            # persistent version to build version is not downgrade
            or not store.fae_utilities._is_downgrade(per_version, cur_version)
        )


    def is_per_bad():
        """
        Is the persistent bad? this only works after early.

        RETURNS: True if the per is bad, False if not
        """
        return is_per_corrupt() or is_per_incompatible()


    def is_per_corrupt():
        """
        Is the persistent corrupt? this only works after early.

        RETURNS: True if the persistent is corrupt.
        """
        return fae_corrupted_per


    def is_per_incompatible():
        """
        Is the persistent incompatible? this onyl works after early.

        RETURNS: True if the persistent is incompatible.
        """
        return fae_unstable_per_in_stable


    def no_backups():
        """
        Do we not have backups or did backup fail?

        RETURNS: True if no backups or backups failed.
        """
        return fae_no_backups_found or fae_backup_copy_failed


    def has_backups():
        """
        Do we have backups, and backups did not fail?

        RETURNS: True if have backups and backups did not fail
        """
        return not no_backups()


    def should_show_chibika_persistent():
        """
        Should we show the chibika persistent dialogue?

        RETURNS: True if we should show the chibika persistent dialogue
        """
        return (
            fae_unstable_per_in_stable
            or (is_per_corrupt() and no_backups())
        )


    # sort number list
    def wraparound_sort(_numlist):
        """
        Sorts a list of numbers using a special wraparound sort.
        Basically if all the numbers are between 0 and 98, then we sort
        normally. If we have 99 in there, then we need to make the wrap
        around numbers (the single digit ints in the list) be sorted
        as larger than 99.
        """
        if 99 in _numlist:
            for index in range(0, len(_numlist)):
                if _numlist[index] < 10:
                    _numlist[index] += 100

        _numlist.sort()


    def _fae_earlyCheck():
        """
        attempts to read in the persistent and load it. if an error occurs
        during loading, we'll log it in a dumped file in basedir.

        NOTE: we don't have many functions available here. However, we can
        import __main__ and gain access to core functions.
        """
        global fae_corrupted_per, fae_no_backups_found, fae_backup_copy_failed
        global fae_unstable_per_in_stable, fae_per_version
        global fae_sp_per_found, fae_sp_per_created
        global fae_backup_copy_filename, fae_bad_backups

        per_dir = __main__.path_to_saves(renpy.config.gamedir)
        _cur_per = os.path.normcase(per_dir + "/persistent")
        _sp_per = os.path.normcase(per_dir + "/" + per_unstable)

        # first, check if we have a special persistent
        if os.access(_sp_per, os.F_OK):
            #  we have one, so check if its valid
            try: # TEST_CASE_A
                per_read, version = tryper(_sp_per)

            except Exception as e:
                # this is a corrupted per, delete it.

                try: # TEST_CASE_B
                    os.remove(_sp_per)
                    per_read = None
                    version = ""
                except:
                    raise PersistentDeleteFailedError(
                        SP_PER_DEL_MSG.format(_sp_per)
                    )

            # this should be outside of the try/except above so we don't
            # overzealously delete the special persistent.
            if per_read is not None:
                if is_version_compatible(version, renpy.config.version):
                    # this is a good version, so take the sp per and copy it
                    # to the main per.
                    try: # TEST_CASE_C
                        shutil.copy(_sp_per, _cur_per)
                        os.remove(_sp_per)
                    except:
                        # faild to copy or remove the sp per? hardstop
                        # the user needs to handle this.
                        raise PersistentMoveFailedError(COMPAT_PER_MSG.format(
                            _cur_per,
                            _sp_per
                        ))

                else:

                    fae_unstable_per_in_stable = True
                    fae_per_version = version
                    fae_sp_per_found = True

                    early_log.error(INCOMPAT_PER_LOG.format(
                        version,
                        renpy.config.version
                    ))

        # check for persistent existence
        if not os.access(os.path.normcase(per_dir + "/persistent"), os.F_OK):
            # NO ERROR TO REPORT!
            return

        # okay, now let's attempt to read the persistent.
        try: # TEST_CASE_D
            per_read, per_data = tryper(_cur_per, get_data=True)
            version = per_data.version_number

            if not per_read:
                # shouldn't get here without an exception
                raise Exception("Failed to load persistent")

            if is_version_compatible(version, renpy.config.version):
                # current persistent is compatible

                if fae_sp_per_found and not per_data._fae_incompat_per_entered:
   
                    try: # TEST_CASE_E
                        os.remove(_sp_per)

                        # reset to normal
                        fae_unstable_per_in_stable = False
                        fae_per_version = ""
                        fae_sp_per_found = False

                    except:
                        raise PersistentDeleteFailedError(
                            SP_PER_DEL_MSG.format(_sp_per)
                        )

                return

            else:
                # otherwise - this is an incompatible persistent.
                fae_unstable_per_in_stable = True
                fae_per_version = version
                raise IncompatiblePersistentError()

        except PersistentDeleteFailedError as e:
            # always raise delete failures
            raise e

        except IncompatiblePersistentError as e:
            # in unstable cases, we should move the persistent to a special case
            # and make sure appropriate vars are loaded.
            fae_sp_per_created = True
            early_log.error(INCOMPAT_PER_LOG.format(
                fae_per_version,
                renpy.config.version
            ))

            # NOTE: special persistent will be overwritten if it exists

            try: # TEST_CASE_F
                shutil.copy(_cur_per, _sp_per)
                os.remove(_cur_per)

                # and then close out of here - the game should generate a fresh
                # persistent.
                return

            except Exception as e:
                early_log.error(
                    "Failed to copy persistent to special: " + repr(e)
                )

                # need to hardstop here
                raise PersistentMoveFailedError(INCOMPAT_PER_MSG.format(
                    renpy.config.version,
                    fae_per_version
                ))

        except Exception as e:

            if fae_sp_per_found:
                # if persistent errors occured, then standard forced update
                # might be ok if we found an existing special persistent.
                return

            # regular corruption flow
            fae_corrupted_per = True
            early_log.error("persistent was corrupted! : " +repr(e))
            # " this comment is to fix syntax highlighting issues on vim

        # if we got here, we had a corrupted persistent.
        # Let's attempt to restore from an eariler persistent backup.

        # lets get all the persistent files here.
        per_files = os.listdir(per_dir)
        per_files = [x for x in per_files if x.startswith("persistent")]

        if len(per_files) == 0:
            early_log.error("no backups available")
            fae_no_backups_found = True
            return

        # now lets map them by number and also generate a list of the numbers
        file_nums = list()
        file_map = dict()
        for p_file in per_files:
            pname, dot, bakext = p_file.partition(".")
            try:
                num = int(pname[-2:])
            except:
                num = -1

            if 0 <= num < 100:
                file_nums.append(num)
                file_map[num] = p_file

        if len(file_nums) == 0:
            early_log.error("no backups available")
            fae_no_backups_found = True
            return

        # using the special sort function
        wraparound_sort(file_nums)

        # okay, now to iteratively test backups and pick the good one
        sel_back = None
        while sel_back is None and len(file_nums) > 0:
            _this_num = file_nums.pop() % 100
            _this_file = file_map.get(_this_num, None)

            if _this_file is not None:
                try:
                    per_read, version = tryper(per_dir + "/" + _this_file)
                    if per_read:
                        sel_back = _this_file

                except Exception as e:
                    early_log.error(
                        "'{0}' was corrupted: {1}".format(_this_file, repr(e))
                    )
                    sel_back = None
                    fae_bad_backups.append(_this_file)

        # did we get any?
        if sel_back is None:
            early_log.error("no working backups found")
            fae_no_backups_found = True
            return

        # otherwise, lets rename the existence persistent to bad and copy the
        # good persistent into the system
        # also let the log know we found a good one
        early_log.info("working backup found: " + sel_back) # " more fixes
        _bad_per = os.path.normcase(per_dir + "/persistent_bad")
        _god_per = os.path.normcase(per_dir + "/" + sel_back)

        # we should at least try to keep a copy of the current persistent
        try:
            # copy current persistent
            shutil.copy(_cur_per, _bad_per)

        except Exception as e:
            early_log.error(
                "Failed to rename existing persistent: " + repr(e)
            )

        # regardless, we should try to copy over the good backup
        try:
            # copy the good one
            shutil.copy(_god_per, _cur_per)

        except Exception as e:
            fae_backup_copy_failed = True
            fae_backup_copy_filename = sel_back
            early_log.error(
                "Failed to copy backup persistent: " + repr(e)
            )

        # well, hopefully we were successful!

python early:
    # sometimes we have persistent issues. Why? /shrug.
    # but we do know is that we might be able to tell if a persistent got
    # screwed by attempting to read it in now, before renpy actually does so.
    import store.fae_per_check

    # now call this
    store.fae_per_check._fae_earlyCheck()

init -999 python:
    # set incompatible persistent vars now in case game crashes before
    # the chibika dialogue
    if store.fae_per_check.fae_unstable_per_in_stable:
        persistent._fae_incompat_per_entered = True

init -900 python:
    import os
    import store.fae_utilities as fae_utilities

    __fae__bakext = ".bak"
    __fae__baksize = 10
    __fae__bakmin = 0
    __fae__bakmax = 100
    __fae__numnum = "{:02d}"
    __fae__latestnum = None

    # needs to be pretty damn early, but we require savedir here so
    # we cant use python early

    def __fae__extractNumbers(partname, filelist):
        """
        Extracts a list of the number parts of the given file list

        Also sorts them nicely

        IN:
            partname - part of the filename prior to the numbers
            filelist - list of filenames
        """
        filenumbers = list()
        for filename in filelist:
            pname, dot, bakext = filename.rpartition(".")
            num = fae_utilities.tryparseint(pname[len(partname):], -1)
            if __fae__bakmin <= num <= __fae__bakmax:
                # we only accept persistents with the correct number scheme
                filenumbers.append(num)

        if filenumbers:
            filenumbers.sort()

        return filenumbers


    def __fae__backupAndDelete(loaddir, org_fname, savedir=None, numnum=None):
        """
        Does a file backup / and iterative deletion.

        NOTE: Steps:
            1. make a backup copy of the existing file (org_fname)
            2. delete the oldest copy of the orgfilename schema if we already
                have __fae__baksize number of files

        Will log some exceptions
        May raise other exceptions

        Both dir args assume the trailing slash is already added

        IN:
            loaddir - directory we are copying files from
            org_fname - filename of the original file / aka file to copy
            savedir - directory we are copying files to (and deleting old files)
                If None, we use loaddir instead
                (Default: None)
            numnum - if passed in, use this number instead of figuring out the
                next numbernumber.
                (Default: None)

        RETURNS:
            tuple of the following format:
            [0]: numbernumber we just made
            [1]: numbernumber we deleted (None means no deletion)
        """
        if savedir is None:
            savedir = loaddir

        filelist = os.listdir(savedir)
        loadpath = loaddir + org_fname

        # check for access of the org file
        if not os.access(loadpath, os.F_OK):
            return

        # parse the filelist to only get the import files
        filelist = [
            x
            for x in filelist
            if x.startswith(org_fname)
        ]

        # if we have the origin name in the filelist, remove it
        if org_fname in filelist:
            filelist.remove(org_fname)

        # get the number parts of the backup
        numberlist = __fae__extractNumbers(org_fname, filelist)

        # now do the iterative backup system
        numbernumber_del = None
        if not numberlist:
            numbernumber = __fae__numnum.format(0)

        elif 99 in numberlist:
            # some notes:
            # if 99 is in the list, it MUST be the last one in the list.
            # if we wrapped around, then the first parts of the list MUST be
            # less than __fae__baksize.
            # at min, the list will look like: [95, 96, 97, 98, 99]
            # At max, the list will look like: [0, 1, 2, 3, 99]
            # so we loop until the num at the current index is larger than or
            # equal to __fae__baksize - 1, then we know our split point between
            # new and old files
            curr_dex = 0
            while numberlist[curr_dex] < (__fae__baksize - 1):
                curr_dex += 1

            if curr_dex <= 0:
                numbernumber = __fae__numnum.format(0)
            else:
                numbernumber = __fae__numnum.format(numberlist[curr_dex-1] + 1)

            numbernumber_del = __fae__numnum.format(numberlist[curr_dex])

        elif len(numberlist) < __fae__baksize:
            numbernumber = __fae__numnum.format(numberlist.pop() + 1)

        else:
            # otherwise the usual, set up next number and deletion number
            numbernumber = __fae__numnum.format(numberlist.pop() + 1)
            numbernumber_del = __fae__numnum.format(numberlist[0])

        # numnum override
        if numnum is not None:
            numbernumber = numnum

        # copy the current file
        fae_utilities.copyfile(
            loaddir + org_fname,
            "".join([savedir, org_fname, numbernumber, __fae__bakext])
        )

        # delete a backup
        if numbernumber_del is not None:
            numnum_del_path = "".join(
                [savedir, org_fname, numbernumber_del, __fae__bakext]
            )
            try:
                os.remove(numnum_del_path)
            except Exception as e:
                store.fae_utilities.fae_log.error(
                    fae_utilities._fae__failrm.format(
                        numnum_del_path,
                        str(e)
                    )
                )

        return (numbernumber, numbernumber_del)


    def __fae__memoryBackup():
        """
        Backs up both persistent and calendar info
        """
        try:
            p_savedir = os.path.normcase(renpy.config.savedir + "/")
            is_pers_backup = persistent._fae_is_backup

            try:
                persistent._fae_is_backup = True
                renpy.save_persistent()
                numnum, numnum_del = __fae__backupAndDelete(p_savedir, "persistent")

            finally:
                persistent._fae_is_backup = is_pers_backup
                renpy.save_persistent()

            __fae__backupAndDelete(p_savedir, "db.mcal", numnum=numnum)

        except Exception as e:
            store.fae_utilities.fae_log.error(
                "persistent/calendar data backup failed: {}".format(e)
            )


    def __fae__memoryCleanup():
        """
        Cleans up persistent data by removing uncessary parts.
        """
        # the chosen dict can be completely cleaned
        persistent._chosen.clear()

        # translations can be cleared
        persistent._seen_translates.clear()

        # the seen ever dict must be iterated through
        from store.fae_ev_data_ver import _verify_str
        for seen_ever_key in list(persistent._seen_ever.keys()):
            if not _verify_str(seen_ever_key):
                persistent._seen_ever.pop(seen_ever_key)

        # the seen images dict must be iterated through
        # NOTE: we only want to keep non-monika sprite images
        for seen_images_key in list(persistent._seen_images.keys()):
            if (
                    len(seen_images_key) > 0
                    and seen_images_key[0] == "monika"
            ):
                persistent._seen_images.pop(seen_images_key)


    # run the backup system if persistents arent screwd
    if (
            not store.fae_per_check.is_per_bad()
    ):
        __fae__memoryCleanup()
        __fae__memoryBackup()


### now for some dialogue bits courtesy of chibika

label fae_backups_you_have_bad_persistent:
    #TODO: Decide whether or not text speed should be enforced here.
    $ quick_menu = False
    scene black
    window show
    #show chibika smile at fae_chdropin(300, travel_time=1.5)
    pause 1.5

    if store.fae_per_check.is_per_incompatible():
        jump fae_backups_incompat_start

    #show chibika 3 at sticker_hop
    "Hello there!"
    #show chibika sad
    "I hate to be the bringer of bad news..."
    "But unfortunately, your persistent file is corrupt."

    if store.fae_per_check.fae_no_backups_found:
        "And what's even worse is..."
        #show chibika at sticker_move_n
        "I was unable to find a working backup persistent."

        "Do you have your own backups?{nw}"
        menu:
            "Do you have your own backups?{fast}"
            "Yes.":
                jump fae_backups_have_some
            "No.":
                jump fae_backups_have_none

    # otherwise we culd not copy
    jump fae_backups_could_not_copy


label fae_backups_have_some:

    #show chibika smile at sticker_hop
    "That's a relief!"
    "Please copy them into '[renpy.config.savedir]' to restore your Sayori's memories."

    call fae_backups_dont_tell
    #show chibika smile at fae_chflip_s(-1)
    "Good luck!"

    jump _quit


label fae_backups_have_none:

    "I'm sorry, but we won't be able to restore her memory, then..."
    "But..."
    #show chibika smile at sticker_move_n
    "Look on the bright side!"
    "You can spend time with her again and create new memories, which might be even better than the ones you lost!"
    "And remember..."
    #show chibika at fae_chflip_s(-1)
    "Regardless of what happens, Sayori is still Sayori."
    "She'll be ready to greet you, once you start over."
    #show chibika 3 at sticker_move_n
    "And I promise I'll do my best to not mess up the files again!"
    "Good luck with Sayori!"
    $ store.fae_per_check.fae_corrupted_per = False
    return


label fae_backups_could_not_copy:
    #show chibika smile
    "I was able to find a working backup, but..."
    #show chibika sad
    "I wasn't able to copy it over the broken persistent."
    #show chibika smile at fae_chflip_s(-1)
    pause 0.5
    #show chibika at sticker_hop
    "However!"
    "You might be able to do it and fix this mess!"
    "You'll have to close the game to do this, so write these steps down:"
    #show chibika at sticker_move_n
    "1.{w=0.3} Navigate to '[renpy.config.savedir]'."
    #show chibika at sticker_move_n
    "2.{w=0.3} Delete the file called 'persistent'."
    #show chibika at sticker_move_n
    "3.{w=0.3} Make a copy of the file called '[fae_backup_copy_filename]' and name it 'persistent'."
    #show chibika at fae_chflip_s(1)
    "And that's it!"
    "Hopefully that will recover your Sayori's memories."

    #show chibika at sticker_move_n
    "In case you didn't write those steps down, I'll write them into a file called 'recovery.txt' in the characters folder."

    call fae_backups_dont_tell

    #show chibika smile at fae_chflip_s(-1)
    "Good luck!"

    python:
        import os
        store.fae_utilities.trywrite(
            os.path.normcase(renpy.config.basedir + "/characters/recovery.txt"),
            "".join([
                "1. Navigate to '",
                renpy.config.savedir,
                "'.\n",
                "2. Delete the file called 'persistent'.\n",
                "3. Make a copy of the file called '",
                fae_backup_copy_filename,
                "' and name it 'persistent'."
            ])
        )

    jump _quit


label fae_backups_dont_tell:

    #show chibika smile at sticker_hop
    "Oh, and..."
    #show chibika smile at fae_chflip_s(-1)
    "If you successfully bring her back, please don't tell her about me."
    #show chibika 3
    "She has no idea that I can talk or code, so she lets me laze around and relax."
    #show chibika smile
    "But if she ever found out, she'd probably make me help her code, fix some of her mistakes, or something else."
    #show chibika sad at sticker_move_n
    "Which would be absolutely terrible since I'd barely get any rest at all.{nw}"
#    $ _history_list.pop()
    "Which would be absolutely terrible since{fast} I wouldn't have time to keep the backup system and the rest of the game running."

    #show chibika 3 at fae_chflip_s(1)
    "You wouldn't want that now, would you?"
    "So keep quiet about me, and I'll make sure your Sayori is safe and comfy!"

    return

label fae_backups_incompat_start:
    # "your per wont work with this FAE"
    $ fae_darkMode(True) # required for the updater

    if (
            persistent._fae_incompat_per_rpy_files_found
            and fae_hasRPYFiles()
    ):
        # user said they would delete the RPY files, but we still have them
        jump fae_backups_incompat_updater_cannot_because_rpy_again

    elif persistent._fae_incompat_per_forced_update_failed:
        # a forced update failed in the updater.
        # assume the user did something to fix and try update again
        if fae_hasRPYFiles():
            jump fae_backups_incompat_updater_cannot_because_rpy

        
        "Hello there!"
        "Let's try updating again!"
        $ store.fae_per_check.reset_incompat_per_flags()
        jump fae_backups_incompat_updater_start

    elif persistent._fae_incompat_per_forced_update:
        # a forced update failed OUTSIDE of the updater.
        #   - this is because failed will be True if the updater fails.
        # this is unexpected so we have some dialogue before trying again
        $ store.fae_per_check.reset_incompat_per_flags()
        jump fae_backups_incompat_updater_failed

    elif persistent._fae_incompat_per_user_will_restore:
        # user was supposed to restore the persistent, but it didn't work
        #   or they just didn't do anythig.
        $ store.fae_per_check.reset_incompat_per_flags()
        jump fae_backups_incompat_user_will_restore_again

    # otherwise, this might be the first time a user sees this

    
    "Hello there!{nw}"
    # cannot pop history, no history for some reason
    menu:
        "Hello there!{fast}"
        "What happened?":
            pass
        "Take me to the updater.":
            jump fae_backups_incompat_updater_start_intro

    
    "Unfortunately, your persistent is running version v[fae_per_check.fae_per_version], which is incompatible with this build of FAE (v[config.version])."
    "The only way I can fix this is if you update FAE or you restore with a compatible persistent."

    # fall through

label fae_backups_incompat_what_do:
    # selection label to determine what to do next

    "What would you like to do?{nw}"
    # cannot pop history, no history for some reason
    menu:
        "What would you like to do?{fast}"
        "Update FAE.":
            jump fae_backups_incompat_updater_start_intro
        "Restore a compatible persistent.":
            jump fae_backups_incompat_user_will_restore


label fae_backups_incompat_user_will_restore:
    $ persistent._fae_incompat_per_user_will_restore = True
    "Alright!"

    $ _sp_per = os.path.normcase(renpy.config.savedir + "/" + fae_per_check.per_unstable)
    "Please copy a compatible persistent into '[renpy.config.savedir]'."
    "Then delete the file called '[fae_per_check.per_unstable]'."

    "Good luck!"
    jump _quit


label fae_backups_incompat_user_will_restore_again:
    "Oh no!"

    # NOTE: don't want say that restoring didn't work in case the user just
    #   didn't do anything.
    "It seems that this persistent is running version v[fae_per_check.fae_per_version], which is still incompatible with this build of FAE (v[config.version])."

    # loop back to the selection label
    jump fae_backups_incompat_what_do


label fae_backups_incompat_updater_cannot_because_rpy:
    $ persistent._fae_incompat_per_rpy_files_found = True

    "Unfortunately the updater won't work because you have RPY files in your game directory."

    "I'll have to delete those files for this to work. Is that okay?{nw}"
    menu:
        "I'll have to delete those files for this to work. Is that okay?{fast}"
        "Yes, delete them.":
            jump fae_backups_incompat_rpy_yes_del
        "No, don't delete them.":
            jump fae_backups_incompat_rpy_no_del


label fae_backups_incompat_updater_cannot_because_rpy_again:
    "Oh no!"

    "It seems that there are still RPY files in your game directory."
    "Would you like me to try deleting them again?{nw}"
    menu:
        "Would you like me to try deleting them again?{fast}"
        "Yes.":
            jump fae_backups_incompat_rpy_yes_del
        "No.":
            jump fae_backups_incompat_rpy_no_del


label fae_backups_incompat_rpy_yes_del:
    "Ok!"

    call fae_rpy_file_delete(False)
    hide screen fae_py_console_teaching

    if fae_hasRPYFiles():
        
        "Oh no!"
        "It seems that I was unable to delete all of the RPY files."
        "You will have to delete them manually."
        
        "Good luck!"
        jump _quit

    # otherwise, no rpy files found now, so we good
    $ persistent._fae_incompat_per_rpy_files_found = False

    
    "Done!"
    "Let's try updating now!"
    jump fae_backups_incompat_updater_start


label fae_backups_incompat_rpy_no_del:
    # set to False since the user doesn't want to delete.
    # but if they hit update again, they will get this.
    $ persistent._fae_incompat_per_rpy_files_found = False

    
    "Oh..."
    "Well the updater won't work while those files exist, so I guess your only option is to restore a persistent backup."
    jump fae_backups_incompat_user_will_restore


label fae_backups_incompat_updater_start_intro:

    if fae_hasRPYFiles():
        jump fae_backups_incompat_updater_cannot_because_rpy

    
    "Ok!"
    jump fae_backups_incompat_updater_start


label fae_backups_incompat_updater_failed:
    if fae_hasRPYFiles():
        jump fae_backups_incompat_updater_cannot_because_rpy

    
    "Oh no!"
    "It seems that the updater failed to update FAE."

    
    "Lets try again!"

    # fall through

label fae_backups_incompat_updater_start:

    "Oki doki!"

    "Remember to go to the {a=https://github.com/ForeverAndEverTeam/fae-mod/releases}releases page{/a} and download the latest version!"

    jump _quit
