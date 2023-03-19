notas = []
media = 0
for i in range(0,4):
    nota = int(input('Insira a nota do aluno: '))
    notas.append(nota)
    media = media + nota
print(f'notas: {notas}')
print(media/4)