"""
Write a method largestAbsVal that accepts three integers as parameters and returns the largest of their three absolute values.
For example, a call of largestAbsVal(7, -2, -11) would return 11, and a call of largestAbsVal(-4, 5, 2) would return 5.

"""
def largest_abs_val(a: int, b: int, c: int) -> int:
    return max(abs(a),abs(b), abs(c))


print(largest_abs_val(7, -2, -11))
print(largest_abs_val(-4, 5, 2))