def sum (long, num) : 
    suma = 0
    for i in range(0, long ) :
        suma = suma + int(num[i])
    return suma

valores_AB = input()

valor_A = int(valores_AB.split()[0])
valor_B = int(valores_AB.split()[1])

nums = []

for num_index in range(valor_A, valor_B + 1) : 
    nums.append(num_index)

count = 0

for index,item in enumerate(nums) :
    num = str(nums[index])
    digits = len(num)
    acum = sum(digits, num)
    count = count + acum

    print(count)
    