string_to_evaluate = input()

resta = 0
suma = 0
if string_to_evaluate.find('+') > 0 :

    for i , add in enumerate(string_to_evaluate.split('+')) :
        print(add)
        if add.find('-') > 0 :
            strings_to_rest = add.split('-')
            for j in range(1 , len(strings_to_rest)) :
                resta = resta +  int(strings_to_rest[j-1]) - int(strings_to_rest[j]) 
                print("resta " + str(resta))
        else :
            suma = suma + int(add) 

    total = suma + resta
    
else: 
    print(string_to_evaluate)

print(total)