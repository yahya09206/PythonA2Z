to_seconds = 24
name_of_units = "hours"

def days_to_units(num_of_days: int):
    if num_of_days > 0:
        return f"{num_of_days} days are {num_of_days * to_seconds} {name_of_units}"
    elif num_of_days == 0:
        return "you entered a 0, please enter a valid positive number"
    else:
        return "you entered a negative value, so no conversion for you"

# function for valid input check
def validate_and_execute():
    if user_input.isdigit():
        user_input_number = int(user_input)
        calculated_value = days_to_units(user_input_number)
        print(calculated_value)
    else:
        print("your input is not a valid number, Don't ruin my program!")


# accept user input
user_input = input("Hey user, enter a number of days and I will convert it to seconds!\n")
validate_and_execute()


