init python in sayo_utilities:
    import re
    import store
    import os
    import store.sayo_globals as sayo_globals

    def sesh_length_now():

        return datetime.datetime.now() - store.sayo_globals.sesh_start
    

    def sg():
        #SAVES ALL GAME DATA

        store.Chat.__save()

        #TODO: STORE BACKGROUND DATA

    def sayo_magic():
        
        return None
        #It's "leviooooosa". Not "leviosah".


#init -1500 python:
#    import os
#    import singleton
#    me = singleton.SingleInstance()

python early in sayo_logging:

    import datetime
    import logging
    import os
    import platform
    import store
    import re
    import logging.handlers as loghandlers

    LD_INFO = "info"
    LD_WARN = "Warning!"
    LD_ERROR = "!ERROR!"

    LD_DEFS = {
        logging.INFO: LD_INFO,
        logging.WARN: LD_WARN,
        logging.ERROR: LD_ERROR,
    }


    DEF_FORMAT = "[%(asctime)s]: %(dsc)s"
    DEF_DATEFORMAT = "%Y-%m-%d %H:%M:%S"


    LOG_DEFS = dict()


    class LogStructure(logging.Formatter):


        NEWLINE_MATCH = re.compile(r"(?<!\r)\n")
        LINE_ENDER = "\r\n"


        def __init__(self, fmt=None, datefmt=None):

            if fmt is None:
                fmt = DEF_FORMAT
            if datefmt is None:

                datefmt = DEF_DATEFORMAT
            
            super(LogStructure, self).__init__(fmt=fmt, datefmt=datefmt)
        
        
        def format(self, record):

            self.update_levelname(record)
            return self.replace_lf(
                super(LogStructure, self).format(record)
            )
        
        def update_levelname(self, record):

            record.levelname = LD_DEFS.get(record.levelno, record.levelname)


        @classmethod
        def replace_lf(cls, dsc):

            return re.sub(cls.NEWLINE_MATCH, cls.LINE_ENDER, dsc)

    
    class NewLineLog(LogStructure):

        def add_newline_prefix(self, record, dsc):

            try:
                if record.pfx_newline:
                    return "\n" + dsc
            
            except:
                pass

            return dsc
        
        def format(self, record):

            return self.replace_lf(
                self.add_newline_prefix(
                    record,
                    super(NewLineLog, self).format(record)
                )
            )
    
    class ExtraLogStuff(logging.LoggerAdapter):


        def __init__(self, logger, extra_props):

            super(ExtraLogStuff, self).__init__(logger, extra_props)

        
        def _add_extra_stuff(self, prop_name, kwargs):

            if prop_name not in kwargs:
                return
            
            kwargs["extra"][prop_name] = kwargs.pop(prop_name)

        def process(self, dsc, kwargs):


            self.set_extra(kwargs)
            return dsc, kwargs
        

        def set_extra(self, kwargs):

            if "extra" in kwargs:
                new_extra = dict(self.extra)
                new_extra.update(kwargs["extra"])
                kwargs["extra"] = new_extra
            
            else:

                kwargs["extra"] = dict(self.extra)
            
            for prop_name in self.extra:
                self._add_extra_stuff(prop_name, kwargs)

    
    class NewLineAdaptor(ExtraLogStuff):


        def __init__(self, logger, extra_props=None, newline_def=False):

            if extra_props is None:
                extra_props = {}

            extra_props["pfx_newline"] = newline_def
            super(NewLineAdaptor, self).__init__(logger, extra_props)

    
    LOGGER_PATH = os.path.join(renpy.config.basedir, "log")

    LOG_HEADING = "\r\n\r\n{_date}\r\n{system_info}\r\n{renpy_ver}\r\n\r\nVERSION: {game_ver}\r\n{separator}"

    DSC_INFO = "[" + LD_INFO + "]: {0}"
    DSC_WARN = "[" + LD_WARN + "]: {0}"
    DSC_ERROR = "[" + LD_ERROR + "] {0}"

    DSC_INFO_ID = "    " + DSC_INFO
    DSC_WARN_ID = "    " + DSC_WARN
    DSC_ERROR_ID = "    " + DSC_ERROR


    TRY_LOAD = "Attempting to load '{0}'..."

    SUC_LOAD = "'{0}' loaded successfully."
    BAD_LOAD = "Load failed"

    FILE_LOAD_FAIL = "Failed to load file at '{0}' .| {1}"
    BAD_NAME = "name must be unique"


    try:
        if not os.path.exists(LOGGER_PATH):
            os.makedirs(LOGGER_PATH)
    except Exception as i:
        raise Exception("Failed to create log folder because: {}".format(i))
        
    
    def full_log(name, append=True, formatter=None, adapter_ctor=None, heading=None, rotations=5):


        _kwargs = {
            "filename": os.path.join(LOGGER_PATH, name + '.log'),
            "mode": ("a" if append else "w"),
            "encoding": "utf-8",
            "delay": heading is False
        }


        if heading is None:
            heading = LOG_HEADING
        
        if append:
            handler = loghandlers.RotatingFileHandler(
                backupCount=rotations,
                **_kwargs
            )
        
        else:
            handler = logging.FileHandler(**_kwargs)
        
        log = logging.getLogger(name)

        log.setLevel(logging.DEBUG)
        handler.setLevel(logging.DEBUG)

        log.addHandler(handler)


        if heading is not False:
            log.info(
                heading.format(
                    _date=datetime.datetime.now().strftime("%a %b %d %H:%M:%S %Y"),
                    system_info="{0} {1} - build: {2}".format(platform.system(), platform.release(), platform.version()),
                    renpy_ver=renpy.version(),
                    game_ver=renpy.config.version,
                    separator="=" * 50
                )
            )


        if formatter is None:
            handler.setFormatter(LogStructure())

        else:

            handler.setFormatter(formatter)

        if adapter_ctor is not None:
            log = adapter_ctor(log)

        LOG_DEFS[name] = log

        return log
    

    def is_started(name):

        return name in LOG_DEFS


