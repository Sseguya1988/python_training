# Exercise 7: Print the following pattern
num_columns = 5
# use nested loops to generate the
for i in range(1, num_columns + 1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()
