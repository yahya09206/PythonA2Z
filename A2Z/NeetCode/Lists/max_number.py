from typing import List


def get_max(nums: List[int]) -> int:
    max = nums[0] # or set this value to first index in list
    for n in nums:
        if n > max:
            max = n
    return max

print(get_max([7, 3, 4, 5]))
print(get_max([5, 4, 5, 6]))