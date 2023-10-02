# Exercise 1: Create a list by picking an odd-index items from the first list and even index items from the second
# Generate sample lists
l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]
# define an empty list l3
l3 = []
# iterate elements of l1 and l2 using zip into l3
for item1, item2 in zip(l1[1::2], l2[2::2]):
    l3.extend([item1, item2])

print(f"The new list is {l3}")
