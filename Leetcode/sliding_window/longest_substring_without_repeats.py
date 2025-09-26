from typing import List

def longest_substring_without_repeating(s: str) -> int:

    # LINE 1: Create empty set to track characters in the current window, this will store characters
    # we've seen in our current window
    charSet = set()

    """
    Set left pointer to 0 (start of string)
    Set result to 0 (maximum length found so far)
    """

    l = 0
    result = 0

