veiculos={"BCC009":{"marca":"Fiat", "modelo":"UNO", "ano":"2003", 
                    "placa":"BCC009", "chassi":"36563652", "cor":"Branco","km":400},
         "BCC006":{"marca":"Fiat", "modelo":"Toro", "ano":"2003", 
                   "placa":"BCC006", "chassi":"36563652","cor":"Branco","km":600},
         "BCC008":{"marca":"Fiat", "modelo":"Argo", "ano":"2003",
                   "placa":"BCC007", "chassi":"36563652","cor":"Branco","km":600}  }

motoristas={"11111":{"nome":"François", "CPF":"11111", "RG":"223212", "CNH":"34221", "total_km": 400, "qnt_viagens":2},
            "22222":{"nome":"Ana", "CPF":"22222", "RG":"223212", "CNH":"34221", "total_km": 0, "qnt_viagens": 0},
            "33333":{"nome":"Maria", "CPF":"33333", "RG":"223212", "CNH":"34221", "total_km": 0, "qnt_viagens": 0}
            }

viagens={0:{"destino":"Bacabal", 
                "origem":"Caxias", 
                "distância":200.0,
                "motorista":motoristas["11111"], 
                "veiculo":veiculos["BCC009"]},
         1:{"destino":"Bacabel", 
                "origem":"Caxias", 
                "distância":200.0, 
                "motorista":motoristas["11111"], 
                "veiculo":veiculos["BCC009"]
               }}

manutencoes ={0:{"veiculo":veiculos["BCC009"],"data":"02-02-2023", "tipo":"preventiva","custo":1000.0},
              1:{"veiculo":veiculos["BCC009"],"data":"02-02-2023", "tipo":"preventiva","custo":1000.0},
              "total": 2000}

abastecimentos={0:{"veiculo":veiculos["BCC009"],"valor":400.0,"data":"4-2-2023","quantidade":150},
               1:{"veiculo":veiculos["BCC009"],"valor":400.0,"data":"4-2-2023","quantidade":150},
               "total":300}

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

       RG = input('RG: ')
       while RG == '':
              print('RG não pode ser vazio, insira novamente')
              RG = input('RG: ')

       CNH = input('CNH: ')
       while CNH == '':
              print('CNH não pode ser vazio, insira novamente')
              CNH = input('CNH: ')
       
       motorista = {
        "nome": nome,
        "CPF": cpf,
        "RG": RG,
        "CNH": CNH,
        "total_km": 0,
        "qnt_viagens": 0
       }
       motoristas[cpf] = motorista

def pesquisar_motorista():
       cpf = input('Insira o cpf do motorista: ')
       motorista = motoristas.get(cpf)
       if motorista:
              return motorista
       else:
              print('Motorista não encontrado\n')

def editar_motorista(motorista):
       print('Atualizando dados, deixe os campos vazios para manter os valores ja cadastrados')
       nome = input('\nDigite o novo nome: ')
       if nome != '':
              motorista["nome"] = nome
              print('Nome atualizado com sucesso\n')
       RG = input('Insira o novo RG: ')
       if RG != '':
              motorista["RG"] = RG
              print('RG atualizado com sucesso\n')
       CNH = input('Insira a nova CNH: ')
       if CNH != '':
              motorista["CNH"] = CNH
              print('CNH atualizada com sucesso\n')

def deletar_motorista(motorista):
       cpf = motorista["CPF"]
       del motoristas[cpf]

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
       
       veiculo = {
        "marca": marca,
        "modelo": modelo,
        "ano": ano,
        "placa": placa,
        "chassi": chassi,
        "cor": cor,
        "km": km
       }
       veiculos[placa] = veiculo

def pesquisar_veiculo():
       placa = input('Insira a placa do veiculo: ')
       veiculo = veiculos.get(placa)
       if veiculo:
              return veiculo
       else:
              print('Veiculo não encontrado\n')

def editar_veiculo(veiculo):
       print('Atualizando dados, deixe os campos vazios para manter os valores ja cadastrados')
       marca = input('\nDigite a marca: ')
       if marca != '':
              veiculo["marca"] = marca
              print('Marca atualizado com sucesso\n')
       modelo = input('\nInsira o novo modelo: ')
       if modelo != '':
              veiculo["modelo"] = modelo
              print('Modelo atualizado com sucesso\n')
       ano = input('Insira o ano: ')
       if ano != '':
              veiculo["ano"] = ano
              print('Ano atualizado com sucesso\n')
              
       chassi = input('Insira a nova chassi: ')
       if chassi != '':
              veiculo["chassi"] = chassi
              print('Chassi atualizado com sucesso\n')
       
       cor = input('Insira a nova cor: ')
       if cor != '':
              veiculo["cor"] = cor
              print('Cor atualizada com sucesso\n')
       
       km = input('Insira a quilometragem: ')
       if km != '':
              veiculo["km"] = float(km)
              print('Quilometragem atualizada com sucesso\n')

