from typing import List

def remove_element_two(nums: List[int], target: int) -> int:

    l = 0

    for r in range(len(nums)):
        if nums[r] != target:
            temp = nums[l]
            nums[l] = nums[r]
            nums[r] = temp
            l += 1
    return l


print(remove_element_two([1, 2, 3, 4], 2))

