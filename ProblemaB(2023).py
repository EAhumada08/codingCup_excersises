def add (string_to_split) :
    suma = 0
    strings_to_add = string_to_split.split('+')

    #print(strings_to_add)

    for i in range(0, len(strings_to_add)) :
        #print("a sumar " + strings_to_add[i])
        if strings_to_add[i].find('-') > 0 :
            suma = suma + rest(strings_to_add[i])
        elif strings_to_add[i].find('*') > 0 :
            suma = suma + multiplicate(strings_to_add[i])  
        elif strings_to_add[i].find('/') > 0 :
            suma = suma + division(strings_to_add[i])         
        else :
            suma = suma + int(strings_to_add[i])
            #print("suma" + str(suma))

    return suma

def rest (string_to_split) :
    resta = 0
    strings_to_rest = string_to_split.split('-')

    for i in range(0, len(strings_to_rest)) :
        #print("a resta " + strings_to_rest[i])
        if strings_to_rest[i].find('*') > 0 :
            if resta == 0 :
                resta = resta + multiplicate(strings_to_rest[i])
            else :
                resta = resta - multiplicate(strings_to_rest[i])
        elif strings_to_rest[i].find('/') > 0 :
            if resta == 0 :
                resta = resta + division(strings_to_rest[i])
            else :
                resta = resta - division(strings_to_rest[i])
        else :   
            if resta == 0:
                resta = resta + int(strings_to_rest[i])
                #print("resta" + str(resta))
            else :
                resta = resta - int(strings_to_rest[i])
                #print("resta" + str(resta))

    #print("resta" + str(resta))
    return resta

def multiplicate (string_to_split) :
    strings_to_mult = string_to_split.split('*')
    mult = 0

    for i in range(0, len(strings_to_mult)) :
        #print("a mult " + str(strings_to_mult[i]))
        
        if strings_to_mult[i].find('/') > 0:
            if mult == 0 :
                mult = division(strings_to_mult[i]) * 1
            else :
                mult = mult * division(strings_to_mult[i])
        else :
            if mult == 0 :
                mult = int(strings_to_mult[i]) * 1
            else :
                mult = mult * int(strings_to_mult[i])
            #print("mult " + str(mult))

    return mult

def division (string_to_split) :
    strings_to_div = string_to_split.split('/')
    div = 0

    for i in range(1, len(strings_to_div)) :
        div = div + int(strings_to_div[i-1]) / int(strings_to_div[i])

    return div


total = 0

string_to_evaluate = input()

if string_to_evaluate.find('+') > 0 :
    total = add(string_to_evaluate)
elif string_to_evaluate.find('-') > 0 :
    total = rest(string_to_evaluate)
elif string_to_evaluate.find('*') > 0 :
    total = multiplicate(string_to_evaluate)
elif string_to_evaluate.find('/') > 0 :
    total = division(string_to_evaluate)

print(str(total))