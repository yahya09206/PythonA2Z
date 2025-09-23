from typing import List

def move_zeroes_two(nums: List[int]) -> None:

    l = 0

    for r in range(len(nums)):
        if nums[r]:
            temp = nums[l]
            nums[l] = nums[r]
            nums[r] = temp
            l += 1

nums = [0,1,0,2,3,0,11,12]
