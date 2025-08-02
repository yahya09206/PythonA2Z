"""
Write a method named lastDigit that returns the last digit of an integer.
For example, lastDigit(3572) should return 2. It should work for negative numbers as well.
For example, lastDigit(-947) should return 7.

"""
def last_digit(num: int) -> int:
    return abs(num) % 10


print(last_digit(3572))
print(last_digit(-947))
