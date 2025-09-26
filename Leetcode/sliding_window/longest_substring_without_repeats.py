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
        #  Check if the current character (at position r) is already in our set. If it is, we have a duplicate!
        while s[r] in charSet:
            """
            Shrink our window from the left until we remove the duplicate:
            Remove the character at the left pointer from our set
            Move the left pointer one step to the right
            Keep doing this until the duplicate is gone
            """
            charSet.remove(s[l])
            l += 1

        # Add the current character to our set (now that we know it's not a duplicate)
        charSet.add(s[r])

        """
        What it does: Calculate the current substring length and update our best result:

        r - l + 1 = current window size (right index - left index + 1)
        Keep the bigger value between our old best and current length

        """

        # Return the longest substring length we found
        return result








