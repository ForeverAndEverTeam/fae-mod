python early in fae_logging:
    import datetime
    import logging
    import os
    import platform
    import store
    import re

    import logging.handlers as loghandlers


    LT_INFO = "info"
    LT_WARN = "Warning"
    LT_ERROR = "ERROR"

    LT_DEFS = {
        logging.INFO: LT_INFO,
        logging.WARN: LT_WARN,
        logging.ERROR: LT_ERROR,
    }

    DEF_FMT = "[%(asctime)s] [%(levelname)s]: %(message)s"

    DEF_DATEFMT = "%Y-%m-%d %H:%M:%S"

    LOG_DEF = dict()

    class FAELogFormatter(logging.Formatter):

        NEWLINE_MATCHER = re.compile(r"(?<!\r)\n")
        LINE_TERMINATOR = "\r\n"

        def __init__(self, fmt=None, datefmt=None):

            if fmt is None:
                fmt = DEF_FMT
            
            if datefmt is None:
                datefmt = DEF_DATEFMT
            
            super().__init__(fmt=fmt, datefmt=datefmt)
        
        def format(self, record):

            """
            Levelname replacement
            """
            self.update_levelname(record)

            return super().format(record)

        def update_levelname(self, record):

            """
            Updates levelname
            """
            record.levelname = LT_DEFS.get(record.levelno, record.levelname)

    
    class FAENewlineLogFormatter(FAELogFormatter):

        """
        Formatter with prefix support for newline
        """

        def apply_newline_prefix(self, record, msg):

            """
            Adds newline to message if the record supports it.

            FEED:
                record: Item to add format to
                msg: Message
            
            RESULT:
                message with newline
            """
            try:
                if record.pfx_newline:
                    return "\n" + msg
            except:
                pass
            return msg

        def format(self, record):
            """
            Adds newline prefix
            """
            return self.apply_newline_prefix(
                record,
                super().format(record)
            )
    
    class FAEExtraPropLogAdapter(logging.LoggerAdapter):

        """
        Allows default of poperties on LogRecord items

        DEFS:
            extra_props: dict of user properties with def values
        """

        def __init__(self, logger, extra_props):
            """
            FEED:
                logger: logger to adapt
                extra_props:
                    key: name of property
                    value: def val
            """
            super(FAEExtraPropLogAdapter, self).__init__(logger, extra_props)
        
        def _add_extra_prop(self, prop_name, kwargs):

            """
            Adds a property from the args to the extra args

            FEED:
                prop_name: name of property to find from args
                kwargs: property data (if present)
            RESULT:
                kwargs: property data moved if present
            """

            if prop_name not in kwargs:
                return

            kwargs["extra"][prop_name] = kwargs.pop(prop_name)
        
        def process(self, msg, kwargs):

            """
            Override process

            Updates dict
            """
            self.set_extra(kwargs)
            return msg, kwargs

        def set_extra(self, kwargs):
            """
            Adds data to kwarg.
            Gets extra properties if found

            RESULT:
                kwargs: the kwarg to add extra to
            """
            if "extra" in kwargs:
                new_extra = dict(self.extra)
                new_extra.update(kwargs["extra"])
                kwargs["extra"] = new_extra
            
            else:
                kwargs["extra"] = dict(self.extra)
            
            for prop_name in self.extra:
                self._add_extra_prop(prop_name, kwargs)
    

    class FAENewlineLogAdapter(FAEExtraPropLogAdapter):
        
        def __init__(self, logger, extra_props=None, newline_def = False):
            """
            FEED:
                logger: the logger to adapt to
                extra_props: additional properties, other than newline
                newline_def: def value for newline
            """

            if extra_props is None:
                extra_props = {}
            
            extra_props["pfx_newline"] = newline_def
            super(FAENewlineLogAdapter, self).__init__(logger, extra_props)
    
    LOG_PATH = os.path.join(renpy.config.basedir, "log")

    LOG_MAXSIZE_B = 5242880

    LOG_HEADER = "\n\n{_date}\n{system_info}\n{renpy_ver}\n\nVERSION: {game_ver}\n{separator}"

    MSG_INFO = "[" + LT_INFO + "]: {0}"
    MSG_WARN = "[" + LT_WARN + "]: {0}"
    MSG_ERR = "[" + LT_ERROR + "]: {0}"

    MSG_INFO_ID = "    " + MSG_INFO
    MSG_WARN_ID = "    " + MSG_WARN
    MSG_ERR_ID = "    " + MSG_ERR

    #Load strs for files
    LOAD_TRY = "Attempting to load '{0}'..."
    LOAD_SUCC = "'{0}' loaded successfully."
    LOAD_FAILED = "Load failed."

    JSON_LOAD_FAILED = "Failed to load json at '{0}'."
    FILE_LOAD_FAILED = "Failed to load file at '{0}'. | {1}"
    NAME_BAD = "name must be unique."


    try:
        if not os.path.exists(LOG_PATH):
            os.makedirs(LOG_PATH)
    
    except Exception as e:
        raise Exception("Failed to create log folder. Reason: {}".format(e))
    

    def init_log(name, append=True, formatter=None, adapter_ctor=None, header=None, cycles=5):

        """
        Starts a logger with handler with the name and files

        FEED:
            name: Name of logger & logfile
                E.G. Name is Test, logfile name would be 'Test.txt'
            append: do we append or clear

            formatter: logging.Formatter used

            adapter_ctor: What adapter do we want to use?

            header: Header block

            cycles: Int representing the amount of log cycles to use

        """

        _kwargs = {
            "filename": os.path.join(LOG_PATH, name + '.log'),
            "mode": ("a" if append else "w"),
            "encoding": "utf-8",
            "delay": header is False
        }

        if header is None:
            header = LOG_HEADER
        
        if append:
            handler = loghandlers.RotatingFileHandler(
                maxBytes=LOG_MAXSIZE_B,
                backupCount=cycles,
                **_kwargs
            )

        else:
            handler = logging.FileHandler(**_kwargs)
        
        log = logging.getLogger(name)

        log.setLevel(logging.DEBUG)
        handler.setLevel(logging.DEBUG)

        log.addHandler(handler)

        if header is not False:
            log.info(
                header.format(
                    _date=datetime.datetime.now().strftime("%a %b %d %H:%M:%S %Y"),
                    system_info="{0} {1} - build: {2}".format(platform.system(), platform.release(), platform.version()),
                    renpy_ver=renpy.version(),
                    game_ver=renpy.config.version,
                    separator="=" * 50
                )
            )
        
        if formatter is None:
            handler.setFormatter(FAELogFormatter())
        
        else:
            handler.setFormatter(formatter)
        
        if adapter_ctor is not None:
            log = adapter_ctor(log)
        
        LOG_DEF[name] = log

        return log

    def is_inited(name):
        """
        Has the log been started?
        """

        return name in LOG_DEF

