# Exercise 2: Print the following pattern
# number of columns
num_columns = 5
# use "nested for loop" to iterate
for i in range(1, num_columns + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()
