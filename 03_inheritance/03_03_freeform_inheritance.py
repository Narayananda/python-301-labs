# Build on your freeform exercise from the previous section.
# Create child classes of two of the existing classes. Create a child class
# of one of the child classes so that the hierarchy is at least three levels.
#
# Build these classes out step-by-step like you did in the previous exercises.
# Use your notebook to brainstorm ideas and scribble down ideas.
#
# If you cannot think of a way to build on your freeform exercise,
# you can start with a new class from scratch.
# Try to make up your own example for this exercise, but if you are stuck,
# you could start working on the following:
#
# - A `Vehicle()` parent class, with `Truck()` and `Motorcycle()` child classes.
# - A `Restaurant()` parent class, with `Gourmet()` and `FastFood()` child classes.

class Movie:

    def __init__(self, title, year):
        self.title = title
        self.year = year

class RomCom(Movie):
    pass    

class ActionMovie(Movie):
    def __init__(self,title,year,pg=13):
        super().__init__(title,year)
        self.pg = pg

class Crew(ActionMovie):
    def __init__(self, title, year, director, pg=13):
        super().__init__(title,year,pg)
        self.director = director

a = Crew("Flip Flop",1999, "Sean")
print(a.title)