pessoas = {}

num_pessoas = int(input('Insira a quantidade de pessoas a serem cadastradas: '))

for i in range(num_pessoas):
    print(f'Cadastro da pessoa {i+1}')
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    cpf = input('CPF: ')
    pessoa = {"nome": nome, "idade": idade, "cpf": cpf}
    pessoas[cpf] = pessoa

menores = {}

for cpf,pessoa in pessoa.items():
    if pessoa["idade"] < 18:
        menores[cpf] = pessoa
        del pessoas[cpf]

print(f'Pessoas maiores de 18 anos')
print(pessoas)
print(f'Pessoas menores de 18 anos')
print(menores)