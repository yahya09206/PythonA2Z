from typing import List


def removed_duplicates(nums: List[int]) -> int:

    l = 0

    # loop through list
    for r in range(len(nums)):
        if nums[r] != nums[l]:
            nums[l + 1] = nums[r]
            l += 1
    return l + 1

print(removed_duplicates([0,0,1,1,1,2,2,3,3,4]))