python early in fae_utilities:
    import codecs
    import os
    import sys
    import platform
    import shutil
    import store
    import time
    import traceback
    import functools

    from store import fae_logging
    fae_log = fae_logging.init_log("fae_log")

    class IsolatedFlexProp(object):

        __slots__ = ("_default_val", "_set_vars")

        def __init__(self, default_val=None):

            """
            FEED:
                value to return as default
            """
            self._default_val = default_val
            self._set_vars = {}
        
        def __repr__(self):
            return "<{}: (def value: {}, data: {})>".format(
                type(self).__name__,
                self._default_val,
                self._set_vars
            )

        def __contains__(self, item):
            return item in self._set_vars

        def __getattr__(self, name):
            if name.startswith("_"):
                return super(IsolatedFlexProp, self).__getattribute__(name)
            return self._set_vars.get(name, self._default_val)

        def __setattr__(self, name, value):
            if name.startswith("_"):
                super(IsolatedFlexProp, self).__setattr__(name, value)
            else:
                self._set_vars[name] = value

        def __getitem__(self, key):
            return self.__getattr__(key)

        def __setitem__(self, key, value):
            self.__setattr__(key, value)

        def _clear(self):
            """
            Erases manually set attr
            """
            self._set_vars.clear()
        
        def _from_dict(self, data):

            """
            FEED:
                data: dict to load from
            """
            for key in data:
                self[key] = data[key]
        
        def _to_dict(self):
            """
            RESULT:
                dictionary of the set data
            """
            return dict(self._set_vars)

    def compareVersionLists(curr_vers, comparative_vers):

        def fixVersionListLen(smaller_vers_list, larger_vers_list):
            for missing_ind in range(len(larger_vers_list) - len(smaller_vers_list)):
                smaller_vers_list.append(0)
            return smaller_vers_list
        
        if len(curr_vers) < len(comparative_vers):
            curr_vers = fixVersionListLen(curr_vers, comparative_vers)

        elif len(curr_vers) > len(comparative_vers):
            comparative_vers = fixVersionListLen(comparative_vers, curr_vers)
        
        if comparative_vers == curr_vers:
            return 0

        for index in range(len(curr_vers)):
            if curr_vers[index] > comparative_vers[index]:
                return 1

            elif curr_vers[index] < comparative_vers[index]:
                return -1

    def copyfile(oldpath, newpath):
        try:
            shutil.copyfile(oldpath, newpath)
            return True
        except Exception as e:
            fae_log.error(_fae__failcp.format(oldpath, newpath, str(e)))
        return False

    def _get_version_nums(ver_str):
    
        return list(map(int, ver_str.partition("-")[0].split(".")))

    def _is_downgrade(from_ver_str, to_ver_str):

        return compareVersionLists(
            _get_version_nums(from_ver_str),
            _get_version_nums(to_ver_str)
        ) > 0

    def trydel(f_path, log=False):

        try:
            os.remove(f_path)
        except Exception as e:
            if log:
                fae_log.error("[exp] {0}".format(repr(e)))
    
    def trywrite(f_path, msg, log=False, mode="w"):

        outfile = None
        try:
            outfile = open(f_path, mode)
            outfile.write(msg)
        except Exception as e:
            if log:
                fae_log.error("[exp] {0}".format(repr(e)))
        finally:
            if outfile is not None:
                outfile.close()
    

    def tryparseint(value, default=0):
        
        try:
            return int(value)
        except:
            return default

