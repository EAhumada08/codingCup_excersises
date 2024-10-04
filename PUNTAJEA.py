Puntajes = input("")
Espino = int(Puntajes.split()[0])
Karel = int(Puntajes.split()[1])
if 0 <= Espino <= 100 and 0 <= Karel <= 100:
    if Espino > Karel:
        print("ESPINO")
    if Karel > Espino:
        print("KAREL")
    if Karel == Espino:
        print("EMPATE")
else:
    print("Los puntajes deben de ser entre 0 y 100")