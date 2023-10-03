# Exercise 6: Remove empty strings from the list of strings
list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
new_list = [item for item in list1 if item != ""]
print(new_list)
