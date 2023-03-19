pessoas = {}
principal = {}
backup = {}

i = 0
cont = 0
while i != 0:
    print(f'Cadastro da pessoa {i+1}')
    nome = input('Nome: ')
    pessoa = {"nome": nome}
    pessoas[nome] = pessoa
    backup[nome] = pessoa
    i = int(input('Digite 1 para continuar inserindo ou 0 para parar de inserir: '))
    cont+=1
    if cont % 5 == 0:
        print(principal)
        principal.clear()
