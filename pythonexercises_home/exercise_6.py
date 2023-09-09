# Exercise 6: Filter dictionary to contain keys present in the given list
di = {"A": 65, "B": 66, "C": 67, "D": 68, "E": 69, "F": 70}
# List of keys to filter
keys_filter = ["A", "C", "F"]
# set up an empty dictionary
filtered_dict = {}
# for all keys in key_filter, if this key is in di, then this key and value is added to new dic
for key in keys_filter:
    if key in di:
        filtered_dict[key] = di[key]
print(filtered_dict)

"""
filtered_dict = {key: ascii_dict[key] for key in keys_to_filter}
"""

