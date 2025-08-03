from typing import List

def get_min(nums: List[int]) -> int:
    min = nums[0] # or set this value to first index in list
    for n in nums:
        if n < min:
            min = n
    return min

print(get_min([7, 3, 4, 5]))
print(get_min([5, 4, 5, 6]))