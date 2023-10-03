# Exercise 1: Add a list of elements to a set
sample_set = {"Yellow", "Orange", "Black"}
sample_list = ["Blue", "Green", "Red"]
# convert sample_list into a set
sample_set2 = set(sample_list)
# combine the two sets
new_set = sample_set | sample_set2
print(new_set)
