import datetime

user_input = input("enter your goal with a deadline separated by a colon\n")
input_list = user_input.split(":")

goal = input_list[0]
deadline = input_list[1]

datetime.datetime.strptime(deadline, "d.m.y")
print(input_list)