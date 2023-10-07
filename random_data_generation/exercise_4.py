# Exercise 4: Pick a random character from a given String
import random
# given list to choose an item randomly
list_of_items = ["bags", "pens", "pencils", "books", "rulers"]
list_of_nums = [1, 4, 2, 67, 82, 12, 14, 9]
# choose an item randomly from list
random_choice = random.choice(list_of_items)
random_num_choice = random.choices(list_of_nums, k=2)
print(f"The random item from list of items is : {random_choice}")
print(f"The randomly picked two items from a list of numbers is: {random_num_choice}")
