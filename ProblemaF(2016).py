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
    