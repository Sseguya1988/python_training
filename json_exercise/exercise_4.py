# Exercise 4: Sort JSON keys in and write them into a file
import json
# Given json data
sampleJson = {
    "id": 1,
    "name": "value2",
    "age": 29
}
# sort this data alphabetically
sort_samplejson = json.dumps(sampleJson, indent=2, sort_keys=True)
print(sort_samplejson)

