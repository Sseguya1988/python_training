# Exercise 6: Create a recursive function
def recursive_function(n):
    if n == 0:
        return 0
    else:
        return n + recursive_function(n-1)


# use the function
result = recursive_function(5)
print(result)

