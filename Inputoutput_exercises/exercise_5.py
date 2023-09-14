# Exercise 5: Accept a list of 5 float numbers as an input from the user
list1 = input("Enter five spaced float numbers: ")
# split each string item individually
new_list1 = list1.split()
# register splited items as float numbers and create a new list
new_list2 = [float(num) for num in new_list1]
# print the obtained list
print(f"The list is: {new_list2}")

"""
list1 = input("Enter five spaced float numbers: ")
new_list1 = list1.split()
if len(new_list1) == 5:
    try:
        new_list2 = [float(num) for num in new_list1]
        print(f"The list is: {new_list2}")
    except ValueError:
        print("Invalid input, pleas enter valid float numbers")
else:
    print("Invalid input, please enter exactly five float numbers")
"""


