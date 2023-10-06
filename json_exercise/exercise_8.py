# Exercise 8: Check whether following json is valid or invalid. If Invalid correct it
import json
# input json object to test
json_object = {
   "company":{
      "employee":{
         "name":"emma",
         "payble":{
            "salary":7000
            "bonus":800
         }
      }
   }
}
# test if it is valid or not using the defined function
try:
    json.dumps(json_object)
    print("The json object is valid")
except json.JSONDecodeError:
    print("The json object is invalid")
"""
# correction of the code above
import json
# input json object to test
json_object = {
   "company":{
      "employee":{
         "name":"emma",
         "payble":{
            "salary":7000,
            "bonus":800
         }
      }
   }
}
# test if it is valid or not using the defined function
try:
    json.dumps(json_object)
    print("The json object is valid")
except json.JSONDecodeError:
    print("The json object is invalid")
"""
