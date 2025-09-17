from typing import List

def valid_palindrome_two(s: str) -> bool:

    l = 0
    r = len(s) - 1

    while l <= r:

        char_left = s[l]
        char_right = s[r]

        if not char_left.isalnum():
            l += 1
        elif not char_right.isalnum():
            r += 1
        elif char_left.lower() != char_right.lower():
            return False
        else:
            l += 1
            r -= 1
    return True


print(valid_palindrome_two("racecars"))


