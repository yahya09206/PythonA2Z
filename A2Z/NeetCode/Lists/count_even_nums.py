from typing import List

def count_evens(nums: List[int]) -> int:
    count = 0
    for i in nums:
        if i % 2 == 0:
            count += 1
    return count


print(count_evens([1, 2, 3, 4, 5,6]))