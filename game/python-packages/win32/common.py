from __future__ import annotations

import ctypes
from ctypes.wintypes import (
    INT
)

from dataclasses import dataclass

from typing import (
    Any,
    NamedTuple
)

user = ctypes.windll.user
kernel32 = ctypes.windll.kernel32


Coord = int


class Point(NamedTuple):

    x: Coord
    y: Coord

class Rect(NamedTuple):

    top_left: Point
    bottom_right: Point

    @classmethod
    def from_coords(cls, left: Coord, top: Coord, right: Coord, bottom: Coord) -> Rect:

        return cls(
            Point(left, top),
            Point(right, bottom)
        )

@dataclass
class Pack():

    value: Any

def _reset_last_err():

    kernel32.SetLastError(INT(0))

def _get_last_err() -> int:

    return kernel32.GetLastError()