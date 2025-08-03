from typing import List


def count_x(nums: List[int], x: int) -> int:

    count = 0
    length = len(nums)
    for n in nums:
        if n == x:
            count += 1
    return count

print(count_x([1, 2, 5, 6, 5], 5))
print(count_x([4, 3, 6, 1, 6], 5))
print(count_x([4, 7, 7, 6, 7, 6], 7))