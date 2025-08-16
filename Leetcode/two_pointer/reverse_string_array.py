import string
from typing import List


def reverse_string(arr):


    l = 0
    r =  len(arr) - 1

    while l < r:
        temp = arr[l]
        arr[l] = arr[r]
        arr[r] = temp
        l += 1
        r -= 1
    return arr


print(reverse_string(['M','I','K','E','Y']))
print(reverse_string(['w','e','n','d','y']))