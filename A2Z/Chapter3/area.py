# Write a method named area that accepts the radius of a circle as a parameter and returns the area of a circle with that radius.
# For example, the call area(2.0) should return 12.566370614359172. You may assume that the radius is non-negative.
import math


def area(a: float) -> float:
    return a * a * math.pi


print(area(2.0))