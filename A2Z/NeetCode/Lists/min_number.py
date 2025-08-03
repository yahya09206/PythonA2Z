from typing import List

def get_min(nums: List[int]) -> int:
    min = float('inf')
    for n in nums:
        if n < min:
            min = n
    return min

print(get_min([7, 3, 4, 5]))
print(get_min([5, 4, 5, 6]))