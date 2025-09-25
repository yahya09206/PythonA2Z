from typing import List

def remove_element(nums: List[int], target: int) -> int:

    l = 0

    for r in range(len(nums)):

        # check if the current index is equal to the target
        if nums[r] != target:
            temp = nums[l]
            nums[l] = nums[r]
            nums[r] = temp
            l += 1
    return l


print(remove_element([3, 2, 2, 3, 3, 4], 2))
print(remove_element([0,1,2,2,3,0,4,2], 2))