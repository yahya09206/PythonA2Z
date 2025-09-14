"""
Need to find which heights from left to right have the most water based on width and height

result = 0
init left and right pointer

while l < r:
compute the area:
area = (r-l) * min(height[l], height[r])
set res to max between current res and current area

increment left pointer if height[l] is <= than height[r]

else decrement right

return res
"""
from typing import List
def container_with_most(height: List[int]) -> int:

    res = 0
    l = 0
    r = len(height) - 1

    while l < r:
        area = (r - l) * min(height[l], height[r])
        res = max(res, area)

        if height[l] <= height[r]:
            l += 1
        else:
            r -= 1
    return res


print(container_with_most([1, 8, 6, 2, 5, 4, 8, 3, 7]))
print(container_with_most([1, 1]))
