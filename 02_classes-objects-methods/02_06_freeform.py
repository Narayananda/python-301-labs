# Write a script with three classes that model everyday objects.
# - Each class should have an `__init__()` method that sets at least 3 attributes
# - Include a `__str__()` method in each class that prints out the attributes
#     in a nicely formatted string.
# - Overload the `__add__()` method in one of the classes so that it's possible
#     to add attributes of two instances of that class using the `+` operator.
# - Create at least two instances of each class.
# - Once the objects are created, change some of their attribute values.
#
# Be creative. Have some fun. :)
# Using objects you can model anything you want:
# Animals, paintings, card games, sports teams, trees, people etc...


class music:

    def __init__(self, name, duration:int, genre):
        self.name = name
        self.duration = duration
        self.genre = genre
    
    def play(self):
        print(f"Sweet {self.genre}",end="")
        for i in range(self.duration):
            print(f"{self.name}","La "*i,end="")

    def __str__(self):
        return f"-----MUSIC-----\nTitle: {self.name}\nDuration: {self.duration}m\nGenre: {self.genre}"

class bowl:

    def __init__(self, radius, height, weight):
        self.radius = radius
        self.height = height
        self.weight = weight

    def __str__(self):
        return f"-----BOWL-----\nRadius: {self.radius}cm\nHeight: {self.height}cm\nWeight: {self.weight}g"

class water:

    def __init__(self, temperature, amount, origin):
        self.temperature = temperature
        self.amount = amount
        self.origin = origin

    def __add__(self, other):
        new_temperature = self.temperature + other.temperature
        new_amount = self.amount + other.amount
        new_origin = self.origin + other.origin
        return water(new_temperature,new_amount,new_origin)
    
    def drink(self,amount):
        print(f"You had a {self.amount}ml sip of water")
        self.amount -= amount

    def fill(self, amount):
        print("You've replenished the water")
        self.amount += amount

    def __str__(self):
        return f"-----WATER-----\nTemperature: {self.temperature}C\nAmount: {self.amount}ml\nOrigin: {self.origin}"


music1 = music("Goat",6,"Jazz")
music2 = music("A way away", 4.51,"RnB")

bowl1 = bowl(5,11,45.6)
bowl2 = bowl(3.5,9,23.2)

water1 = water(25,264,"ocean")
water2 = water(4,2431,"spring")
water3 = water1+water2
water3.fill(4000)

print(water3)
print(bowl1)
print(music1.play())

