from typing import List

def container_two(height: List[int]) -> int:

    result = 0

    l = 0
    r = len(height) - 1

    while l < r:

        area = (l - r) * min(height[l], height[r])
        result = max(result, area)

        if height[l] <= height[r]:
            l += 1
        else:
            r -= 1


