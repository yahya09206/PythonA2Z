"""
Write a method called printStrings that accepts a String and a number of repetitions as
parameters and prints that String the given number of times.
For example, the call:

printStrings("abc", 5);
will print the following output:

abcabcabcabcabc
"""
def print_strings(word: str, reps: int) -> None:
    for i in range(reps):
        print(word,end="")

print_strings("abs",5)
