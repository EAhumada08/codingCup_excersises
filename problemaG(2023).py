import datetime

def transponer(datos) :
    datos_transpuestos = [[fila[i] for fila in datos] for i in range(len(datos[0]))]
    return datos_transpuestos

def comprar (productos) :
    fechas_id = [(id_product, datetime.datetime.strptime(fecha, '%Y-%m-%d')) for id_product, fecha in productos.items()]

    productos_ordenados = sorted(fechas_id, key=lambda x: x[1])

    for id, fecha in productos_ordenados :
        print(id, fecha.strftime('%Y-%m-%d'))
    
    return productos_ordenados

def imprimir (productos):
    lista_datos = [productos[i:i+5] for i in range(0,len(productos),5)]
    
    for fila in lista_datos:
        while len(fila) < 5:
            fila.insert(0,0)

    for fila in transponer(lista_datos):
        for elemento in fila:
            if elemento == 0:
                vacio=""
                print(f"{vacio:5}", end="")
            else:
                print(f"{elemento[0]:5}", end="")
        print()

cant_op = input()

for i in range(0,int(cant_op)) :
    tipo_op_input = input()

    if tipo_op_input.split()[0].upper() == 'C' :
        products = {}
        for i in range(0, int(tipo_op_input.split()[1])) :
           product_input = input()
           products[product_input.split()[0]] = product_input.split()[1]
        comprados = comprar(products)
    
    if tipo_op_input.split()[0].upper() == 'E' :
        imprimir(comprados)
           

