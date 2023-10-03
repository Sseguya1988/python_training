# Exercise 4: Initialize dictionary with default values
employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}
# define new dictionary
new_dict = {keys: defaults for keys in employees}
print(new_dict)
