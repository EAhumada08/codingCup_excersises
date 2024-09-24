puntajes = input()

puntaje_E = int(puntajes.split()[0])
puntaje_K = int(puntajes.split()[1])

if(puntaje_E > puntaje_K) :
    print('ESPINO')
if(puntaje_K > puntaje_E) :
    print('KAREL')
if(puntaje_E == puntaje_K) :
    print('EMPATE')