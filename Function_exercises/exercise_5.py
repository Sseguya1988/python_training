# Exercise 5: Create an inner function to calculate the addition in the following way
# create an outer function that accepts a and b
def outer_function(a, b):
    # create inner function that computes the addition
    def inner_function(x, y):
        return x + y
    # calculate the addition using inner function
    addition_result = inner_function(a, b)

    # add 5 to addition result
    final_result = addition_result + 5
    # return final result
    return final_result


# use the function
result = outer_function(10, 2)
print(f"The final result is {result}")
