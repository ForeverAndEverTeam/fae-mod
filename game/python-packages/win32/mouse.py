__all__ = (
    "get_screen_mouse_pos",
)

import ctypes
import ctypes.wintypes as wt

from .common import Point, _get_last_err
from .errors import Win32Error


user = ctypes.windll.user

user.GetCursorPos.argtypes = (wt.LPPOINT,)
user.GetCursorPos.restype = wt.BOOL


def get_screen_mouse_pos() -> Point:

    c_point = wt.POINT()
    result = user.GetCursorPos(ctypes.byref(c_point))

    if not result:
        raise Win32Error("Failed to get mouse pos", _get_last_err())
    
    return Point(c_point.x, c_point.y)