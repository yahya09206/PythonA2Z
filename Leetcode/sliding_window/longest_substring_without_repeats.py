from typing import List

def longest_substring_without_repeating(s: str) -> int:

    # LINE 1: Create empty set to track characters in the current window, this will store
    # we've seen in our current window
    charSet = set()