"""
Write a method called min that takes three integers as parameters and returns the smallest of the three values,
such that a call of min(3, -2, 7) would return -2, and a call of min(19, 27, 6) would return 6.
Use Math.min to write your solution.

"""
def min_num(a: int, b: int, c: int) -> int:
        minimal = min(a,b,c)
        return minimal



print(min(3, -2, 7))