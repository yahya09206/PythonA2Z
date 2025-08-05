from typing import List


def product_of_elements(nums: List[int]) -> int:
    cumulative_product = 1
    for elements in nums:
        cumulative_product *= elements
    return cumulative_product


print(product_of_elements([2, 3, 4, 5]))
