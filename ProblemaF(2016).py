def sum (long, a) : 
    if long == 1 :
        return int(a)
    
    suma = 0
    for i in range(0, long ) :
        suma = suma + int(a[i])
        print(i)
    return suma


AB = input()

A = int(AB.split()[0])
B = int (AB.split()[1])

print(A)
print(B)

nums = []

for auxA in range(A,B+1) :
    num = auxA + 1 
    nums.append(auxA)

print(nums)

count = 0
for index,item in enumerate(nums) :
    a = str(nums[index])
    long = len(a)
    acum = sum(long, a)
    count = count + acum

    print(count)
    

""" 
valores=input("")
lista=valores.split(" ")
acumula=0

for x in range(int(lista[0]),int(lista[1])+1,1):
    if x<10:
        acumula=acumula+x
    else:
        convierte=str(x)
        total_car=len(convierte)
        if total_car==2:
            acumula=acumula+int(convierte[0])+int(convierte[1])
        elif total_car==3:
            acumula=acumula+int(convierte[0])+int(convierte[1])+int(convierte[2])
        elif total_car==4:
            acumula=acumula+int(convierte[0])+int(convierte[1])+int(convierte[2])+int(convierte[3])
        elif total_car==5:
            acumula=acumula+int(convierte[0])+int(convierte[1])+int(convierte[2])+int(convierte[3])+int(convierte[4])
        elif total_car==6:
            acumula=acumula+int(convierte[0])+int(convierte[1])+int(convierte[2])+int(convierte[3])+int(convierte[4])+int(convierte[5])
        elif total_car==7:
            acumula=acumula+int(convierte[0])+int(convierte[1])+int(convierte[2])+int(convierte[3])+int(convierte[4])+int(convierte[5])+int(convierte[6])
        elif total_car==8:
            acumula=acumula+int(convierte[0])+int(convierte[1])+int(convierte[2])+int(convierte[3])+int(convierte[4])+int(convierte[5])+int(convierte[6])+int(convierte[7])
        elif total_car==9:
            acumula=acumula+int(convierte[0])+int(convierte[1])+int(convierte[2])+int(convierte[3])+int(convierte[4])+int(convierte[5])+int(convierte[6])+int(convierte[7])+int(convierte[8])
        elif total_car==10:
            acumula=acumula+int(convierte[0])+int(convierte[1])+int(convierte[2])+int(convierte[3])+int(convierte[4])+int(convierte[5])+int(convierte[6])+int(convierte[7])+int(convierte[8])+int(convierte[9])
print(acumula)
"""