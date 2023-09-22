# Exercise 12: Display Fibonacci series up to 10 terms
# define a function to process fibonacci numbers
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a)
        a, b = b, a + b

# print sequence
num_terms = int(input("Enter number of Fibonacci terms: "))
fibonacci(num_terms)

