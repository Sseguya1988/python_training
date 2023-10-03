# Exercise 7: Checks if one set is a subset or superset of another set. If found, delete all elements from that set
first_set = {27, 43, 34}
second_set = {34, 93, 22, 27, 43, 53, 48}
# check if first set is a subset of second set
is_subset = first_set.issubset(second_set)
print(f"first_set is a subset of second_set: {is_subset}")
# Check if second_set is a subset of first_set
is_subset2 = second_set.issubset(first_set)
print(f"second_set is a subset of the first_set: {is_subset2}")
# check if first_set is a superset of second_set
is_superset = first_set.issuperset(second_set)
print(f"first_set is a superset of the second_set: {is_superset}")
# check if first_set is a superset of second_set
is_superset2 = second_set.issuperset(first_set)
print(f"second_set is a superset of the first_set: {is_superset2}")

# clear sets as required
if is_subset:
    first_set.clear()
if is_superset:
    second_set.clear()
print(f"The first_set is {first_set}")
print(f"The second_set is {second_set}")
"""
if first_set.issubset(second_set):
    first_set.clear()
    print(f"first_set is a subset of second_set and this has been cleared. {first_set}")

# check if first_set is a superset of second_set
if second_set.issuperset(first_set):
    second_set.clear()
    print(f"second_set is a superset of first_set and first_set has been cleared. {second_set} ")

"""
