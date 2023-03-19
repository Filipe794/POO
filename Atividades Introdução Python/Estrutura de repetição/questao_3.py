qnt = int(input('insira a quantidade de numeros a serem inseridos: '))
cont=1
for i in range(qnt):
    num = int(input('insira um numero: '))
    if i == 0:
        maior = num
    elif num > maior:
        maior = num
        cont=1
    elif num == maior:
        cont+=1
print(f'o maior numero lido foi {maior} e foi inserido {cont} vezes')
    