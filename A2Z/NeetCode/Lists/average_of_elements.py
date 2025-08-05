from typing import List

def avg_of_elements(nums: List[float]) -> float:
    sum = 0
    for elements in nums:
        sum += elements
    return sum / len(nums)

print(avg_of_elements([2, 3, 4, 5]))
