# Exercise 7: Check if a value exists in a dictionary
sample_dict = {'a': 100, 'b': 200, 'c': 300}
# use loops
for value in sample_dict.values():
    if value == 200:
        print("Value of 200 exists in the dictionary")
        break
# in case loop completes without locating the 200
else:
    print("Value of 200 doesn't exist in this dictionary")
