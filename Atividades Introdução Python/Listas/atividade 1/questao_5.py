lista_completa = []

for i in range(0,20):
    numero = float(input('Insira um numero: '))
    lista_completa.append(numero)

lista_par = [x for x in lista_completa if x % 2 == 0]
lista_impar = [x for x in lista_completa if x % 2 != 0]

print(f'lista par {lista_par}')
print(f'lista impar {lista_impar}')

