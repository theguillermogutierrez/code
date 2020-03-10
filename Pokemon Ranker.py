from Pokemon import Pokemon as p
from Flamethrower import Flamethrower as fm

pokemon1 = p("Charizard", "Fire", 34, 10)
move1 = "Flamethrower"
fm.damage = 35
move = ""
wrong_move_count = 0
wrong_move_limit = 3
out_of_moves = False

Trainers = {}
Trainers[pokemon1] = "Ash Ketchum"

print("Pkmn Tnr: " + Trainers[pokemon1])

print("Pokemon: " + pokemon1.name)
print("     Type: " + pokemon1.type)
print("     Level: " + str(pokemon1.lvl))
print("     Health Points: " + str(pokemon1.hp))
print("     Fainted? " + str(pokemon1.is_fainted()))
print("     Evolutionary Stage Number: " + str(pokemon1.evolvl()))

while move != move1 and not(out_of_moves):
    if wrong_move_count < wrong_move_limit:
        move = input("Enter your move: ")
        wrong_move_count += 1
    else:
        out_of_moves = True
if out_of_moves:
    print("\nCharizard hurt itself in confusion!\nCharizard took 10 damage!")
    pokemon1.hp -= 10
else:
    print("")
    print(pokemon1.name + " used " + move + "!")
    print(pokemon1.name + " did " + str(fm.damage) + " damage!")
print("Pokemon Faint Status: " + str(pokemon1.is_fainted()))