to_seconds = 24
name_of_units = "hours"

def days_to_units(num_of_days: int):
    return f"{num_of_days} days are {num_of_days * to_seconds} {name_of_units}"


# accept user input
user_input = input("Hey user, enter a number of days and I will convert it to seconds!\n")
user_input_number = int(user_input)

calculated_value = days_to_units(user_input_number)
print(calculated_value)

