import webbrowser

class Ingredient:

    def __init__(self, name, amount):
          self.name = name
          self.amount =  amount

    def get_info(self):
         webbrowser.open_new(f"https://en.wikipedia.org/wiki/{self.name}")

    def get_recipe(self):
         webbrowser.open_new(f"https://www.allrecipes.com/search?q={self.name}")


    def __str__(self):
         return f"{self.name}. Amount: {self.amount}"
         

apple = Ingredient("apple",4)

apple.get_recipe()