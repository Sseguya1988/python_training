# Exercise 9: Parse the following JSON to get all the values of a key ‘name’ within an array
# given json object
json_object = [
   {
      "id":1,
      "name":"name1",
      "color":[
         "red",
         "green"
      ]
   },
   {
      "id":2,
      "name":"name2",
      "color":[
         "pink",
         "yellow"
      ]
   }
]
# xextract names from json_object
names = [item["name"] for item in json_object]
# print these names
print(names)
