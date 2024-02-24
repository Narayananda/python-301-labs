# Create two classes that model a rectangle and a circle.
# The rectangle class should be constructed by length and width
# while the circle class should be constructed by radius.
#
# Write methods in the appropriate class so that you can calculate
# the area of both the rectangle and the circle, the perimeter
# of the rectangle, and the circumference of the circle.

class rectangle:

    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        return self.height*self.width
    


class circle:
    
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.1415*self.radius**2


a = rectangle(14,23)
b = circle(43)

print(a.area())
print(b.area())
