numero_casos = input()

for i in range(0, int(numero_casos)) :
    letras_disponibles = []
    palabra_verificar = []

    while len(letras_disponibles) < 1 or len(letras_disponibles) > 20 :
        letras_disponibles = input()
        #print(len(letras_disponibles))
    while len(palabra_verificar) < 1 or len(palabra_verificar) > 20 :
        palabra_verificar = input()

    count = []
    for index in range(0, len(palabra_verificar)) :
        count.append(0)

    for j in range(0, len(palabra_verificar)) :
        for k in range(0, len(letras_disponibles)) :
            if palabra_verificar[j].upper == letras_disponibles[k].upper :
                count[j] += 1

    if count.count(0) > 0 :
        print("LOSE")
    else :
        print("WIN")