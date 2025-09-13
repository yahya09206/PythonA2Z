def valid_palindrome(self, s: str) -> bool:

    l = 0
    r = len(s) - 1

    while l <= r:

        char_left = s[l]
        char_right = s[r]
