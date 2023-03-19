salario = float(input('insira o salario: '))
prestacao = float(input('insira o valor da prestacao: '))

if prestacao > (salario * 0.2):
    print('Empréstimo não concedido')
else:
    print('Empréstimo concedido')