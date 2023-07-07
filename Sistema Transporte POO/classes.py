class Veiculos:
    def __init__(self, marca, modelo, ano, chassi, cor, placa,km):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.chassi = chassi
        self.cor = cor
        self.placa = placa
        self.km = km

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

class Viagens:
    def __init__(self, destino: str, origem: str, distancia: int, veiculo: Veiculos, motorista: Motoristas, codigo: int):
        self.destino = destino
        self.origem = origem
        self.distancia = distancia
        self.motorista = motorista
        self.veiculo = veiculo
        self.codigo_viagem = codigo

class Abastecimento:
    def __init__(self, veiculo, valor, data, quantidade,codigo_abastecimento):
        self.veiculo = veiculo
        self.valor = valor
        self.data = data
        self.quantidade = quantidade
        self.codigo_abastecimento = codigo_abastecimento

class Manutencao:
    def __init__(self, veiculo, data, tipo, custo,codigo_manutencao):
        self.veiculo = veiculo
        self.data = data
        self.tipo = tipo
        self.custo = custo
        self.codigo_manutencao = codigo_manutencao