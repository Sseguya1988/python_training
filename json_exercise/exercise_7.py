# Exercise 7: Convert the following JSON into Vehicle Object
import json
# Define the object class or Vehicle class
class Vehicle:
    def __init__(self, name, engine, price):
        self.name = name
        self.engine = engine
        self.price = price


# Given json object representing the Vehicle data
json_object = {
    "name": "Toyota Rav4",
    "engine": "2.5L",
    "price": 32000
}
# convert json object to vehicle object
vehicle_object = Vehicle(json_object["name"], json_object["engine"], json_object["price"])
print(f"Vehicle name: {vehicle_object.name}, Engine size: {vehicle_object.engine}, Price: {vehicle_object.price}")
