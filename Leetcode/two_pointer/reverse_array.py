from typing import List

def reverse_list(arr: List[int]) -> List:

    # initialize a left and right pointer
    l = 0
    r = len(arr) - 1

    while l < r:
        # can also use tuple unpacking to swap -> arr[l], arr[r] = arr[r], arr[l]
        temp = arr[l]
        arr[l] = arr[r]
        arr[r] = temp
        l += 1
        r -= 1
    return arr


print(reverse_list([1, 2, 3, 4, 5]))
