from typing import List

def remove_duplicates_from_sorted_array(nums: List[int]) -> int:

    l = 1

    for r in range(1, len(nums)):
        if nums[r] != nums[r - 1]:
            nums[l] = nums[r]
            l += 1
    return l


remove_duplicates_from_sorted_array([1,1,2])
remove_duplicates_from_sorted_array([0,0,1,1,1,2,2,3,3,4])


