from typing import List

def remove_element(nums: List[int], target: int) -> None:

    l = 0

    for r in range(len(nums)):

        if nums[r]:
            temp = nums[l]
            nums[l] = nums[r]
            nums[r] = temp
            l += 1