def deletar_veiculo(veiculo):
       placa = veiculo["placa"]
       del veiculos[placa]

def km_veiculo(veiculo):
       print(f'A quilometragem do {veiculo["marca"]} {veiculo["modelo"]} é {veiculo["km"]} quilometros')

def cadastrar_viagem(codigo_viagem):
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

       motorista = pesquisar_motorista()
       veiculo = pesquisar_veiculo()

       motorista["total_km"] += km
       motorista["qnt_viagens"] += 1

       veiculo["km"] += km
       
       viagem = {
        "destino": destino,
        "origem": origem,
        "distancia": km,
        "motorista": motorista,
        "veiculo": veiculo
       }
       print(f"Codigo da viagem: {codigo_viagem}")
       viagens[codigo_viagem] = viagem

def pesquisar_viagem():
       codigo_viagem = input('Insira o codigo da viagem: ')
       viagem = viagens.get(codigo_viagem)
       if viagem:
              return viagem
       else:
              print('Viagem não encontrado\n')

def editar_viagem(viagem):
       print('Atualizando dados, deixe os campos vazios para manter os valores ja cadastrados')

       destino = input('\nDigite o destino: ')
       if destino != '':
              viagem["destino"] = destino
       
       origem = input('Origem: ')
       if origem != '':
              viagem["origem"] = origem
       
       motorista = viagem["motorista"]
       km_antigo = viagem["distancia"]
       veiculo = viagem["veiculo"]

       km = input('Distancia percorrida: ')
       if km != '':
              motorista["km"] += float(km)
              veiculo["km"] -= float(km_antigo)
              veiculo["km"] += float(km)
              viagem["distancia"] = float(km)

       
       print("Editar motorista?")
       # atualizar km
       print("1- Sim")
       print("2- Não")
       op = input()
       if op == 'Sim' or op == "sim":
              motorista["total_km"] -= viagem["distancia"]
              motorista = pesquisar_motorista()
              motorista["total_km"] += viagem["distancia"]
              viagem["motorista"] = motorista
       
       print("Editar Veiculo?")
       print("1- Sim")
       print("2- Não")
       op = input()
       if op == 'Sim' or op == "sim":
              veiculo["km"] -= viagem["distancia"]
              veiculo = pesquisar_veiculo()
              veiculo["km"] += viagem["distancia"]
              viagem["veiculo"] = veiculo

def registrar_abastecimento(codigo_abastecimento):
       print('\nInsira os dados do abastecimento\n')

       veiculo = pesquisar_veiculo()

       valor = float(input('Valor abastecido: '))
       while valor == '':
              print('Valor abastecido não pode ser vazio, insira novamente')
              valor = float(input('Valor abastecido: '))
       abastecimentos["total"] += valor

       data = input('Data do abastecimento: ')
       while data == '':
              print('Data do abastecimento não pode ser vazio, insira novamente')
              data = input('Data do abastecimento: ')

       quantidade = float(input('Quantidade abastecida: '))
       while quantidade == '':
              print('Quantidade abastecida não pode ser vazio, insira novamente')
              quantidade = float(input('Quantidade abastecida: '))
       
       abastecimento = {
        "veiculo": veiculo,
        "valor": valor,
        "data": data,
        "quantidade": quantidade
       }
       print(f"O codigo do abastecimento é {codigo_abastecimento}")
       abastecimentos[codigo_abastecimento] = abastecimento

def registrar_manutencao(codigo_manutencao):
       print('\nInsira os dados da manutencao\n')

       veiculo = pesquisar_veiculo()

       custo = float(input('Custo: ') )
       while custo == '':
              print('Custo  não pode ser vazio, insira novamente')
              custo = float(input('Custo: ') )
       manutencoes["total"] += custo

       data = input('Data da manutenção: ')
       while data == '':
              print('Data da manutenção não pode ser vazia, insira novamente')
              data = input('Data da manutenção: ')

       tipo = input('Tipo da manutencao: ')
       while tipo == '':
              print('Tipo da manutencao não pode ser vazio, insira novamente')
              tipo = input('Tipo da manutencao: ')

       manuntencao = {
        "veiculo": veiculo,
        "data": data,
        "tipo": tipo,
        "custo": custo        
       }
       print(f"O codigo da manutencao é {codigo_manutencao}")
       manutencoes[codigo_manutencao] = manuntencao

