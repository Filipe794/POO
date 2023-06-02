# criar estrutura para armazenar os objetos
# lista ou dicionario

class Veiculos:
    def __init__(self, marca, modelo, ano, chassi, cor, placa, km):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.chassi = chassi
        self.cor = cor
        self.placa = placa
        self.total_km = km
    def editar_veiculo(self,marca,modelo,ano,chassi,cor,km):
        if marca != '':
            self.marca = marca
            print('Marca atualizado com sucesso\n')
        if modelo != '':
            self.modelo = modelo
            print('Modelo atualizado com sucesso\n')
        if ano != '':
            self.ano = ano
            print('Ano atualizado com sucesso\n')
        if chassi != '':
            self.chassi = chassi
            print('Chassi atualizado com sucesso\n')
        if cor != '':
            self.cor = cor
            print('Cor atualizada com sucesso\n')
        if km != '':
            self.km = float(km)
            print('Quilometragem atualizada com sucesso\n')
    def km_veiculo(self):
        print(f'A quilometragem do {self.marca} {self.modelo} é {self.km} quilometros')
    def atualizar_km(self,km_novo,km_antigo = 0):
        self.total_km -= km_antigo
        self.total += km_novo

class Veiculos_pequenos(Veiculos):
    def __init__(self,marca, modelo, ano, chassi, cor, placa, km):
        super().__init__(marca,modelo,ano,chassi,cor,placa,km)

class Veiculos_grandes(Veiculos):
    def __init__(self,marca, modelo, ano, chassi, cor, placa, km):
        super().__init__(marca,modelo,ano,chassi,cor,placa,km)

class Veiculos_vip(Veiculos):
    def __init__(self,marca, modelo, ano, chassi, cor, placa, km, blindagem: bool):
        super().__init__(marca,modelo,ano,chassi,cor,placa,km)
        self.blindagem = blindagem

class Motoristas:
    def __init__(self, nome, cpf, rg, cnh):
        self.nome = nome
        self.cpf = cpf
        self.rg = rg
        self.cnh = cnh
        self.total_km = 0
        self.qnt_viagens = 0

    def editar_motorista(self,nome,rg,cnh):
        if nome != '':
            self.nome = nome
            print('Nome atualizado com sucesso\n')
        if rg != '':
            self.rg = rg
            print('RG atualizado com sucesso\n')
        if cnh != '':
            self.cnh = cnh
            print('CNH atualizada com sucesso\n')

    def atualizar_km(self,km_novo,km_antigo = 0):
        self.total_km -= km_antigo
        self.total += km_novo

class Viagens:
    def __init__(self, destino: str, origem: str, distancia: int, veiculo: Veiculos, motorista: Motoristas):
        self.destino = destino
        self.origem = origem
        self.distancia = distancia
        self.motorista = motorista
        self.veiculo = veiculo
        veiculo.atualizar_km(distancia)
        motorista.atualizar_km(distancia)
        motorista.qnt_viagens += 1

    def editar_viagem(self,destino,origem,km,motorista_novo: Motoristas, veiculo_novo: Veiculos):
       if destino != '':
            self.destino = destino
       if origem != '':
            self.origem = origem

       if km != '':
            self.motorista.total_km -= float(self.distancia)
            self.veiculo.total_km -= float(self.distancia)

            self.motorista.total_km += float(km)
            self.veiculo.total_km += float(km)

            self.distancia = float(km)

       
       print("Editar motorista?")
       # atualizar km
       print("Sim")
       print("Não")
       op = input()
       if op == 'Sim' or op == "sim":
        self.motorista.total_km -= self.distancia
        self.motorista.qnt_viagens -= 1
        motorista_novo.total_km += self.distancia
        motorista_novo.qnt_viagens += 1
        self.motorista = motorista_novo
       
       print("Editar Veiculo?")
       print("Sim")
       print("Não")
       op = input()
       if op == 'Sim' or op == "sim":
        self.veiculo.atualizar_km(0,self.distancia)
        veiculo_novo.atualizar_km(self.distancia)
        veiculo_novo.atualizar_km(self.distancia)
        self.veiculo = veiculo_novo

codigo_abastecimento = 0

class Abastecimento:
    def __init__(self, veiculo: Veiculos, valor, data, quantidade):
        self.veiculo = veiculo
        self.valor = valor
        self.data = data
        self.quantidade = quantidade
        codigo_abastecimento += 1
        self.codigo_abastecimento = codigo_abastecimento

codigo_manutencao = 0

class Manutencao:
    def __init__(self, veiculo: Veiculos, data, tipo, custo):
        self.veiculo = veiculo
        self.data = data
        self.tipo = tipo,
        self.custo = custo
        codigo_manutencao += 1
        self.codigo_manutencao = codigo_manutencao
