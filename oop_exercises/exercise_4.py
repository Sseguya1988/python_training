# 0OP Exercise 4: Class Inheritance
class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"


# create an instance
bus = Vehicle("Bus", 70, 10)
# apply this class in code
print(bus.seating_capacity(50))
