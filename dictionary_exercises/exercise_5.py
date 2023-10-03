# Exercise 5: Create a dictionary by extracting the keys from a given dictionary
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# Keys to extract
keys = ["name", "salary"]
# create new dictionary
new_dict = {key: sample_dict[key] for key in keys}
print(new_dict)
