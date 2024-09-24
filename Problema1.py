from collections import Counter

def validate_Posible(S,X):
    cuenta_S = Counter(S)
    cuenta_X = Counter(X)

    es_posible = True
    for letra in X:
        if cuenta_S[letra] > cuenta_X[letra]: 
            es_posible = False
            break
    if es_posible:
        print("POSIBLE")
    else:
        print("IMPOSIBLE")


while True:
    S = input("")
    if S == "0":
        break
    X = input("")
    if X == '0' :
        break

    char_delete = input()

    if(char_delete) :
        auxS = S.replace(char_delete, "")
        cuenta_auxS = Counter(auxS)
        cuenta_X = Counter(X)

        es_posible = True
        for letra in X:
            if cuenta_auxS[letra] < cuenta_X[letra]: 
                es_posible = False
                break
        if es_posible:
            print(auxS)
            print("POSIBLE")
        else:
            print(auxS)
            print("IMPOSIBLE")

    else :
        validate_Posible(S,X)
        
#--------Funcionamiento de la libreria----------------------     
#import collections
#print collections.Counter(['a', 'b', 'c', 'a', 'b', 'b'])
#print collections.Counter({'a':2, 'b':3, 'c':1})
#print collections.Counter(a=2, b=3, c=1)