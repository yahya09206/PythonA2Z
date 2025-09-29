from typing import List

def trapping_rain_water(height: List[int]) -> int:

    if not height:
        return 0

    l = 0
    r = len(height) - 1

    left_max = height[l]
    right_max = height[r]

    result = 0

    while l < r:

        if left_max < right_max:








    return result
