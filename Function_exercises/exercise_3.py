# Exercise 3: Return multiple values from a function
def calculation(a, b):
    a + b, a - b
    print(f"The sum is: {a + b} and the difference is: {a - b}")


# Use the function
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
calculation(a, b)
