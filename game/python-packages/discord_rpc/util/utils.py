from copy import deepcopy
import json
from os import getenv, getpid, path
import platform
from sys import version_info, argv


class Empty(Exception):
    pass


class DummyQueue(object):
    """
    Dummy queue thread that does nothing. Should only be used if imports fail.
    """

    def __init__(self, maxsize=0):
        pass

    def qsize(self):
        return 0

    def empty(self):
        return True

    def full(self):
        return False

    def put(self, obj, *args, **kwargs):
        pass

    def put_nowait(self, obj):
        pass

    def get(self, *args, **kwargs):
        raise Empty

    def get_nowait(self):
        raise Empty

    def task_done(self):
        pass

    def join(self):
        pass


def is_python3():
    return version_info[0] == 3


def is_windows():
    return platform.system() == 'Windows'


def is_linux():
    return platform.system() == 'Linux'


def is_mac_osx():
    # this may not be accurate, just going off of what I find off the internet
    return platform.system() == 'Darwin'


def get_temp_path():
    if is_windows():
        return None
    for val in ('XDG_RUNTIME_DIR', 'TMPDIR', 'TMP', 'TEMP'):
        tmp = getenv(val)
        if tmp is not None:
            return tmp
    return '/tmp'


def get_process_id():
    return getpid()


def is_callable(obj):
    try:
        # for Python 2.x or Python 3.2+
        return callable(obj)
    except Exception:
        # for Python version: 3 - 3.2
        return hasattr(obj, '__call__')


# python 2 + 3 compatibility
if is_python3():
    unicode = str
    bytes = bytes
else:
    bytes = str
    unicode = unicode


def to_bytes(obj):
    if isinstance(obj, type(b'')):
        return obj
    if hasattr(obj, 'encode') and is_callable(obj.encode):
        return obj.encode('ascii', 'replace')
    raise TypeError('Could not convert object type "{}" to bytes!'.format(type(obj)))


def to_unicode(obj):
    if isinstance(obj, type(u'')):
        return obj
    if hasattr(obj, 'decode') and is_callable(obj.decode):
        return obj.decode(encoding='utf-8')
    raise TypeError('Could not convert object type "{}" to unicode!'.format(type(obj)))


def iter_keys(obj):
    if not isinstance(obj, dict):
        raise TypeError('Object must be of type dict!')
    if is_python3():
        return obj.keys()
    return obj.iterkeys()


def iter_items(obj):
    if not isinstance(obj, dict):
        raise TypeError('Object must be of type dict!')
    if is_python3():
        return obj.items()
    return obj.iteritems()


def iter_values(obj):
    if not isinstance(obj, dict):
        raise TypeError('Object must be of type dict!')
    if is_python3():
        return obj.values()
    return obj.itervalues()


def _py_dict(obj):
    if not isinstance(obj, dict):
        raise TypeError('Object must be of type dict!')
    new_dict = dict()
    for name, val in iter_items(obj):
        if isinstance(name, type(b'')) and is_python3():
            name = to_unicode(name)
        elif isinstance(name, type(u'')) and not is_python3():
            name = to_bytes(name)
        if isinstance(val, dict):
            val = _py_dict(val)
        elif isinstance(val, type(b'')) and is_python3():
            val = to_unicode(val)
        elif isinstance(val, type(u'')) and not is_python3():
            val = to_bytes(val)
        new_dict[name] = val
    return deepcopy(new_dict)


def json2dict(obj):
    if isinstance(obj, dict):
        return deepcopy(_py_dict(obj))
    if obj is None:
        return dict()
    if hasattr(obj, 'strip'):
        if obj.strip() == '':
            return dict()
        else:
            return deepcopy(_py_dict(deepcopy(json.loads(obj))))
    raise TypeError('Object must be of string type!')


if not is_python3():
    range = xrange
else:
    range = range


def get_executable_directory():
    return path.abspath(path.dirname(argv[0]))


def get_executable_path():
    return path.join(get_executable_directory(), argv[0])
