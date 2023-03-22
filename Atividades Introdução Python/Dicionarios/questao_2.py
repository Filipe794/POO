pessoas = {}

num_pessoas = int(input('Insira a quantidade de pessoas a serem cadastradas: '))

for i in range(num_pessoas):
    print(f'Cadastro da pessoa {i+1}')
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    cpf = input('CPF: ')
    pessoas[cpf] = {"nome": nome, "idade": idade, "cpf": cpf}

menores = {}
deletar = []

for cpf,pessoa in pessoas.items():
    if pessoa["idade"] < 18:
        menores[cpf] = pessoa
        deletar.append(cpf)
for i in deletar:
    del pessoas[i]

print(f'Pessoas maiores de 18 anos')
print(pessoas)
print(f'Pessoas menores de 18 anos')
print(menores)