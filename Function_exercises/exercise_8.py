# Exercise 8. Generate a Python list of all the even numbers between 4 to 30
def even_numbers_in_range(start, end):
    even_numbers = [x for x in range(start, end + 1) if x % 2 == 0]
    return even_numbers


# call for the function
num = even_numbers_in_range(4, 30)
print(num)
