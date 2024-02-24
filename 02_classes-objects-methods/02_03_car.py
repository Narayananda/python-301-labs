# The classic OOP example: Write a class to model a car. The class should:
#
# 1. Set the attributes model, year, and max_speed in the `__init__()` method.
# 2. Have a method that increases the `max_speed` of the car by 5 when called.
# 3. Have a method that prints the details of the car.
#
# Create at least two different objects of this `Car()` class and demonstrate
# changing the objects' attributes.


class Car:

    def __init__(self, model, year, max_speed):
        self.model = model
        self.year = year
        self.max_speed = max_speed

    def accelerate(self):
        self.max_speed += 5

    def details(self):
        return f"The car model is {self.model}.\nIt was released in {self.year}.\nIts max speed is {self.max_speed}"
    

a = Car('FX43',1998,190)
b = Car("QQ88",2006, 150)
a.accelerate()
b.accelerate()

print(a.details())
print(b.details())