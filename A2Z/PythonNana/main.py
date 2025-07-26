to_seconds = 24
name_of_units = "hours"

def days_to_units(num_of_days: int):
    return f"{num_of_days} days are {num_of_days * to_seconds} {name_of_units}"

# function for valid input check
def validate_and_execute():
    try:

            user_input_number = int(num_of_days_elements)
            if user_input_number > 0:
                calculated_value = days_to_units(user_input_number)
                print(calculated_value)
            elif user_input_number == 0:
                print("you entered a 0, please enter a valid positive number")
            else:
                print("you entered a negative number: please enter a positive number")
    except ValueError:
            print("your input is not a valid number, Don't ruin my program!")

user_input = ""
# accept user input
while user_input != "exit":
    user_input = input("Hey user, enter a number of days and I will convert it to seconds!\n")
    list_of_days = user_input.split(", ")

    print(list_of_days)
    print(set(list_of_days))

    print(type(list_of_days))
    print(type(set(list_of_days)))

    for num_of_days_elements in set(list_of_days):
        validate_and_execute()


