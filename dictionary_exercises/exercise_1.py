# Exercise 1: Convert two lists into a dictionary
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
dictionary = {Key: Value for Key, Value in zip(keys, values)}
print(dictionary)
