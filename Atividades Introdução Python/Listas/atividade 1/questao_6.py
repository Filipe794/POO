lista_media = []
cont = 0
for i in range(0,10):
    media = 0
    print(f'notas aluno {i+1}: ')
    nota_1 = float(input('Insira a nota 1 do aluno: '))
    nota_2 = float(input('Insira a nota 2 do aluno: '))
    nota_3 = float(input('Insira a nota 3 do aluno: '))
    nota_4 = float(input('Insira a nota 4 do aluno: '))
    media = (nota_1+nota_2+nota_3+nota_4)/4
    lista_media.append(media)

for i in lista_media:
    if i >= 7.0:
        cont+=1

print(f'tiveram {cont} alunos com notas maior que 7')