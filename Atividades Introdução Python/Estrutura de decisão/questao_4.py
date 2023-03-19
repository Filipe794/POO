nota_1 = float(input('insira a nota 1: '))
nota_2 = float(input('insira a nota 2: '))

if (nota_1 > 0 and nota_1 < 10) and (nota_2 > 0 and nota_2 < 10):
    print ('a média é:', (nota_1 + nota_2)/2)
else:
    print('notas inválidas')