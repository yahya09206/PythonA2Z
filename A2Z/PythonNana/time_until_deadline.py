import datetime

user_input = input("enter your goal with a deadline separated by a colon\n")
input_list = user_input.split(":")

goal = input_list[0]
deadline = input_list[1]

deadline_date = datetime.datetime.strptime(deadline, "%d.%m.%Y")
today_date = datetime.datetime.today()
time_till = deadline_date - today_date

# calculate how many days from now until the deadline
print(f"Dear user! Time remaining for your goal: {goal} is {time_till.days} days")