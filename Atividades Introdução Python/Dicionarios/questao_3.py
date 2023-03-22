principal = {}
backup = {}

i = 1
cont = 0
while i != 0:
    cont+=1
    print(f'Cadastro da pessoa {cont}')
    principal[cont] = {cont: input('Nome: ')}
    backup[cont] = principal[cont]
    if cont % 5 == 0:
        for indice,pessoa in principal.items():
            print(principal[indice])
        principal.clear()
    i = int(input('Digite 1 para continuar inserindo ou 0 para parar de inserir: '))
