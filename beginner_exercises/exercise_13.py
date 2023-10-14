# Exercise 13: Print multiplication table from 1 to 10
for i in range(1, 11):  # apply nested loops
    for j in range(1, 11):
        print(f"{i*j:3}", end="")  # :3 represents the spacing between the table characters
    print()
