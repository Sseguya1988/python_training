# Exercise 2: Access the value of key2 from the following JSON
import json
# Given json
sample_json = """{"key1": "value1", "key2": "value2"}"""
# convert json string into python dictionary
json_data = json.loads(sample_json)
value2 = json_data["key2"]
print(value2)