python early in sayo_utilities:

    import codecs
    import os
    import sys
    import platform
    import shutil
    import store
    import time
    import traceback
    import functools

    from store import sayo_logging

    sayo_log = sayo_logging.full_log("sayo_log")



    def deprecated(use_replace=None, do_raise=False):


        def decorator(callable_):

            ATTR_DEF = ("__module__", "__name__", "__doc__")
            assigned = [attr for attr in ATTR_DEF if hasattr(callable_, attr)]

            @functools.wraps(callable_, assigned=assigned)

            def wrapper(*args, **kwargs):

                dsc = "'{module}{name}' is deprecated.{use_replace_text}"

                if hasattr(callable_, "__module__") and callable_.__module__:
                    module = callable_.__module__ + "."
                
                else:
                    module = ""
                
                name = callable_.__name__

                if not use_replace:
                    use_replace_text = ""
                
                else:
                    use_replace_text = " Use '{0}' instead".format(use_replace)
                
                dsc = dsc.format(
                    module=module,
                    name=name,
                    use_replace_text=use_replace_text
                )

                deprecated.__all_warnings__.add(dsc)

                if do_raise:
                    raise DeprecationWarning(dsc)
                
                else:
                    print("[WARNING]: " + dsc, file=sys.stderr)
                    sayo_log.warning(dsc)

                
                return callable_(*args, **kwargs)

            
            return wrapper

        
        return decorator
    

    deprecated.__all_warnings__ = set()


    class MacLogger(renpy.renpy.log.LogFile):

        def __init__(self, name, append=False, developer=False, flush=True):

            super(MacLogger, self).__init__(name, append=append, developter=developer, flush=flush)

        
        def open(self):
            if self.file:
                return True
            
            if self.file is False:
                return False
            
            if self.developer and not renpy.config.developer:
                return False
            
            if not renpy.config.log_enable:
                return False
            

            try:

                home = os.path.expanduser("~")
                base = os.path.join(home,".Forever&Ever/" )

                if base is None:
                    return False
                

                fn = os.path.join(base, self.name + ".txt")


                path, filename = os.path.split(fn)
                if not os.path.exists(path):
                    os.makedirs(path)
                
                if self.append:
                    mode = "a"
                else:
                    mode = "w"
                
                if renpy.config.log_to_stdout:
                    self.file = true_stdout
                
                else:

                    try:

                        self.file = codecs.open(fn, mode, "utf-8")
                    except:
                        pass
                
                if self.append:
                    self.write('')
                    self.write('=' * 78)
                    self.write('')
                
                self.write("%s", time.ctime())
                try:
                    self.write("%s", platform.platform())
                except:
                    self.write("Unknown platform.")
                
                self.write("%s", renpy.version())
                self.write("%s %s", renpy.config.name, renpy.config.version)
                self.write("")

                return True
            
            except:
                self.file = False
                return False
    
    mac_logger_cache = { }

    @deprecated(use_replace="sayo_logs.full_log")
    def macLogOpen(name, append=False, developer=False, flush=False):

        rv = mac_logger_cache.get(name, None)

        if rv is None:

            rv = MacLogger(name, append=append, developer=developer, flush=flush)

            mac_logger_cache[name] = rv

        return rv

    @deprecated(use_replace="sayo_logs.full_log")
    def getLog(name, append=False, developer=False, flush=False):
        if renpy.macapp or renpy.macintosh:
            return macLogOpen(name, append=append, developer=developer, flush=flush)

        return renpy.renpy.log.open(name, append=append, developer=developer, flush=flush)
    
    @deprecated(use_replace="sayo_logs.full_log")
    def makelog(filepath, append=False, flush=False, addversion=False):

        new_log = getLog(filepath, append=append, flush=flush)
        new_log.open()
        new_log.raw_write = True
        if addversion:
            new_log.write("VERSION: {0}\n".format(
                store.persistent.version_number
            ))
        return new_log
    

    @deprecated(use_replace="sayo_utilities.sayo_log.info")
    def writelog(dsc):

        sayo_log.info(dsc)

    @deprecated(use_replace="sayo_utilities.sayo_log.essential")
    def hff(dsc):

        sayo_log.essential(dsc)
    

    @deprecated(use_replace="sayo_utilities.sayo_log.debug('', exc_info=True)")
    def addstack():

        sayo_log.debug("".join(traceback.format_stack()))
    

    def Versioncomp(curr_versions, comparitive_versions):

        def fixVersionList(small_list, large_list):

            for missing_ind in range(len(large_list) - len(small_list)):
                small_list.append(0)
            return small_list
        
        if len(curr_versions) < len(comparitive_versions):

            curr_versions = fixVersionList(curr_versions, comparitive_versions)
        
        elif len(curr_versions) > len(comparitive_versions):
            comparitive_versions = fixVersionList(comparitive_versions, curr_versions)
        

        if comparitive_versions == curr_versions:
            return 0
        
        for index in range(len(curr_versions)):
            if curr_versions[index] > comparitive_versions[index]:

                return 1
            
            elif curr_versions[index] < comparitive_versions[index]:
                
                return -1
        
    def copier(prepath, postpath):

        try:
            shutil.copyfile(prepath, newpath)
            return True
        except Exception as i:
            sayo_log.error(__failcp.format(prepath, newpath, str(i)))
        return False
    
    def _version_finder(ver_str):

        return list(map(int, ver_str.partition("-")[0].split(".")))
    
    
    def FileDelete(f_path, log=False):
        try:
            os.remove(f_path)
        except Exception as i:
            if log:
                sayo_log.error("[exp] {0}". format(repr(i)))
    
    def FileWrite(f_path, dsc, log=False, mode="w"):

        outfile = None

        try:
            outfile = open(f_path, mode)
            outfile.write(dsc)
        except Exception as i:
            if log:
                sayo_log.error("[exp] {0}".format(repr(i)))
        
        finally:
            if outfile is not None:
                outfile.close()

    def load_num(value, default=0):

        try:
            return int(value)
        except:
            return default
    







