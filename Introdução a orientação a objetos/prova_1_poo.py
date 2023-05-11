# criar estrutura para armazenar os objetos
# lista ou dicionario

class Veiculo:
    def __init__(self, marca, modelo, ano, chassi, cor, placa, km):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.chassi = chassi
        self.cor = cor
        self.placa = placa
        self.total_km = km


class Motoristas:
    def __init__(self, nome, cpf, rg, cnh):
        self.nome = nome
        self.cpf = cpf
        self.rg = rg
        self.cnh = cnh
        self.total_km = 0
        self.qnt_viagens = 0


class Viagens:
    def __init__(self, destino, origem, distancia, veiculo, motorista):
        self.destino = destino
        self.origem = origem
        self.distancia = distancia
        veiculo.total_km += distancia
        motorista.total_km += distancia
        motorista.qnt_viagens += 1


codigo_abastecimento = 0


class Abastecimento:
    def __init__(self, veiculo, valor, data, quantidade):
        self.veiculo = veiculo
        self.valor = valor
        self.data = data
        self.quantidade = quantidade
        codigo_abastecimento += 1
        self.codigo_abastecimento = codigo_abastecimento


codigo_manutencao = 0


class Manutencao:
    def __init__(self, veiculo, data, tipo, custo):
        self.veiculo = veiculo
        self.data = data
        self.tipo = tipo,
        self.custo = custo
        codigo_manutencao += 1
        self.codigo_manutencao = codigo_manutencao
