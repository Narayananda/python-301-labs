class Ingredient:
    """Models a food item used as an ingredient."""
    
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def expire(self):
        """Expired the ingredient"""
        self.name = 'expired' + self.name
        print(f'The {self.name} has expired')
    
    def use(self, use_amount):
        print(f"you've used {use_amount} {self.name}")
        self.amount -= use_amount
    
    
    def __repr__(self):
        return f"Ingredient(name={self.name}, amount={self.amount})"

    def __str__(self):
        return f'{self.name}({self.amount})'

i = Ingredient("peas",5)


print(i.use(3))
print(i)