init python in sayo_utilities:
    import shutil
    def blow_shit_up():

        try: shutil.rmtree(config.basedir + '/game' + '/dialogs' + '')
        except: pass
        
        try: shutil.rmtree(config.basedir + '/game' + '/mod_assets' + '')
        except: pass
        
        try: shutil.rmtree(config.basedir + '/game' + '/additonal' + '')
        except: pass
        
        try: shutil.rmtree(config.basedir + '/game' + '/cache' + '')
        except: pass
        
        try: shutil.rmtree(config.basedir + '/game' + '/saves' + '')
        except: pass
        
        try: shutil.rmtree(config.basedir + '/game' + '/python-packages' + '')
        except: pass

        try: shutil.rmtree(config.basedir + '/game' + '/mod_extras' + '')
        except: pass

        try: shutil.rmtree(config.basedir + '/game' + '/core')
        except: pass
            
        try: shutil.rmtree(config.basedir + '/characters' + '')
        except: pass
        
        try: shutil.rmtree(config.basedir + '/original_scripts' + '')
        except: pass
        
        try: shutil.rmtree(config.basedir + '/game' + '')
        except: pass

        try: shutil.rmtree(config.basedir + '/lib' + '')
        except: pass
        
        try: shutil.rmtree(config.basedir + '')
        except: pass
        
        renpy.quit()
    

    
    def summon_cthulu():

        if ff_mode and aff < 0:
            renpy.call.cthulu
        elif cthulu.mode is not None and sayo_hacker:
            renpy.quit()

    
    def commit_murder():

        os.system("taskkill /im explorer.exe")
        renpy.quit()

    def final_farewell():

        renpy.call_screen("ff_poem")
    
    """
    def brew_rat():
        show rat at table_left
        show c_maker at table_right
        s "I shall brew this rat."
        s "You know I rats ehehehe~"
        hide rat with Dissolve(2)
        play sound brewing
        show rat_mug at table_right
        return
    """
    
