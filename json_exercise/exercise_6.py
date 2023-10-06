# Exercise 6: Convert the following Vehicle Object into JSON
import json
# Given  Vehicle json object
class Vehicle:
    def __init__(self, name, engine, price):
        self.name = name
        self.engine = engine
        self.price = price

    def to_json(self):
        return {
            "name": self.name,
            "engine": self.engine,
            "price": self.price
        }


vehicle = Vehicle("Toyota Rav4", "2.5L", 32000)
# convert this into a json object
vehicle_json = json.dumps(vehicle.to_json(), indent=2)
print(vehicle_json)
