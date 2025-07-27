for i in range(0,13):
    print(i, end=' ')

print()
print("------------------------")
# for loop with range
for i in range(10, 21):
    print(i, end=' ')

print()
print("------------------------")
# for loop with different increment
for i in range(0,101, 10):
    print(i, end=' ')

print()
print("------------------------")
# for loop to reverse sequence of numbers
for i in range(20, 9, -1):
    print(i, end=' ')

print()
print("------------------------")
# wrap above into a function
for i in reversed(range(10, 21)):
    print(i, end=' ')