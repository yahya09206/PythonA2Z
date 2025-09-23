from typing import List

def move_zeroes_two(nums: List[int]) -> None:

    l = 0

    for r in range(len(nums)):
        if nums[r]:
            temp = nums[l]
            nums[l] = nums[r]
            nums[r] = temp
