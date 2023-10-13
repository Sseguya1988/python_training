# Exercise 8: Print the following pattern
num_rows = int(input("Enter the number of rows: "))

# use a nested for loop to draw required triangle
for i in range(1, num_rows +1):
    for j in range(1, i +1):   # inner loop that prints number for each row
        print(i, end=" ")
    print()
