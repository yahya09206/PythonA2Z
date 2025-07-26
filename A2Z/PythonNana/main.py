to_seconds = 24 * 60 * 60
name_of_units = "seconds"

def days_to_units(num_of_days: int):
    print(f"{num_of_days} days are {20 * to_seconds} {name_of_units}")


days_to_units(20)
days_to_units(35)
days_to_units(50)
days_to_units(100)