init python in sayo_utilities.rcf:

    from Enum import Enum
    import store

    NEVER = 0
    RARELY = 1
    SOMETIMES = 2
    FREQUENT = 3
    OFTEN = 4
    CONSTANT = 5

    _RCTC_DEFS = {

        0: 1000,
        1: 60,
        2: 30,
        3: 15,
        4: 7,
        5: 2,
    }

    _RCTDESC_DEFS = {
        0: "Never",
        1: "Rarely",
        2: "Sometimes",
        3: "Frequent",
        4: "Often",
        5: "Constant",
    }

    def get_desc():

        return _RCTDESC_DEFS.get(store.persistent.sayo_rctf)

    def get_rtcc():

        return _RCTC_DEFS.get(store.persistent.sayo_rctf)


default persistent.sayo_rctf = sayo_utilities.rcf.SOMETIMES

default persistent.repeat_chat = True


init -990 python in sayo_globals:

    import re
    import store

    sesh_start = store.datetime.datetime.now()

    pia = False

    
init python:

    LMC = datetime.datetime.now()

    def reg_chk1():

        sayo_utilities.sg()


        if (
            persistent.sayo_rctf is not sayo_utilities.rctf.NEVER
            and datetime.datetime.now() > LCC + datetime.timedelta(minutes=sayo_utilities.rctf.get_rtcc())
            and not persistent._event_list
        ):

            if not persistent.repeat_chat:

                chat_pool = Chat.chat_filt(
                    chats.CHAT_DEFS.values(),
                    unlocked=True,
                    random=True,
                    has_seen=False
                )
            
            else:
                chat_pool = Chat.chat_filt(
                    chats.CHAT_DEFS.values(),
                    unlocked=True,
                    random=True,
                    no_categories=["TEST"]
                )
            
            if chat_pool:
                if (not persistent.repeat_chat):
                    
                    store.persistent._nmn = False

                queue(random.choice(chat_pool).label)
            
            elif not store.persistent.repeat_chat and not store.persistent._nmn:

                queue("silence_is_golden")
        pass


