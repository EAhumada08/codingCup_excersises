def validate_possibility (cadena_S, cadena_X) :
    for index_x, item_x in enumerate(cadena_X) :
        count = 0

        for index_s, item_s in enumerate(cadena_S) :
            if(item_x.lower == item_s.lower) :
                count += 1
            print(item_s, item_x)

        print(count)
        if(count > 1) :
            is_possible = False
            break
        is_possible = True

    return is_possible


while True :
    aux_cadena_S = ''

    cadena_S = input()
    if(cadena_S == '0') :
        break
    cadena_X = input()
    if(cadena_X == '0') :
        break
    
    aux_cadena_S = cadena_S

    is_possible = validate_possibility(cadena_S, cadena_X)
    if( is_possible is False) :
        print('IMPOSSIBLE')
    else:
        for index, item in enumerate(cadena_S) :
            if(item == cadena_X[0]) :
                pre = index
            if(item == cadena_X[-1]) :
                su = index

        aux_cadena_S = cadena_S[pre : su + 1]
        print(aux_cadena_S)
        print("POSSIBLE")


