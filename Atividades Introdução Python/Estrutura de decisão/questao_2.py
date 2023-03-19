num_1 = int(input('insira um numero: '))
num_2 = int(input('insira um numero: '))

if num_1 > num_2:
    print(num_1)
    print(num_1 - num_2)
elif num_1 < num_2:
    print(num_2)
    print(num_2 - num_1)
else:
    print('numero iguais')
    print(num_1 - num_2)