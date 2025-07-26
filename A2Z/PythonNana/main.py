to_seconds = 24
name_of_units = "hours"

def days_to_units(num_of_days: int):
    return f"{num_of_days} days are {num_of_days * to_seconds} {name_of_units}"

# function for valid input check
def validate_and_execute():
    try:

        if user_input.isdigit():
            user_input_number = int(user_input)
            if user_input_number > 0:
                calculated_value = days_to_units(user_input_number)
                print(calculated_value)
            elif user_input_number == 0:
                print("you entered a 0, pleaser enter a valid positive number")

    except ValueError:
            print("your input is not a valid number, Don't ruin my program!")


# accept user input
while user_input != "exit":
    user_input = input("Hey user, enter a number of days and I will convert it to seconds!\n")
    validate_and_execute()


