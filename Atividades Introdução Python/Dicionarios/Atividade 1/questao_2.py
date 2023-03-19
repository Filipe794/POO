info = {}
i = int(input('Insira a quantidade de dados a serem inseridos: '))
pessoa =[]    
for j in range(i):
    info ={
        "cpf": input('Insira seu cpf: '),
        "nome": input('Insira seu nome: '),
        "idade": int(input('Insira sua idade: '))
    }
    pessoa.append(info)

print(pessoa)

# for i in range(len(pessoa)):

