# Exercise 14: Print a downward Half-Pyramid Pattern of Star (asterisk)

# input the number of rows for the loop
num_rows = int(input("Enter the number of rows: "))
# iterate through rows and columns using a "for loop" to draw the desired pattern
for i in range(num_rows, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()
