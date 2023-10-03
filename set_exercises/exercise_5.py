# Exercise 5: Remove items from the set at once
set1 = {10, 20, 30, 40, 50}
items_remove = {10, 20, 30}
set2 = set()
for item in set1:
    if item not in items_remove:
        set2.add(item)
print(set2)
