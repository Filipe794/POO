agenda = {}
i = int(input('Insira a quantidade de contatos: '))
contatos = []
for j in range(i):
    contatos.append(agenda={
        "cpf": input('Insira seu cpf: '),
        "nome": input('Insira seu nome: '),
        "idade": int(input('Insira sua idade: ')),
        "telefone": input('Insira seu telefone: ')
    })
print(contatos)
# dic.update() - fazer um dicionario aninhado
# contatos = {}
# for j in range(i):
#     contatos.update({i:{ usando o i como chave dos dicionarios
#         "cpf": input('Insira seu cpf: '),
#         "nome": input('Insira seu nome: '),
#         "idade": int(input('Insira sua idade: ')),
#         "telefone": input('Insira seu telefone: ')
#     }
#     })
# print(contatos)