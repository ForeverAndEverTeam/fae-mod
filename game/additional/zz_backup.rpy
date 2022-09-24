default persistent._fae_incompat_per_forced_update = False

default persistent._fae_incompat_per_forced_update_failed = False

default persistent._fae_incompat_per_user_will_restore = False

default persistent._fae_incompat_per_rpy_file_found = False

default persistent._fae_incompat_per_entered = False

python early in fae_per_checker:

    import __main__
    import pickle
    import codecs
    import os
    import datetime
    import shutil
    import renpy
    import store
    import store.fae_utilities as fae_utilities

    early_log = store.fae_logging.init_log("early", header=False)

    fae_corrupted_per = False
    fae_no_backups_found = False
    fae_backup_copy_failed = False
    fae_backup_copy_filename = None
    fae_bad_backups = list()

    fae_unstable_per_in_stable = False
    fae_per_version = ""
    per_unstable = "persistent_unstable"
    fae_sp_per_created = False
    fae_sp_per_found = False


    INCOMPAT_PER_MSG = (
        "Fialed to move incompatible persistent. Either replace the persistent "
        "with one that is compatible with {0} or install a version of FAE "
        "compatible with a persistent version of {1}."
    )
    INCOMPAT_PER_LOG = (
        "Failed to load compatible persistent. "
        "Replace {0} with {1} and restart."
    )

    SP_PER_DEL_MSG = (
        "Found erroneous persistent but was unable to delete it. "
        "Delete the persistent found at {0} and restart."
    )


    class PersistentMoveFailedError(Exception):
        """
        Peristent failed to be moved (aka copied, then deleted)
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

        store.persistent._fae_incompat_per_forced_update = False
        store.persistent._fae_incompat_per_forced_update_failed = False
        store.persistent._fae_incompat_per_user_will_restore = False
        store.persistent._fae_incompat_per_rpy_file_found = False

    def tryper(_tp_persistent, get_data=False):

        per_file = None
        try:
            per_file = open(_tp_persistent, "rb")
            per_data = codecs.decode(per_file.read(), "zlib")
            per_file.close()
            actual_data = pickle.loads(per_data)

            if get_data:
                return True, actual_data
        
        except Exception as e:
            raise e
        
        finally:
            if per_file is not None:
                per_file.close()
        
    
    def is_version_compatible(per_version, cur_version):

        return (
            not store.fae_utilities.is_ver_stable(cur_version)

            or store.fae_utilities.is_ver_stable(per_version)

            or not store.fae_utilities._is_downgrade(per_version, cur_version)
        )
    

    def is_per_bad():

        return is_per_corrupt()
    

    def is_per_corrupt():

        return fae_corrupted_per


    def no_backups():

        return fae_no_backups_found or fae_backup_copy_failed
    
    def has_backups():

        return not no_backups()

    
    def should_show_persistent_dialogue():

        return (
            is_per_corrupt() and no_backups()
        )

    
    def wraparound_sort(_numlist):

        if 99 in _numlist:
            for index in range(0, len(_numlist)):
                if _numlist[index] < 10:
                    _numlist[index] += 100
        _numlist.sort()

    
    def _fae_earlyCheck():


        global fae_corrupted_per, fae_no_backups_found, fae_backup_copy_failed

        global fae_sp_per_found, fae_sp_per_created
        global fae_backup_copy_filename, fae_bad_backups

        per_dir = __main__.path_to_saves(renpy.config.gamedir)
        _cur_per = os.path.normcase(per_dir + "/persistent")
        _sp_per = os.path.normcase(per_dir + "/" + per_unstable)

        if os.access(_sp_per, os.F_OK):

            try:
                per_read, version = tryper(_sp_per)

            except Exception as e:
                try:
                    os.remove(_sp_per)
                    per_read = None
                    version = ""
                except:
                    raise PersistentDeleteFailedError(
                        SP_PER_DEL_MSG.format(_sp_per)
                    )
            
            if per_read is not None:
                if is_version_compatible(version, renpy.config.version):

                    try:
                        shutil.copy(_sp_per, _cur_per)
                        os.remove(_sp_per)
                    except:

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
        
        if not os.access(os.path.normcase(per_dir + "/persistent"), os.F_OK):

            return
        
        try:
            per_read, per_data = tryper(_cur_per, get_data=True)
            version = per_data.version_number

            if not per_read:

                raise Exception("Failed to load persistent")

            if is_version_compatible(version, renpy.config.version):

                if fae_sp_per_found and not per_data._fae_incompat_per_entered:

                    try:
                        os.remove(_sp_per)

                        fae_unstable_per_in_stable = False
                        fae_per_version = ""
                        fae_sp_per_found = False
                    
                    except:
                        raise PersistentDeleteFailedError(
                            SP_PER_DEL_MSG.format(_sp_per)
                        )

                    
                return
            
            else:
                fae_unstable_per_in_stable = True
                fae_per_version = version

                raise IncompatiblePersistentError()
            
        except PersistentDeleteFailedError as e:
            raise e
        
        except IncompatiblePersistentError as e:

            fae_sp_per_created = True
            early_log.error(INCOMPAT_PER_LOG.format(
                fae_per_version,
                renpy.config.version
            ))


            try:

                shutil.copy(_cur_per, _sp_per)
                os.remove(_cur_per)

                return
            
            except Exception as e:
                early_log.error(
                    "Failed to copy persistent to special: " + repr(e)
                )

                raise PersistentMoveFailedError(INCOMPAT_PER_MSG.format(
                    renpy.config.version,
                    fae_per_version
                ))

        except Exception as e:

            if fae_sp_per_found:

                return
            
            fae_corrupted_per = True
            early_log.error("Peristent was corrupted! : " + repr(e))

        
        per_files = os.listdir(per_dir)
        per_files = [x for x in per_files if x.startswith("persistent")]

        if len(per_files) == 0:
            early_log.error("no backups found")
            fae_no_backups_found = True
            return
        

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
        
        wraparound_sort(file_nums)

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
        
        if sel_back is None:

            early_log.error("No working backups found")
            fae_no_backups_found = True
            return
        

        early_log.info("Working backup found: " + sel_back)
        _bad_per = os.path.normcase(per_dir + "/persistent_bad")
        _god_per = os.path.normcase(per_dir + "/" + sel_back)

        try:

            shutil.copy(_cur_per, _bad_per)
        
        except Exception as e:
            early_log.error(
                "failed to rename existing persistent: " + repr(e)
            )

        
        try:
            shutil.copy(_god_per, _cur_per)
        
        except Exception as e:

            fae_backup_copy_failed = True
            fae_backup_copy_filename = sel_back
            early_log.error(
                "Failed to copy backup persistent: " + repr(e)
            )


python early:

    import store.fae_per_checker

    #store.fae_per_checker._fae_earlyCheck()

init -999 python:

    if store.fae_per_checker.fae_unstable_per_in_stable:
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

    def __fae__extractNumbers(partname, filelist):

        filenumbers = list()
        for filename in filelist:
            pname, dot, bakext = filename.rpartition(".")
            num = fae_utilities.tryparseint(pname[len(partname):], -1)
            if __fae__bakmin <= num <= __fae__bakmax:

                filenumbers.append(num)
        
        if len(filenumbers) > 0:
            return sorted(filenumbers)
        
        return []

    
    def __fae__backupAndDelete(loaddir, org_fname, savedir=None, numnum=None):

        if savedir is None:
            savedir = loaddir
        
        filelist = os.listdir(savedir)
        loadpath = loaddir + org_fname

        if not os.access(loadpath, os.F_OK):
            return
        
        filelist = [
            x
            for x in filelist
            if x.startswith(org_fname)
        ]

        if org_fname in filelist:
            filelist.remove(org_fname)
        
        numberlist = __fae__extractNumbers(org_fname, filelist)

        numbernumber_del = None
        if len(numberlist) <= 0:
            numbernumber = __fae__numnum.format(0)
        
        elif 99 in numberlist:


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
            numbernumber = __fae__numnum.format(numberlist.pop() + 1)
            numbernumber_del = __fae__numnum.format(numberlist[0])
        
        if numnum is not None:
            numbernumber = numnum
        
        fae_utilities.copyfile(
            loaddir + org_fname,
            "".join([savedir, org_fname, numbernumber, __fae__bakext])
        )

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

        try:
            p_savedir = os.path.normcase(renpy.config.savedir + "/")
            p_name = "persistent"
            numnum, numnum_del = __fae__backupAndDelete(p_savedir, p_name)
            cal_name = "db.mcal"
            __fae__backupAndDelete(p_savedir, cal_name, numnum=numnum)
        
        except Exception as e:
            store.fae_utilities.fae_log.error(str(e))
        
    
    def __fae__memoryCleanup():

        persistent._chosen.clear()

        persistent._seen_translates.clear()

        if (
            not store.fae_per_checker.is_per_bad()
        ):
            __fae__memoryCleanup()
            __fae__memoryBackup()


label fae_backups_bad_persistent:

    "You have bad persistent."

    if store.fae_per_checker.fae_no_backups_found:
        "And there's now workign backups"

        "Do you have backups?{nw}"

        menu:
            "Do you have backups?{fast}"
            "Yes":
                jump fae_backups_have_some
            "No":
                jump fae_backups_have_none
        
    jump fae_backups_could_not_copy


label fae_backups_have_some:

    "That's a relif!"
    "Put them into '[renpy.config.savedir]' to restore Sayori's memories."

    call fae_backups_dont_tell from _call_fae_backups_dont_tell

    "Good luck!"

    jump _quit


label fae_backups_have_none:

    "Well we cant restore her memory."
    "But you''l be able to make more memories"
    "Good luck!"

    $ store.fae_per_checker.fae_corrupted_per = False

    return


label fae_backups_could_not_copy:

    "I found a working persistent."
    "But I can't copy it over the broken one."

    "You might be able to fix it!"
    "1. Navigate to '[renpy.config.savedir]'."
    "2.{w=0.3} Delete the file called 'persistent'."
    "3.{w=0.3} Make a copy of the file called '[fae_backup_copy_filename]' and name it 'persistent'."

    "And that's it."

    "In case you missed it, I'll make text file with the steps for you."

    python:
        import os
        store.fae_utilities.trywrite(
            os.path.normcase(renpy.config.basedir + "/character/recovery.txt"),
            "".join([
                "1. Navigate to '",
                renpy.config.savedir,
                "'.\n",
                "2. Delete the file caled 'persistent'.\n",
                "3. Make a copy of the file called '",
                fae_backup_copy_filename,
                "' and name it 'persistent'."
            ])
        )
    
    jump _quit


label fae_backups_dont_tell:

    "Oh and..."

    "If you bring her back, don't tell her about me."
    return





    