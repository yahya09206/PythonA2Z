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


The key insight: We always move the pointer at the shorter wall because:

The water level is always limited by the shorter wall
Moving the taller wall's pointer would only make the width smaller with no chance of improvement
Moving the shorter wall's pointer might find a taller wall, giving us a chance for more water
"""
from typing import List
def container_with_most(height: List[int]) -> int:

    # result to keep track of the current biggest area
    res = 0
    l = 0
    r = len(height) - 1


    while l < r:
        # Calculate the water area between our two "walls":
        # min(height[l], height[r]) = height (water level is limited by the shorter wall)
        # Example: If l=1, r=8, height[1]=8, height[8]=7, then area = (8-1) * min(8,7) = 7 * 7 = 49
        area = (r - l) * min(height[l], height[r])
        # Update our best result. If this new area is bigger than what we had before, keep it.
        # Otherwise, stick with the old best.
        res = max(res, area)

        # If the left wall is shorter or equal, move the left pointer to the right.
        # Why? The shorter wall is the "bottleneck" - we want to find a potentially taller left wall.
        if height[l] <= height[r]:
            l += 1
        # If the right wall is shorter, move the right pointer to the left.
        # Same logic - we're looking for a potentially taller right wall.
        else:
            r -= 1
    # Return the maximum area we found
    return res


print(container_with_most([1, 8, 6, 2, 5, 4, 8, 3, 7]))
print(container_with_most([1, 1]))
