# function that prints "Hello, World!"
def greet():
    print("Hello, World!")

# function that prints "Goodbye, World!"
def say_goodbye():
    print("Goodbye, World!")


# call above function
greet()
say_goodbye()

print("------------------------------")

def print_number(n):
    print(n)

print(2)
print(3)
print(4)
print(5)

print("------------------------------")
#functions with parameters
def greet(name):
    msg = "Hello " + name
    print(msg)


greet("Mikey")

def farewell(name):
    msg = "Goodbye " + name
    print(msg)

farewell("NeetCode")

print("------------------------------")
#functions with multiple parameters
def two_sum(num1, num2):
    print(num1 + num2)

def three_sum(num1, num2, num3):
    print(num1 + num2 + num3)

two_sum(7,10)
three_sum(3,5,6)
