# Exercise 9: Get the key of a minimum value from the following dictionary
sample_dict = {
  'Physics': 82,
  'Math': 65,
  'history': 75
}
min_key = min(sample_dict, key=sample_dict.get)
# min_value = sample_dict[min_key]
print(min_key)
