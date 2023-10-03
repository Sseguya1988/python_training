# Exercise 8: Iterate a given list and check if a given element exists as a key’s value in a dictionary. If not, delete it from the list
roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
sample_dict = {'John': 47, 'Emma': 69, 'Kelly': 76, 'Jason': 97}
# using list comprehension to filter elements
new_list = [num for num in roll_number if num in sample_dict.values()]
print(new_list)

"""roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
sample_dict = {'John': 47, 'Emma': 69, 'Kelly': 76, 'Jason': 97}
# iterate to check if given element exists as key's value else delete from list
new_list = [i for i in roll_number if i in sample_dict]
print(new_list)"""
