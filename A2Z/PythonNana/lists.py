names_of_months = ["January", "February", "March"]

print(names_of_months[0])
names_of_months[0] = "April"
print(names_of_months)

# add a new value to list of elements
names_of_months.append("April")
names_of_months[0] = "January"
print(names_of_months)

print(len(names_of_months))

for months in names_of_months:
    print(months)
