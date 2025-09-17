from typing import List

def reverse_string_part_two(s: List[str]):

    l = 0
    r = len(s) - 1

    while l < r:
        s[l], s[r] = s[r], s[l]
        l += 1
        r -= 1

s = ["w", "a", "k", "e"]
reverse_string_part_two(s)
print(s)