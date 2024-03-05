import webbrowser

class Ingredient:

     def __init__(self, name, amount):
          self.name = name
          self.amount =  amount

     def get_info(self):
         webbrowser.open_new(f"https://en.wikipedia.org/wiki/{self.name}")

     def get_recipe(self):
         webbrowser.open_new(f"https://www.allrecipes.com/search?q={self.name}")

     def use(self, use_amount):
          self.amount -= use_amount

     def expire(self):
          print(f"whoops, these {self.name}'s went bad...")
          self.name = "expired " + self.name
          


     def __str__(self):
         return f"{self.name}, Amount: {self.amount}"
         

# apple = Ingredient("apple",4)

# apple.get_recipe()

class Spice(Ingredient):

     def __init__(self, name,  amount, taste):
          super().__init__(name, amount)
          self.taste = taste

     
     def grind(self):
          print(f"You now have {self.amount}g of ground {self.name}.")

     def taste(self):
          print(f"You tasted the {self.name}.")


class Vegetable(Ingredient):

     def expire(self):
          print(f" your {self.name} has begun to rot")

     def chop(self):
          print(f"You've chopped the {self.name}")


# a = Spice("salt",200,"flamming hot")
# print(a.taste)
# a.expire()
# a.grind()
# a.taste()

# b = Ingredient("apple",20,"free")

class Stove:
     def __init___(self, name):
          self.name = name

     def turn_on(self):
          print(f"{self.name} is on")

     def turn_off(self):
          print(f"{self.name} is off")     

class Fridge:
     def __init__(self,name):
          self.name = name

     def turn_on(self):
          print(f"{self.name} is on")

     def turn_off(self):
          print(f"{self.name} is off") 

class  Sink:
     def __init__(self,name):
          self.name = name 
          
     def turn_on(self):
          print(f"water is running")

     def turn_off(self):
          print(f"water is off") 

class Countertop:
     def __init__(self, name):
          self.name = name

     def clean():
          print("The counter top has been cleaned")

class kitchen:
     def __init__(self, Stove, Fridge, Countertop, Sink):
          self.stove = Stove
          self.fridge = Fridge
          self.countertop = Countertop
          self.sink = Sink
          
st = Stove("stove")
fr = Fridge("fridge")
si = Sink("sink")
co = Countertop("countertop")

ki = kitchen(st,fr,si,co)
print(ki.stove.name)
