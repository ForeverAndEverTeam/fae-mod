from __future__ import absolute_import
import random
from .types import Int32, Int64


class Backoff(object):
    _min_amt = None
    _max_amt = None
    _current = None
    _fails = Int32()

    def __init__(self, min_amt, max_amt):
        min_amt = max(min_amt, 1)
        max_amt = max(max_amt, 1)
        self._min_amt = Int64(min_amt)
        self._max_amt = Int64(max_amt)
        self._current = Int64(min_amt)

    def reset(self):
        self._fails = Int32(0)
        self._current = self._min_amt.get_copy()

    def next_delay(self):
        self._fails += 1
        delay = Int64(self._current.get_number() * 2.0 * random.random())
        self._current = Int64(min(self._current.get_number() + delay.get_number(), self._max_amt))
        return self._current

    @property
    def fails(self):
        return self._fails

    @property
    def current(self):
        return self._current
