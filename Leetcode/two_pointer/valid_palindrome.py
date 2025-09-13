def valid_palindrome(self, s: str) -> bool:

    l = 0
    r = len(s) - 1

    while l <= r:

        char_left = s[l]
        char_right = s[r]

        if not char_left.isalnum():
            l += 1
        elif not char_right.isalnum():
            r -= 1
        elif char_left.lower() != char_right.lower():
            return False
