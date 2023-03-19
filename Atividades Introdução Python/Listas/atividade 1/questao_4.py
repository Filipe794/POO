lista = []
vogal = ['a','e','i','o', 'u']
cont = 0
for i in range(0,10):
    caracter = input('Insira um caracter: ')
    if caracter not in vogal:
        lista.append(caracter)
        cont+=1
print(lista)
print(f'foram lidas {cont} consoantes')