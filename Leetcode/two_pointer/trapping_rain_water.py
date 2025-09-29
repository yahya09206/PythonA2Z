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
            l += 1
            left_max = max(left_max, height[l])
            result += left_max - height[l]
        else:
            r -= 1
            right_max = max(right_max, height[r])
            result += right_max - height[r]

    return result


print(trapping_rain_water([0, 2, 0, 3, 1, 0, 1, 3, 2, 1]))
print(trapping_rain_water([0,1,0,2,1,0,1,3,2,1,2,1]))
print(trapping_rain_water([4,2,0,3,2,5]))