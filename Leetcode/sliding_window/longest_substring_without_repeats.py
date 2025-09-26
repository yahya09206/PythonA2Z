from typing import List

def longest_substring_without_repeating(s: str) -> int:

    # Creates an empty set to keep track of characters we've already seen in our current "window".
    # A set automatically prevents duplicates.
    charSet = 0

    # Sets up our left pointer at the beginning of the string (index 0). This marks the start of our current substring.
    l = 0

    # Initialize our result to 0. This will track the longest substring length we've found so far.
    result = 0

    # Start a loop where r (right pointer) goes through each character in the string from left to right.
    # This marks the end of our current substring.
    for r in range(len(s)):



