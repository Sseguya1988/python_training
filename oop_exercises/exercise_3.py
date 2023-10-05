# OOP Exercise 3: Create a child class Bus that will inherit all of the variables and methods of the Vehicle class
class Vehicle:
    def __init__(self, max_speed, car_mileage):
        self.max_speed = max_speed
        self.car_mileage = car_mileage


class Bus(Vehicle):
    pass
