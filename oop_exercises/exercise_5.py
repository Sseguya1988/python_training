# OOP Exercise 5: Define a property that must have the same value for every class instance (object)
class Vehicle:
    common_property = "Color: White"

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage


class Bus(Vehicle):
    pass


class Car(Vehicle):
    pass


# define instances
School_Volvo = Bus("School Volvo", 180, 12)
Audi_Q5 = Car("Audi Q5", 240, 18)

print(f"{School_Volvo.common_property}, Vehicle name: {School_Volvo.name}, Speed {School_Volvo.max_speed}, Mileage: {School_Volvo.mileage}")
print(f"{Audi_Q5.common_property}, Vehicle  name {Audi_Q5.name}, Speed: {Audi_Q5.max_speed}, Mileage: {Audi_Q5.mileage}")
