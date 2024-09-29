number_of_potions = 0
potions = []

number_of_potions = input()

val_potions = input()
potions = val_potions.split()

while  len(potions) != int(number_of_potions) :
    print(len(potions))
    val_potions = input()
    potions = val_potions.split()

valores = input()

health_points = int(valores.split()[0])
turnos = int(valores.split()[1])
damage = int(valores.split()[2])

damage_turn = round(health_points / turnos)

for i in range(len(potions)) :
    if(health_points < health_points + int(potions[i])) :
        shield = round(damage - damage_turn)
        min_potions = 1
        break


print("POCIONES "+ str(min_potions) + " ESCUDO " + str(shield))

