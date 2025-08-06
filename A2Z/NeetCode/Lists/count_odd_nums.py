from typing import List

def count_odds(nums: List[int]) -> int:
    count = 0
    for i in nums:
        if i % 2 != 0:
            count += 1
    return count

print(count_odds([1, 2, 3, 4, 5, 6, 7]))