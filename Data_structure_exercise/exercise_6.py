# Exercise 6: Find the intersection (common) of two sets and remove those elements from the first set
first_set = {23, 42, 65, 57, 78, 83, 29}
second_set = {57, 83, 29, 67, 73, 43, 48}
# find intersection
intersection = first_set.intersection(second_set)
# remove the intersection from first_set
first_set.difference_update(intersection)
# print new first_set
print(f"The intersection is {intersection} and the modified first_set is {first_set}")
