# Exercise 9: Find the largest item from a given list
def find_largest_item(input_list):
    if not input_list:
        return None
    else:
        return max(input_list)


# Define a list of numbers
list1 = [1, 20, 3, 41, 19, 6, 12]

# use this function
max_number = find_largest_item(list1)

if max_number is not None:
    print(f"The maximum number in this list is {max_number}")
else:
    print(f"The list is empty")
