from collections import Counter
while True:
    S = input("")
    if S == "0":
        break
    X = input("")
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

#--------Funcionamiento de la libreria----------------------     
#import collections
#print collections.Counter(['a', 'b', 'c', 'a', 'b', 'b'])
#print collections.Counter({'a':2, 'b':3, 'c':1})
#print collections.Counter(a=2, b=3, c=1)