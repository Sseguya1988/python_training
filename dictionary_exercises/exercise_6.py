# Exercise 6: Delete a list of keys from a dictionary
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

# Keys to remove
keys_removed = ["name", "salary"]
# use loop to delete keys
for key in keys_removed:
    if key in sample_dict:
        del sample_dict[key]
print(sample_dict)
