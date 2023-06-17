from classes import *
from persistencia import *

codigo_viagem = 0
codigo_abastecimento = 0
codigo_manutencao = 0

def menu():
    print('\n')
    print('Escolha uma opcao: ')
    print('1- Gerenciamento de Motoristas')
    print('2- Gerenciamento de Veiculos')
    print('3- Gerenciamento de Viagem')
    print('4- Registrar Abastecimento')
    print('5- Registrar Manuntencao')
    print('6- Relatorio')
    print('7- Desviar Dinheiro')
    print('0- Sair')
    op = int(input())
    return op

def submenu_motoristas():
       print('\n')
       print('a- Cadastrar Novo Motorista')
       print('b- Pesquisar Motorista')
       print('c- Editar Motorista')
       print('d- Deletar Motorista')
       op = input('Escolha uma opcao: ')
       return op

def submenu_veiculos():
       print('\n')
       print('a- Cadastrar Veiculo')
       print('b- Pesquisar Veiculo')
       print('c- Editar Veiculo')
       print('d- Deletar Veiculo')
       print('e- Ver Quilometragem de Veiculo')
       op = input('Escolha uma opcao: ')
       return op

def submenu_viagem():
       print('\n')
       print('a- Cadastrar Viagem')
       print('b- Pesquisar Editar Viagem')
       op = input('Escolha uma opcao: ')
       return op

def cadastro_motorista():
    print('\nInsira os dados do motorista\n')

    nome = input('Nome: ')
    while nome == '':
        print('Nome não pode ser vazio, insira novamente')
        nome = input('Nome: ')

    cpf = input('CPF: ')
    while cpf == '':
        print('CPF não pode ser vazio, insira novamente')
        cpf = input('CPF: ')

    rg = input('RG: ')
    while rg == '':
        print('RG não pode ser vazio, insira novamente')
        rg = input('RG: ')

    cnh = input('CNH: ')
    while cnh == '':
        print('CNH não pode ser vazio, insira novamente')
        cnh = input('CNH: ')

    motorista = Motoristas(nome,cpf,rg,cnh)
    return motorista

def pesquisar_motorista():
       cpf = input('Insira o cpf do motorista: ')
       motorista = dao_motorista.pesquisar(cpf)
       if motorista:
              return motorista
       else:
              print('Motorista não encontrado\n')

def editar_motorista(motorista):
     dao_motorista.edit(motorista)

def deletar_motorista(motorista):
     dao_motorista.delete(motorista)

def cadastro_veiculo():
    print('\nInsira os dados do veiculo\n')

    marca = input('Marca: ')      
    while marca == '':
        print('Marca não pode ser vazio, insira novamente')
        marca = input('Marca: ')
    modelo = input('Modelo: ')      
    while modelo == '':
        print('Modelo não pode ser vazio, insira novamente')
        marca = input('Modelo: ')
    ano = input('Ano: ')
    while ano == '':
        print('Ano não pode ser vazio, insira novamente')
        ano = input('Ano: ')
    chassi = input('chassi: ')
    while chassi == '':
        print('Chassi não pode ser vazio, insira novamente')
        chassi = input('Chassi: ')
    placa = input('Placa: ')
    while placa == '':
        print('Placa não pode ser vazio, insira novamente')
        placa = input('Placa: ')
    cor = input('Cor: ')
    while cor == '':
        print('Cor não pode ser vazio, insira novamente')
        cor = input('Cor: ')
    km = float(input('Quilometragem: '))
    while km == '':
        print('Quilometragem não pode ser vazio, insira novamente')
        km = float(input('Quilometragem: '))
    
    veiculo = Veiculos(marca,modelo,ano,chassi,cor,placa)
    return veiculo

def pesquisar_veiculo():
    placa = input('Insira a placa do veiculo: ')
    veiculo = dao_veiculo.pesquisar(placa)
    if veiculo:
         return veiculo
    else:
         print("Veiculo nao encontrado")

def editar_veiculo(veiculo):
     dao_veiculo.edit(veiculo)

def deletar_veiculo(veiculo):
     dao_veiculo.delete(veiculo)

def cadastrar_viagem(motorista, veiculo,codigo_viagem):
       print('\nInsira os dados da viagem\n')

       destino = input('Destino: ')
       while destino == '':
              print('Destino não pode ser vazio, insira novamente')
              destino = input('Destino: ')
       origem = input('Origem: ')
       while origem == '':
              print('Origem não pode ser vazio, insira novamente')
              origem = input('Origem: ')
       
       km = float(input('Distancia percorrida: '))
       while km == '':
              print('Distancia percorrida não pode ser vazia, insira novamente')
              km = float(input('Distancia percorrida: '))

       print(f"Codigo da viagem: {codigo_viagem}")
       viagem = Viagens(destino,origem,km,motorista,veiculo,codigo_viagem)
       return viagem

def pesquisar_viagem():
     codigo = input("Insira o codigo da viagem: ")
     viagem = dao_viagens.pesquisar(codigo)
     if viagem:
          return viagem
     else:
          print("Viagem nao encontrada")

