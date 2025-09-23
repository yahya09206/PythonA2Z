from typing import List

def three_sum(nums: List[int]) -> List[List[int]]:

    # sort array
    nums.sort()

    # set n to length of array
    n = len(nums) - 1

    result = []

    for r in range(len(nums)):

        if nums[r] > 0:
            break


