numero = int(input('informe um numero entre 100 e 999'))
while numero < 100 or numero > 999:
    print('numero invalido')
    numero = int(input('informe um numero entre 100 e 999'))
print(numero//100)
num = numero%100
print(num//10)
num_2=num%10
print(num_2)