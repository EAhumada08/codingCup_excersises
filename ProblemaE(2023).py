def valor_mas_repetido (array) :
    conteo = {}

    for sublista in array :
        for elemento in sublista :
            if elemento in conteo :
                conteo[elemento] += 1
            else :
                conteo[elemento] = 1
    #print(conteo)
    max_valor = max(conteo.values())
    #print(max_valor)
    for clave , valor in conteo.items():
        if valor == max_valor :
            return clave
        
def promedio_general (array) :
    acum = 0
    elemnts = 0
    for sublist in array:
        for elemento in sublist:
            acum = acum + elemento
            elemnts += 1 
    promedio = acum/elemnts
    return promedio

def promedio_plantel (array):
    acum = 0
    elemnts = 0

    for elemento in array:
        acum += elemento
        elemnts += 1

    promedio = acum/elemnts
    return promedio

def moda_plantel (array) :
    conteo = {}

    for elemento in array:
        if elemento in conteo:
            conteo[elemento] += 1
        else:
            conteo[elemento] = 1
    
    max_valor = max(conteo.values())
    for clave, valor in conteo.items():
        if valor == max_valor:
            return clave

def mat_aprobadas (array) :
    aprobadas = 0
    for elemento in array:
        if elemento >= 70 :
            aprobadas += 1
    return aprobadas

def mat_reprobadas (array) :
    reprobadas = 0
    for elemento in array:
        if elemento < 70 :
            reprobadas += 1
    return reprobadas

numero_de_campus = input()

califs_grl = []
for i in range(0, int(numero_de_campus)) :
    cantidad_calif = input()

    califs_input = input()

    califs = califs_input.split()

    for j in range(0,len(califs)) :
        if int(califs[j]) < 70 :
            califs[j] = 0
        else : 
            califs[j] = int(califs[j])
    califs_grl.append(califs)

#print(califs_grl)

print(promedio_general(califs_grl))
print(valor_mas_repetido(califs_grl))

for array in califs_grl:
    print(f"{promedio_plantel(array)} {moda_plantel(array)} {mat_aprobadas(array)} {mat_reprobadas(array)}")
#for i in range(0, len(califs_grl)) :
#   for j in range(0, len(califs_grl[i])) :
#       print(califs_grl[i][j])