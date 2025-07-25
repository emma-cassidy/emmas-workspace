#Pokemon Types Chart correct for games from 2013 onwards

print("Welcome to the Pokemon type checker!")
poke_type1 = input("Please enter attacking Pokemon type: ").lower()
poke_type2 = input("Please enter defending Pokemon type: ").lower()

if poke_type1 == "normal":
    if poke_type2 == "ghost":
        print("This move has no effect!")
    elif poke_type2 == "rock" or poke_type2 == "steel":
        print("Not very effective...")
    else:
        print("Neutral damage.")
elif poke_type1 == "fire":
    if poke_type2 == "grass" or poke_type2 == "ice" or poke_type2 == "bug" or poke_type2 == "steel":
        print("It's super effective!")
    elif poke_type2 == "fire" or poke_type2 == "water" or poke_type2 == "rock" or poke_type2 == "dragon":
        print("It's not very effective...")
    else:
        print("Neutral damage.")
elif poke_type1 == "water":
    if poke_type2 == "fire" or poke_type2 == "ground" or poke_type2 == "rock":
        print("It's super effective!")
    elif poke_type2 == "water" or poke_type2 == "grass" or poke_type2 == "dragon":
        print("It's not very effective...")
    else:
        print("Neutral damage.")
elif poke_type1 == "electric":
    if poke_type2 == "water" or poke_type2 == "flying":
        print("It's super effective!")
    elif poke_type2 == "electric" or poke_type2 == "grass" or poke_type2 == "dragon":
        print("It's not very effective...")
    elif poke_type2 == "ground":
        print("This move has no effect!")
    else:
        print("Neutral damage.")
elif poke_type1 == "grass":
    if poke_type2 == "water" or poke_type2 == "ground" or poke_type2 == "rock":
        print("It's super effective!")
    elif poke_type2 == "fire" or poke_type2 == "grass" or poke_type2 == "poison" or poke_type2 == "flying":
        print("It's not very effective...")
    elif poke_type2 == "bug" or poke_type2 == "dragon" or poke_type2 == "steel":
        print("It's not very effective...")
    else:
        print("Neutral damage.")
elif poke_type1 == "ice":
    if poke_type2 == "grass" or poke_type2 == "ground" or poke_type2 == "flying" or poke_type2 == "dragon":
        print("It's super effective!")
    elif poke_type2 == "fire" or poke_type2 == "water" or poke_type2 == "ice" or poke_type2 == "steel":
        print("It's not very effective...")
    else:
        print("Neutral damage.")
elif poke_type1 == "fighting":
    if poke_type2 == "normal" or poke_type2 == "ice" or poke_type2 == "rock" or poke_type2 == "dark" or poke_type2 == "steel":
        print("It's super effective!")
    elif poke_type2 == "poison" or poke_type2 == "psychic" or poke_type2 == "bug" or poke_type2 == "flying" or poke_type2 == "fairy":
        print("It's not very effective...")
    elif poke_type2 == "ghost":
        print("This move has no effect!")
    else:
        print("Neutral damage.")
elif poke_type1 == "poison":
    if poke_type2 == "grass" or poke_type2 == "fairy":
        print("It's super effective!")
    elif poke_type2 == "poison" or poke_type2 == "ground" or poke_type2 == "rock" or poke_type2 == "ghost":
        print("It's not very effective...")
    elif poke_type2 == "steel":
        print("This move has no effect!")
    else:
        print("Neutral damage.")
elif poke_type1 == "ground":
    if poke_type2 == "fire" or poke_type2 == "electric" or poke_type2 == "poison" or poke_type2 == "rock" or poke_type2 == "steel":
        print("It's super effective!")
    elif poke_type2 == "grass" or poke_type2 == "bug":
        print("It's not very effective...")
    elif poke_type2 == "flying":
        print("This move has no effect!")
    else:
        print("This move has no effect!")
elif poke_type1 == "flying":
    if poke_type2 == "grass" or poke_type2 == "fighting" or poke_type2 == "bug":
        print("It's super effective!")
    elif poke_type2 == "electric" or poke_type2 == "rock" or poke_type2 == "steel":
        print("It's not very effective...")
    else:
        print("Neutral damage.")
elif poke_type1 == "psychic":
    if poke_type2 == "fighting" or poke_type2 == "poison":
        print("It's super effective!")
    elif poke_type2 == "psychic" or poke_type2 == "steel":
        print("It's not very effective...")
    elif poke_type2 == "dark":
        print("This move has no effect!")
    else:
        print("Neutral damage.")
elif poke_type1 == "bug":
    if poke_type2 == "grass" or poke_type2 == "psychic" or poke_type2 == "dark":
        print("It's super effective!")
    elif poke_type2 == "fire" or poke_type2 == "fighting" or poke_type2 == "poison" or poke_type2 == "flying":
        print("It's not very effective...")
    elif poke_type2 == "ghost" or poke_type2 == "steel" or poke_type2 == "fairy":
        print("It's not very effective...")
    else:
        print("Neutral damage.")
elif poke_type1 == "rock":
    if poke_type2 == "fire" or poke_type2 == "ice" or poke_type2 == "flying" or poke_type2 == "bug":
        print("It's super effective!")
    elif poke_type2 == "fighting" or poke_type2 == "ground" or poke_type2 == "steel":
        print("It's not very effective...")
    else:
        print("Neutral damage.")
elif poke_type1 == "ghost":
    if poke_type2 == "psychic" or poke_type2 == "ghost":
        print("It's super effective!")
    elif poke_type2 == "dark":
        print("It's not very effective...")
    elif poke_type2 == "normal":
        print("This move has no effect!")
    else:
        print("Neutral damage.")
elif poke_type1 == "dragon":
    if poke_type2 == "dragon":
        print("It's super effective!")
    elif poke_type2 == "steel":
        print("It's not very effective...")
    elif poke_type2 == "fairy":
        print("This move has no effect!")
    else:
        print("Neutral damage.")
elif poke_type1 == "dark":
    if poke_type2 == "psychic" or poke_type2 == "ghost":
        print("It's super effective!")
    elif poke_type2 == "fighting" or poke_type2 == "dark" or poke_type2 == "fairy":
        print("It's not very effective...")
    else:
        print("Neutral damage.")
elif poke_type1 == "steel":
    if poke_type2 == "ice" or poke_type2 == "rock" or poke_type2 == "fairy":
        print("It's super effective!")
    elif poke_type2 == "fire" or poke_type2 == "water" or poke_type2 == "electric" or poke_type2 == "steel":
        print("It's not very effective...")
elif poke_type1 == "fairy":
    if poke_type2 == "fighting" or poke_type2 == "dragon" or poke_type2 == "dark":
        print("It's super effective!")
    elif poke_type2 == "fire" or poke_type2 == "poison" or poke_type2 == "steel":
        print("It's not very effective...")
    else:
        print("Neutral damage.")
else:
    print("Please enter a valid type!")