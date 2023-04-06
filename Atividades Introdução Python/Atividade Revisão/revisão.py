# dicionario para cada funcionario
funcionario = {}
# lista para armazenar cada funcionario
funcionarios = []


def cadastro_funcionario():
    print('\nInsira os dados do funcionario\n')

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
        if telefone == 'sair':
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
            print('\nNome:', funcionario["nome"])
            print('CPF:', funcionario["cpf"])
            print('Cargo:', funcionario["cargo"])
            print('Salario:', funcionario["salario"])
            print('Telefones: ')
            for telefone in funcionario["telefones"]:
                print(' - ', telefone)
            print('\n')
            return
    print('Funcionário não encontrado\n')


def cadastrar_telefone():
    cpf = input('Insira o cpf do funcionario: ')
    for funcionario in funcionarios:
        if funcionario["cpf"] == cpf:
            telefone = input('\nInsira o novo telefone: ')
            if telefone != '':
                        funcionario["telefones"].append(telefone)
                        print('\nTelefone cadastrado com sucesso\n')
            else:
                        print('\nTelefone nao pode ser vazio')
            return
    print('\nFuncionário não encontrado\n')


def menu_editar():
    print('O que voce deseja fazer?')
    print('1- Atualizar Nome')
    print('2- Adicionar um telefone')
    print('3- Remover um telefone')
    print('4- Atualizar cargo')
    print('5- Atualizar salario')
    print('0- Sair')
    op = int(input('\nEscolha uma opcao: '))
    print('\n')
    return op
    


def editar_dados():
    cpf = input('Insira o cpf do funcionario: ')
    for funcionario in funcionarios:
        if funcionario["cpf"] == cpf:
            while True:
                op = menu_editar()
                if op == 1:
                    nome = input('\nDigite o novo nome: ')
                    if nome != '':
                        funcionario["nome"] = nome
                        print('Nome atualizado com sucesso\n')
                    else:
                        print('\nNome nao pode ser vazio')
                elif op == 2:
                    telefone = input('\nInsira o novo telefone: ')
                    if telefone != '':
                        funcionario["telefones"].append(telefone)
                        print('Telefone atualizado com sucesso\n')
                    else:
                        print('\nTelefone nao pode ser vazio\n')
                elif op == 3:
                    telefone = input('Insira o telefone a ser removido: ')
                    if telefone in funcionario["telefones"]:
                        funcionario["telefones"].remove(telefone)
                        print('Telefone removido com sucesso\n')
                    else:
                        print('\nTelefone nao encontrado\n')
                elif op == 4:
                    cargo = input('Insira o novo cargo: ')
                    if cargo != '':
                        funcionario["cargo"] = cargo
                        print('Cargo atualizado com sucesso\n')
                    else:
                        print('Cargo nao pode ser vazio\n')
                elif op == 5:
                    salario = float(input('Insira o novo salario: '))
                    if salario != '':
                        funcionario["salario"] = salario
                        print('Salario atualizado com sucesso\n')
                    else:
                        print('\nSalario nao pode ser vazio\n')
                elif op == 0:
                    return
                else:
                    print('Opção inválida!')


def deletar_funcionario():
    cpf = input('Insira o cpf do funcionario: ')
    for funcionario in funcionarios:
        if funcionario["cpf"] == cpf:
            funcionarios.remove(funcionario)
            print('\nFuncionario removido\n')
            return
    print('\nFuncionario nao encontrado\n')


def menu():
    print('\n')
    print('1- Cadastro de Funcionários')
    print('2- Pesquisar funcionário')
    print('3- Cadastrar novo telefone')
    print('4- Editar dados do Funcionário')
    print('5- Deletar funcionário')
    print('0- Sair')
    op = int(input('Escolha uma opcao: '))
    return op


def main():
    while True:
        op = menu()
        if op == 1:
            cadastro_funcionario()
        elif op == 2:
            if len(funcionarios) == 0:
                print("Nao ha funcionarios cadastrados\n")
            else:
             pesquisar_funcionario()
        elif op == 3:
            if len(funcionarios) == 0:
                print("Nao ha funcionarios cadastrados\n")
            else:
             cadastrar_telefone()
        elif op == 4:
            if len(funcionarios) == 0:
                print("Nao ha funcionarios cadastrados\n")
            else:
                editar_dados()
        elif op == 5:
            if len(funcionarios) == 0:
                print("Nao ha funcionarios cadastrados\n")
            else:
             deletar_funcionario()
        elif op == 0:
             return
        else:
            print('\nOpção inválida!')

main()