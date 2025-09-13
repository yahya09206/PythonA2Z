def valid_palindrome(self, s: str) -> bool:

    l = 0
    r = len(s) - 1

    while l <= r:

        char_left = s[l]
        char_right = s[r]

        # Skip non-alphanumeric characters from the left
        if not char_left.isalnum():
            l += 1
        # Skip non-alphanumeric characters from the right
        elif not char_right.isalnum():
            r -= 1
        # Check if the characters are equal ignoring case
        elif char_left.lower() != char_right.lower():
            # Characters are not equal, so it's not a palindrome
            return False
        # Move both pointers towards the center
        else:

            l += 1
            r -= 1
    # All characters have been checked and are equal, so it's a
    # palindrome
    return True
