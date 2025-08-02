"""
Write a method called cylinderSurfaceArea that accepts a radius and height (both real numbers) as parameters and
returns the surface area of a cylinder with those dimensions. For example,
the call cylinderSurfaceArea(3.0, 4.5) should return 141.3716694115407.
The formula for the surface area of a cylinder with radius r and height h is the following:

surface area = 2πr2 + 2πrh
"""
import math


def cylinder_surf_area(r: float, h: float) -> float:
    return (2 * math.pi * r * r) + (2 * math.pi * r * h)

print(cylinder_surf_area(3.0, 4.5))
