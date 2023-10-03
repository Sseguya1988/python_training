# Exercise 7: Check if two sets have any elements in common. If yes, display the common elements
set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}
if set1 & set2:
    set3 = set1.intersection(set2)
    print(f"There is an intersection between set1 and set2 given by set: {set3}")
else:
    print("There is no intersection between set1 and set2")
