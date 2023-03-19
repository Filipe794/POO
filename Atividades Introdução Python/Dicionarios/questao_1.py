agenda = {}
i = int(input('Insira a quantidade de pessoas a serem cadastradas: '))
contatos =[]    
for j in range(i):
    agenda ={
        "cpf": input('Insira seu cpf: '),
        "nome": input('Insira seu nome: '),
        "idade": int(input('Insira sua idade: ')),
        "telefone": input('Insira seu telefone: ')
    }
    contatos.append(agenda)

print(contatos)