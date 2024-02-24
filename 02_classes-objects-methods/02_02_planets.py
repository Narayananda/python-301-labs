# Create a `Planet()` class that models attributes and methods of
# a planet object.
# Use the appropriate dunder method to get informative output with `print()`

class Planet():
    
    def __init__(self, planet, volume, radius, distance, temperture, color, galaxy, speed ):
        self.planet = planet
        self.volume = volume
        self.radius = radius
        self.distance = distance
        self.temperture = temperture
        self.color = color
        self.galaxy = galaxy
        self.speed = speed 

    def info(self):
        return f"""The planet is {self.planet} is located in the {self.galaxy} galaxy, which is {self.distance} lightyears away from earth.\nThe volume of 
{self.planet} is {self.volume}\nIt's radius is {self.radius}.\nIt's temperture is {self.temperture}.\nIt's color is {self.color}.\nIt's speed is {self.speed}"""

    def __str__(self):
        return f"{self.planet} {self.volume} {self.radius} {self.distance} {self.temperture} {self.color} {self.galaxy} {self.speed}"
    
    
i = Planet('CyperX-108', '100000km3', 200345, 35045, '273K', 'Green', 'Andromida', 435345)

print(i.info())