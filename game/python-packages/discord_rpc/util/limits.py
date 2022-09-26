def get_min_max(bit_size, unsigned=False):
    if unsigned:
        bit_min = 0
        bit_max = (2**bit_size) - 1
    else:
        bit_min = -(2**(bit_size - 1))
        bit_max = 2**(bit_size - 1) - 1
    return bit_min, bit_max


# limits for c types
CHAR_MIN = -128
CHAR_MAX = 127
UCHAR_MAX = 255

SHORT_MIN = -32768
SHORT_MAX = 32767
USHORT_MAX = 65535

INT_MIN = -2147483648
INT_MAX = 2147483647
UINT_MAX = 4294967295
INT32_MIN = INT_MIN
INT32_MAX = INT_MAX
UINT32_MAX = UINT_MAX

LONG_MIN = -9223372036854775808
LONG_MAX = 9223372036854775807
ULONG_MAX = 18446744073709551615
INT64_MIN = LONG_MIN
INT64_MAX = LONG_MAX
UINT64_MAX = ULONG_MAX
