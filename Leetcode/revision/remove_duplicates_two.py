from typing import List

def remove_dupes(nums: List[int]) -> int:

    l = 0

    for r in range(len(nums)):
        if nums[r] != nums[r - 1]:
            nums[l] = nums[r]
            l += 1
    return l


print(remove_dupes([1, 1, 1, 2, 3,3, 4, 5,6,6]))
