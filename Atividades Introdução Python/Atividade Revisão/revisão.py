# dicionario para cada funcionario
funcionario = {}
# lista para armazenar cada funcionario
funcionarios = []


def cadastro_funcionario():
    print('Insira os dados do funcionario')

    nome = input('Nome: ')
    while nome == '':
        print('Nome não pode ser vazio, insira novamente')
        nome = input('Nome: ')

    cpf = input('CPF: ')
    while cpf == '':
        print('CPF não pode ser vazio, insira novamente')
        cpf = input('CPF: ')

    cargo = input('Cargo: ')
    while cargo == '':
        print('Cargo não pode ser vazio, insira novamente')
        cargo = input('Cargo: ')

    salario = float(input('Salario: '))
    while salario == '':
        print('Salario não pode ser vazio, insira novamente')
        salario = float(input('Salario: '))

    telefones = []
    while True:
        telefone = input("Digite o telefone a ser cadastrado ou digite 'sair' para parar de inserir\n")
        if telefones == 'sair':
            break
        if telefone != '':
            telefones.append(telefone)
        else: 
            print('Telefone nao pode ser vazio')

    funcionario = {
        "nome": nome,
        "cpf": cpf,
        "cargo": cargo,
        "salario": salario,
        "telefones": telefones
    }

    funcionarios.append(funcionario)


def pesquisar_funcionario():
    cpf = input('Insira o cpf do funcionario: ')
    for funcionario in funcionarios:
        if funcionario["cpf"] == cpf:
            print('Nome:', funcionario["nome"])
            print('CPF:', funcionario["cpf"])
            print('Cargo:', funcionario["cargo"])
            print('Salario:', funcionario["salario"])
            print('Telefones: ')
            for telefone in funcionario["telefones"]:
                print(' - ', telefone)
            return
    print('Funcionário não encontrado\n')


def cadastrar_telefone():
    cpf = input('Insira o cpf do funcionario: ')
    for funcionario in funcionarios:
        if funcionario["cpf"] == cpf:
            telefone = input('Insira o novo telefone: ')
            if telefone != '':
                        funcionario["telefones"].append(telefone)
            else:
                        print('Telefone nao pode ser vazio')
            return
    print('Funcionário não encontrado\n')


def menu_editar():
    print('O que voce deseja fazer?')
    print('1- Atualizar Nome')
    print('2- Adicionar um telefone')
    print('3- Remover um telefone')
    print('4- Atualizar cargo')
    print('5- Atualizar salario')
    print('6- Sair')


def editar_dados():
    cpf = input('Insira o cpf do funcionario: ')
    for funcionario in funcionarios:
        if funcionario["cpf"] == cpf:
            while True:
                menu_editar()
                op = int(input())
                if op == 1:
                    nome = input('Digite o novo nome: ')
                    if nome != '':
                        funcionario["nome"] = nome
                    else:
                        print('Nome nao pode ser vazio')
                elif op == 2:
                    telefone = input('Insira o novo telefone: ')
                    if telefone != '':
                        funcionario["telefones"].append(telefone)
                    else:
                        print('Telefone nao pode ser vazio')
                elif op == 3:
                    telefone = input('Insira o teleofone a ser removido: ')
                    if telefone in funcionario["telefones"]:
                        funcionario["telefones"].remove(telefone)
                    else:
                        print('Telefone nao encontrado')
                elif op == 4:
                    cargo = input('Insira o novo cargo')
                    if cargo != '':
                        funcionario["cargo"] = cargo
                    else:
                        print('Cargo nao pode ser vazio')
                elif op == 5:
                    salario = float(input('Insira o novo cargo'))
                    if salario != '':
                        funcionario["salario"] = salario
                    else:
                        print('salario nao pode ser vazio')
                elif op == 6:
                    return
                else:
                    print('Opção inválida!')


def deletar_funcionario():
    