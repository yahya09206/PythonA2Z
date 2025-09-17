from typing import List

def reverse_part_two(nums: List[int]):

    l = 0
    r = len(nums) - 1

    while l < r:
        temp = nums[l]
        nums[l] = nums[r]
        nums[r] = temp
        l += 1
        r -= 1


nums_list = [1,2,3,4,5]
reverse_part_two(nums_list)
print(nums_list)