def editar_viagem(viagem: dict):
    dao_viagens.edit(viagem)

def registrar_abastecimento(codigo_abastecimento):
       print('\nInsira os dados do abastecimento\n')

       veiculo = pesquisar_veiculo()

       valor = float(input('Valor abastecido: '))
       while valor == '':
              print('Valor abastecido não pode ser vazio, insira novamente')
              valor = float(input('Valor abastecido: '))

       data = input('Data do abastecimento: ')
       while data == '':
              print('Data do abastecimento não pode ser vazio, insira novamente')
              data = input('Data do abastecimento: ')

       quantidade = float(input('Quantidade abastecida: '))
       while quantidade == '':
              print('Quantidade abastecida não pode ser vazio, insira novamente')
              quantidade = float(input('Quantidade abastecida: '))
       
       abastecimento = Abastecimento(veiculo,valor,data,quantidade)
       print(f"O codigo do abastecimento é {codigo_abastecimento}")
       return abastecimento

def registrar_manutencao(codigo_manutencao):
       print('\nInsira os dados da manutencao\n')

       veiculo = pesquisar_veiculo()

       custo = float(input('Custo: ') )
       while custo == '':
              print('Custo  não pode ser vazio, insira novamente')
              custo = float(input('Custo: ') )

       data = input('Data da manutenção: ')
       while data == '':
              print('Data da manutenção não pode ser vazia, insira novamente')
              data = input('Data da manutenção: ')

       tipo = input('Tipo da manutencao: ')
       while tipo == '':
              print('Tipo da manutencao não pode ser vazio, insira novamente')
              tipo = input('Tipo da manutencao: ')

       manutencao = Manutencao(veiculo,data,tipo,custo)
       print(f"O codigo da manutencao é {codigo_manutencao}")
       return manutencao



#-------------------------------------------------------------------------------#
loop = True
while loop:
    op = menu()
    # Gerenciamento de Motoristas
    if op == 1:
        op_2 = submenu_motoristas()
        if op_2 == 'a':
            motorista = cadastro_motorista()
            dao_motorista.add(motorista)
    if op_2 == 'b':
        if len(motoristas) != 0:
            motorista = pesquisar_motorista()
            if motorista:
                print(motorista)
        else:
            print("Não há motoristas cadastrados")
    if op_2 == 'c':
        if len(motoristas) != 0:
            motorista = pesquisar_motorista()
            if motorista:
                editar_motorista(motorista)
        else:
            print("Não há motoristas cadastrados")
    if op_2 == 'd':
        if len(motoristas) != 0:
            motorista = pesquisar_motorista()
            if motorista:
                deletar_motorista(motorista)
        else:
            print("Não há motoristas cadastrados")
    # Gerenciamento de Veiculos
    if op == 2:
        op_2 = submenu_veiculos()
        if op_2 == 'a':
            veiculo = cadastro_veiculo()
            dao_veiculo.add(veiculo)
        if op_2 == 'b':
            if len(veiculos) != 0:
                veiculo = pesquisar_veiculo()
                if veiculo:
                    print(veiculo)
            else:
                print("Não há veiculos cadastrados") 
        if op_2 == 'c':
            if len(veiculos) != 0:
                veiculo = pesquisar_veiculo() 
                if veiculo:
                    editar_veiculo(veiculo)
            else:
                print("Não há veiculos cadastrados") 
        if op_2 == 'd':
            if len(veiculos) != 0:
                veiculo = pesquisar_veiculo() 
                if veiculo:
                    deletar_veiculo(veiculo)
            else:
                print("Não há veiculos cadastrados") 
        # if op_2 == 'e':
        #     if len(veiculos) != 0:
        #         km_veiculo(pesquisar_veiculo())
        #     else:
        #         print("Não há veiculos cadastrados") 
    # Gerenciameto de Viagens
    if op == 3:
        if len(veiculos) != 0 and len(motoristas) != 0:
            op = submenu_viagem()
            if op == 'a':
                codigo_viagem += 1
                motorista = pesquisar_motorista()
                veiculo = pesquisar_veiculo()
                if veiculo and motorista:
                    cadastrar_viagem(motorista, veiculo, codigo_viagem)
            if op == 'b':
                if len(viagens) != 0:
                    viagem = pesquisar_viagem()
                    if viagem:
                        editar_viagem(viagem)
                else:
                    print("Não há viagens cadastradas")
        else:
            print("Não há veiculos ou motoristas suficientes")
       # Registrar Abastecimento
    if op == 4:
        if len(veiculos) != 0:
            codigo_abastecimento += 1
            abastecimento = registrar_abastecimento(codigo_abastecimento)
            dao_abastecimento.add(abastecimento)
        else:
            print("Não há veiculos cadastrados")
       # Registrar Manutencao
    if op == 5:
        if len(veiculos) != 0:
            codigo_manutencao += 1
            manutencao  = registrar_manutencao(codigo_manutencao)
            dao_manutencao.add(manutencao)
        else:
            print("Não há veiculos cadastrados")
    #    # Relatorio
    #    if op == 6:
    #         relatorio()
    if op == 0:
        loop = False