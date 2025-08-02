"""
Write a method called inputBirthday that accepts a Scanner for the console as a parameter and prompts the user to enter a month,
day, and year of birth, then prints the birthdate in a suitable format. Here is an example dialogue with the user:

On what day of the month were you born? 8
What is the name of the month in which you were born? May
During what year were you born? 1981
You were born on May 8, 1981. You're mighty old!
"""
def input_birth() -> None:
    print(f"You were born on {input("On what day of the month were you born? ")} "
          f"{input("What is the name of the month in which you were born?")}, "
          f"{input("During what year were you born?")}. You're mighty old!")

input_birth()