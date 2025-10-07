from typing import List

def reverse_string_three(s: List[str]):

    l = 0
    r = len(s) - 1

    while l < r:
        temp = s[l]
        s[l] = s[r]
        s[r] = temp
        l += 1
        r -= 1

word = ['w', 'a', 'k', 'e']
reverse_string_three(word)
print(word)

