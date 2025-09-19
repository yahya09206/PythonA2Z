from typing import List

def remove_element(nums: List[int], target: int) -> int:

    l = 0

    for r in range(len(nums)):

        if nums[r] == target:
            temp = nums[l]
            nums[l] = nums[r]
            nums[r] = temp
            l += 1
    return l