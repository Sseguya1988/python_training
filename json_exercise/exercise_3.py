# Exercise 3: PrettyPrint following JSON data
import json
# sample json
sampleJson = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3"
}
# prettyprint following json
new_json_sample = json.dumps(sampleJson, indent=2, separators=(",", "="))
print(new_json_sample)
