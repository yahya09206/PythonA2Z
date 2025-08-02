"""
Write a method called largerAbsVal that takes two integers as parameters and returns the larger of the two absolute values.
A call of largerAbsVal(11, 2) would return 11, and a call of largerAbsVal(4, -5) would return 5.

"""
import math


def larger_abs_val(a: int, b: int) -> int:
    return max(abs(a),abs(b))


print(larger_abs_val(11, 2))
print(larger_abs_val(4, -5))