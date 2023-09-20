# Exercise 4: Write a program to print multiplication table of a given number
num = int(input("Enter number, whose multiplication table is required: "))
for i in range(1, 11):
    mult = num * i
    print(mult)
