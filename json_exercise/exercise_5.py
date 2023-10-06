# Exercise 5: Access the nested key ‘salary’ from the following JSON
import json
# Given sample data of the json object
sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payble":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""
# convert a json string into a Python dictionary
new_samplejson = json.loads(sampleJson)
# Access the nested key "salary" and print its value
salary_value = new_samplejson["company"]["employee"]["payble"]["salary"]
print(f"The value for salary is {salary_value}")
