# Build a very basic Pokémon class that allows you to simulate battles
# in a Rock-Paper-Scissors game mechanic, as well as feed your Pokémon.
#
# The class should follow these specifications:
#
# - Each Pokemon should have a `name`, `primary_type`, `max_hp` and `hp`
# - Primary types should be limited to `water`, `fire` and `grass`
# - Implement a `battle()` method based on rock-paper-scissors that
#   decides who wins based only on the `primary_type`:
#       water > fire > grass > water
# - Display messages that explain who won or lost a battle
# - If a Pokemon loses a battle, they lose some of their `hp`
# - If you call the `feed()` method on a Pokemon, they regain some `hp`


from typing import Any


class Pokemon:

    allowed_types = ["water","fire","grass"]

    def __init__(self, name:str, type:"water""fire""grass", max_hp, hp):
        if type not in self.allowed_types:
            print(f"{type} is not a valid type. please chose one of the following: {', '.join(self.allowed_types)}")
            pass
        else:
            self.type = type
        self.name = name
        self.max_hp = max_hp
        self.hp = hp    


    def battle(self,other):

        if (self.type == "water" and other.type == "fire") or (self.type == "fire" and other.type == "grass") or (self.type == "grass" and other.type == "water"):
            print("You won")
            other.hp -= 2
        elif (self.type == "water" and other.type == "grass") or (self.type == "fire" and other.type == "water") or (self.type == "grass" and other.type == "fire"):
            print("You lost")
            self.hp -= 2
        elif (self.type == "water" and other.type == "water") or (self.type == "fire" and other.type == "fire") or (self.type == "grass" and other.type == "grass"):
            print("It's a tie")
            self.hp -= 1
            other.hp -= 1

    def feed(self,amount = 1):
        if self.hp >= self.max_hp:
            print(f"{self.name} health is full")
        else:
            temp_hp = self.hp
            self.hp += amount
            print(f"{self.name} health is {self.hp}, up from {temp_hp}")

    def __str__(self):
        return f"Pokemon = {self.name}. Type = {self.type}. Max hp = {self.max_hp}. Hp = {self.hp}"




    