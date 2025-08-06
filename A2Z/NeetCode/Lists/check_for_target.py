from typing import List

def check_for_target_element(nums: List[int], target: int) -> int:

    for i in nums:
        if i == target:
            return target
    return -1



print(check_for_target_element([1, 2, 3, 4, 5, 6, 7, -2], -2))