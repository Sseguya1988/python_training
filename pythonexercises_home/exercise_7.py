# Exercise 7: Print the following number pattern
rows = int(input("Enter number of rows: "))
# Nested loop for rows and columns
for i in range(rows):
    for j in range(rows - i):
        print(i + 1, end=" ")  # Prints the numbers in a given row and end=" " keeps it on the same row
    print()  # iterates to the next value of i or row
