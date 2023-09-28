# Exercise 14: Remove empty strings from a list of strings
list_of_strings = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
filtered_list = [string for string in list_of_strings if string != ""]
print(filtered_list)
