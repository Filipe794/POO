class Veiculos:
    def __init__(self, marca, modelo, ano, chassi, cor, placa):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.chassi = chassi
        self.cor = cor
        self.placa = placa
        self.km = 0

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

class Viagens:
    def __init__(self, destino: str, origem: str, distancia: int, veiculo: Veiculos, motorista: Motoristas, codigo: int):
        self.destino = destino
        self.origem = origem
        self.distancia = distancia
        self.motorista = motorista
        self.veiculo = veiculo
        self.codigo_viagem = codigo

global codigo_abastecimento
codigo_abastecimento = 0

class Abastecimento:
    def __init__(self, veiculo: Veiculos, valor, data, quantidade):
        self.veiculo = veiculo
        self.valor = valor
        self.data = data
        self.quantidade = quantidade
        self.codigo_abastecimento = codigo_abastecimento

global codigo_manutencao
codigo_manutencao = 0

class Manutencao:
    def __init__(self, veiculo: Veiculos, data, tipo, custo):
        self.veiculo = veiculo
        self.data = data
        self.tipo = tipo,
        self.custo = custo
        self.codigo_manutencao = codigo_manutencao

