# Exercise 16: Calculate the cube of all numbers from 1 to a given number
number_n = int(input("Enter maximum number: "))
# calculate and print the cube of numbers 1 to number_n
for i in range(1, number_n + 1):
    cube = i**3
    print(f"Current number is: {i} and the cube is {cube}")
