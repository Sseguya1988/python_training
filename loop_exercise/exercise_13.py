# Exercise 13: Find the factorial of a given number
# define a function to process the factorial
def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result


# apply theis function
num = int(input("Enter number whose Factorial is require: "))
result1 = factorial(num)
print(result1)
