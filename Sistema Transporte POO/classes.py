class Veiculos:
    def __init__(self, marca, modelo, ano, chassi, cor, placa, km):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.chassi = chassi
        self.cor = cor
        self.placa = placa

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
