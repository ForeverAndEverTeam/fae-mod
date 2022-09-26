from __future__ import absolute_import
from .limits import INT32_MIN, INT32_MAX, UINT32_MAX, INT64_MIN, INT64_MAX, UINT64_MAX


_number_types = [int]
try:
    _number_types.append(float)
except NameError:
    pass
try:
    _number_types.append(long)
except NameError:
    pass
_number_types = tuple(_number_types)


class UnderflowError(ArithmeticError):
    pass


class Number(object):
    _min = None
    _max = None
    _bits = None
    _raise_exceptions = False

    def __init__(self, number=0, raise_exceptions=False):
        self._raise_exceptions = raise_exceptions
        if isinstance(number, Number):
            number = number.get_number()
        else:
            # validate number, ret_val should only be number, not a class
            number = self._check_number(number, number_only=True)
        if not isinstance(number, _number_types):
            raise TypeError('Number must be of type int/float/long!')
        self._number = number

    def _check_number(self, num, number_only=False):
        if self._max is not None and self._min is not None:
            if self._raise_exceptions:
                if num > self._max:
                    raise OverflowError()
                elif num < self._min:
                    raise UnderflowError()
            if self._min == 0:
                if not number_only:
                    return self.__class__(num & self._max)
                else:
                    return num & self._max
            else:
                if num & (1 << (self._bits-1)):
                    if not number_only:
                        return self.__class__(num | ~self._max)
                    else:
                        return num | ~self._max
                else:
                    if not number_only:
                        return self.__class__(num & self._max)
                    else:
                        return num & self._max
        else:
            # there are no min/max to check with, so just return the number
            if not number_only:
                return self.__class__(num)
            else:
                return num

    def __lt__(self, other):
        if isinstance(other, Number):
            other = other.get_number()
        return self._number < other

    def __le__(self, other):
        if isinstance(other, Number):
            other = other.get_number()
        return self._number <= other

    def __eq__(self, other):
        if isinstance(other, Number):
            other = other.get_number()
        return self._number == other

    def __ne__(self, other):
        if isinstance(other, Number):
            other = other.get_number()
        return self._number != other

    def __gt__(self, other):
        if isinstance(other, Number):
            other = other.get_number()
        return self._number > other

    def __ge__(self, other):
        if isinstance(other, Number):
            other = other.get_number()
        return self._number >= other

    def __bool__(self):
        return self._number

    def __repr__(self):
        return "{class_name}({number})".format(class_name=self.__class__.__name__, number=self._number)

    def __str__(self):
        return str(self._number)

    def __cmp__(self, other):
        if isinstance(other, Number):
            other = other.get_number()
        if self._number == other:
            return 0
        elif self._number < other:
            return -1
        elif self._number > other:
            return 1

    def __nonzero__(self):
        return self._number != 0

    def __add__(self, other):
        if isinstance(other, Number):
            other = other.get_number()
        return self._check_number(self._number + other)

    def __sub__(self, other):
        if isinstance(other, Number):
            other = other.get_number()
        return self._check_number(self._number - other)

    def __mul__(self, other):
        if isinstance(other, Number):
            other = other.get_number()
        return self._check_number(self._number * other)

    def __div__(self, other):
        if isinstance(other, Number):
            other = other.get_number()
        return self._check_number(self._number / other)

    def __truediv__(self, other):
        if isinstance(other, Number):
            other = other.get_number()
        return self.__div__(other)

    def __floordiv__(self, other):
        if isinstance(other, Number):
            other = other.get_number()
        return self._check_number(self._number // other)

    def __mod__(self, other):
        if isinstance(other, Number):
            other = other.get_number()
        return self._check_number(self._number % other)

    def __divmod__(self, other):
        if isinstance(other, Number):
            other = other.get_number()
        return self._check_number(divmod(self._number, other))

    def __pow__(self, power, modulo=None):
        if isinstance(power, Number):
            power = power.get_number()
        if modulo is not None and isinstance(modulo, Number):
            modulo = modulo.get_number()
        return self._check_number(pow(self._number, power, modulo))

    def __lshift__(self, other):
        if isinstance(other, Number):
            other = other.get_number()
        return self._check_number(self._number << other)

    def __rshift__(self, other):
        if isinstance(other, Number):
            other = other.get_number()
        return self._check_number(self._number >> other)

    def __and__(self, other):
        if isinstance(other, Number):
            other = other.get_number()
        return self._check_number(self._number & other)

    def __xor__(self, other):
        if isinstance(other, Number):
            other = other.get_number()
        return self._check_number(self._number ^ other)

    def __or__(self, other):
        if isinstance(other, Number):
            other = other.get_number()
        return self._check_number(self._number | other)

    def __radd__(self, other):
        if isinstance(other, Number):
            other = other.get_number()
        return self._check_number(other + self._number)

    def __rsub__(self, other):
        if isinstance(other, Number):
            other = other.get_number()
        return self._check_number(other - self._number)

    def __rmul__(self, other):
        if isinstance(other, Number):
            other = other.get_number()
        return self._check_number(other * self._number)

    def __rdiv__(self, other):
        if isinstance(other, Number):
            other = other.get_number()
        return self._check_number(other / self._number)

    def __rtruediv__(self, other):
        if isinstance(other, Number):
            other = other.get_number()
        return self.__rdiv__(other)

    def __rfloordiv__(self, other):
        if isinstance(other, Number):
            other = other.get_number()
        return self._check_number(other // self._number)

    def __rmod__(self, other):
        if isinstance(other, Number):
            other = other.get_number()
        return self._check_number(other % self._number)

    def __rdivmod__(self, other):
        if isinstance(other, Number):
            other = other.get_number()
        return self._check_number(divmod(other, self._number))

    def __rpow__(self, other):
        if isinstance(other, Number):
            other = other.get_number()
        return self._check_number(pow(other, self._number))

    def __rlshift__(self, other):
        if isinstance(other, Number):
            other = other.get_number()
        return self._check_number(other << self._number)

    def __rrshift__(self, other):
        if isinstance(other, Number):
            other = other.get_number()
        return self._check_number(other >> self._number)

    def __rand__(self, other):
        if isinstance(other, Number):
            other = other.get_number()
        return self._check_number(other & self._number)

    def __rxor__(self, other):
        if isinstance(other, Number):
            other = other.get_number()
        return self._check_number(other ^ self._number)

    def __ror__(self, other):
        if isinstance(other, Number):
            other = other.get_number()
        return self._check_number(other | self._number)

    def __neg__(self):
        return self._check_number(-self._number)

    def __pos__(self):
        return self._check_number(+self._number)

    def __abs__(self):
        return self._check_number(abs(self._number))

    def __invert__(self):
        return self._check_number(~self._number)

    def __complex__(self):
        return complex(self._number)

    def __int__(self):
        return int(self._number)

    def __long__(self):
        return long(self._number)

    def __float__(self):
        return float(self._number)

    def __oct__(self):
        return oct(self._number)

    def __hex__(self):
        return hex(self._number)

    def __round__(self, ndigits=None):
        if ndigits is not None and isinstance(ndigits, Number):
            ndigits = ndigits.get_number()
        return round(self._number, ndigits)

    def __trunc__(self):
        from math import trunc
        return trunc(self._number)

    def __floor__(self):
        from math import floor
        return floor(self._number)

    def __ceil__(self):
        from math import ceil
        return ceil(self._number)

    def get_number(self):
        return self._number

    def get_copy(self):
        return self.__class__(self._number)


class _Int(Number):
    def __init__(self, number=0, raise_exceptions=False):
        if isinstance(number, Number):
            number = number.get_number()
        number = int(number)
        Number.__init__(self, number, raise_exceptions)

    def _check_number(self, num, number_only=False):
        if isinstance(num, Number):
            num = num.get_number()
        num = int(num)
        return Number._check_number(self, num, number_only)


class Int32(_Int):
    _min = INT32_MIN
    _max = INT32_MAX
    _bits = 32


class Int64(_Int):
    _min = INT64_MIN
    _max = INT64_MAX
    _bits = 64


class UInt32(_Int):
    _min = 0
    _max = UINT32_MAX


class UInt64(_Int):
    _min = 0
    _max = UINT64_MAX
