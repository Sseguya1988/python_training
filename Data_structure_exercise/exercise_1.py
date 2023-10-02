# Exercise 1: Create a list by picking an odd-index items from the first list and even index items from the second
# Generate sample lists
l1 = [1, 2, 3, 4, 5, 6]
l2 = ["a", "b", "c", "d", "e", "f"]
# define an empty list l3
l3 = []
# iterate elements of l1 and l2 using zip into l3
for item1, item2 in zip(l1[1::2], l2[::2]):
    l3.extend([item1, item2])

print(f"The new list is {l3}")
