from pokemon_game import Pokemon as pk

fry = pk("fry","grass",5,5)
bristine = pk("bristine","fire",5,5)

fry.battle(bristine)
    
print(fry)

fry.feed()
fry.feed(5)

print(fry)