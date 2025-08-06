from typing import List

def count_how_many(nums: List[int], target: int) -> int:
    count = 0
    for i in nums:
        if i == target:
            count += 1
    return count


print(count_how_many([1, 1, 1, 2, 2, 3, 4], 3))
print(count_how_many([1, 1, 1, 2, 2, 3, 4], 2))
print(count_how_many([1, 1, 1, 2, 2, 3, 4], 4))
print(count_how_many([1, 1, 1, 2, 2, 3, 4], 1))