def veiculo_maior_km():
       maior = 0
       for veiculo in veiculos.values():
              if maior < veiculo["km"]:
                     maior = veiculo["km"]
                     veiculo_maior = veiculo

       print(f'O veiculo com maior quilometragem é o {veiculo_maior["marca"]} {veiculo_maior["modelo"]} com {veiculo_maior["km"]} quilometros\n')

def motorista_mais_viagens():
       maior = 0
       for motorista in motoristas.values():
              if maior < motorista["qnt_viagens"]:
                     maior = motorista["qnt_viagens"]
                     motorista_maior = motorista
       print(f'O motorista com mais viagens é o {motorista_maior["nome"]} com {motorista_maior["qnt_viagens"]} viagens\n')

def motorista_maior_km():
       maior = 0
       for motorista in motoristas.values():
              if maior < motorista["total_km"]:
                     maior = motorista["total_km"]
                     motorista_maior = motorista
       print(f'O motorista com maior quilometragem é o {motorista_maior["nome"]} com {motorista_maior["total_km"]} quilometros\n')

def relatorio():
       print(f"Quantidade de Motoristas: {len(motoristas)}\n")
       print(f"Quantidade de Veiculos: {len(veiculos)}\n")
       print("Motorista que mais realizou viagens:")
       motorista_mais_viagens()
       print("Motorista que mais quilometros percorreu:")
       motorista_maior_km()
       print("Veiculo com maior quilometragem:\n")
       veiculo_maior_km()
       total = abastecimentos["total"]
       print(f"Total de despesas com abastecimento: {total}\n")
       total = manutencoes["total"]
       print(f"Total de despesas com manutençoes: {total}\n")
       
def main():
    codigo_viagem = 1
    codigo_abastecimento = 1
    codigo_manutencao = 1
    while True:
       op = menu()
       # Gerenciamento de Motoristas
       if op == 1:
              op_2 = submenu_motoristas()
              if op_2 == 'a':
                     cadastro_motorista()
              if op_2 == 'b':
                     if len(motoristas) != 0:
                            print(pesquisar_motorista())
                     else:
                            print("Não há motoristas cadastrados")
              if op_2 == 'c':
                     if len(motoristas) != 0:
                            editar_motorista(pesquisar_motorista())
                     else:
                            print("Não há motoristas cadastrados")
              if op_2 == 'd':
                     if len(motoristas) != 0:
                            deletar_motorista(pesquisar_motorista())
                     else:
                            print("Não há motoristas cadastrados")
       # Gerenciamento de Veiculos
       if op == 2:
              op_2 = submenu_veiculos()
              if op_2 == 'a':
                     cadastro_veiculo()
              if op_2 == 'b':
                     if len(veiculos) != 0:
                            print(pesquisar_veiculo())
                     else:
                           print("Não há veiculos cadastrados") 
              if op_2 == 'c':
                     if len(veiculos) != 0:
                            editar_veiculo(pesquisar_veiculo())
                     else:
                           print("Não há veiculos cadastrados") 
              if op_2 == 'd':
                     if len(veiculos) != 0:
                            deletar_veiculo(pesquisar_veiculo())
                     else:
                           print("Não há veiculos cadastrados") 
              if op_2 == 'e':
                     if len(veiculos) != 0:
                            km_veiculo(pesquisar_veiculo())
                     else:
                           print("Não há veiculos cadastrados") 
       # Gerenciameto de Viagens
       if op == 3:
              if len(veiculos) != 0 or len(motoristas) != 0:
                     op = submenu_viagem()
                     if op == 'a':
                            codigo_viagem += 1
                            cadastrar_viagem(codigo_viagem)
                     if op == 'b':
                            if len(viagens) != 0:
                                   editar_viagem()
                            else:
                                   print("Não há viagens cadastradas")
              else:
                     print("Não há veiculos ou motoristas suficientes")
       # Registrar Abastecimento
       if op == 4:
              if len(veiculos) != 0:
                     codigo_abastecimento += 1
                     registrar_abastecimento(codigo_abastecimento)
              else:
                     print("Não há veiculos cadastrados")
       # Registrar Manutencao
       if op == 5:
              if len(veiculos) != 0:
                     codigo_manutencao += 1
                     registrar_manutencao(codigo_manutencao)
              else:
                     print("Não há veiculos cadastrados")
       # Relatorio
       if op == 6:
              relatorio()
       if op == 0:
             return

main()