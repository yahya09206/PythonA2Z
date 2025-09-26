from typing import List

def longest_substring_without_repeating(s: str) -> int:

    # Creates an empty set to keep track of characters we've already seen in our current "window".
    # A set automatically prevents duplicates.
    charSet = 0

    l = 0
    result = 0



