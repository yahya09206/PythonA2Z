from typing import List
def move_zeroes_to_right(nums):

    left = 0
    for right in range(len(nums)):
        if nums[right] != 0:
            # used when tuples are involved for strict comparison
            # nums[left], nums[right] = nums[right], nums[left]
            temp = nums[right]
            nums[left] = nums[right]
            nums[right] = nums[temp]
            left += 1


nums = [1, 0, 2, 0, 3, 4, 0, 5, 6]
move_zeroes_to_right(nums)
print(nums)