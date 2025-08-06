from typing import List


def get_sum(nums: List[int]) -> int:
    total_sum = 0
    for i in nums:
        total_sum += i
    return total_sum

print(get_sum([1, 2, 3, 4, 5]))
print(get_sum([5, 4, 5, 6]))