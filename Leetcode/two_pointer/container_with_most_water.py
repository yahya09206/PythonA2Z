"""
Need to find which heights from left to right have the most water based on width and height

result = 0
init left and right pointer

while l < r:
compute the area:
area = (r-l) * min(height[l], height[r])

increment left pointer if height[l] is greater than height[r]

else decrement right

return res
"""
from typing import List
def container_with_most(height: List[int]) -> int:

    res = 0
    l = 0
    r = len(height) - 1