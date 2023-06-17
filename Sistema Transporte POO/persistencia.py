from abc import ABC, abstractmethod
from classes import Motoristas, Veiculos, Manutencao, Abastecimento, Viagens
import json

class Base_DAO_1(ABC):
    @abstractmethod
    def add(): ...
    @abstractmethod
    def pesquisar(): ...
    @abstractmethod
    def edit(): ...
    @abstractmethod
    def delete(): ...


class Base_DAO_2(ABC):
    @abstractmethod
    def add(): ...
    @abstractmethod
    def pesquisar(): ...
    @abstractmethod
    def edit(): ...


class Base_DAO_3(ABC):
    @abstractmethod
    def add(): ...


motoristas = {}
veiculos = {}
manutencoes = {}
abastecimentos = {}
viagens = {}

codigo_viagem = 0
codigo_abastecimento = 0
codigo_manutencao = 0


class MotoristasDAO(Base_DAO_1):
    def add(self, motorista: Motoristas):
        cpf = motorista.cpf
        motorista = {
            "nome": motorista.nome,
            "cpf": cpf,
            "rg": motorista.rg,
            "cnh": motorista.cnh
        }
        motoristas[cpf] = motorista

        with open("motoristas.json", 'w') as file:
            json.dump(motoristas, file, indent=2)

    def pesquisar(self, cpf):
        with open("motoristas.json") as file:
            data = json.load(file)
        motorista = data.get(cpf)
        if motorista:
            return motorista
        else:
            print('Motorista não encontrado\n')

    def edit(self, motorista: dict):
        cpf = motorista["cpf"]

        print('Atualizando dados, deixe os campos vazios para manter os valores ja cadastrados')
        nome = input('\nDigite o novo nome: ')
        if nome != '':
            motorista["nome"] = nome
            print('Nome atualizado com sucesso\n')

        RG = input('Insira o novo RG: ')
        if RG != '':
            motorista["rg"] = RG
            print('RG atualizado com sucesso\n')

        CNH = input('Insira a nova CNH: ')
        if CNH != '':
            motorista["cnh"] = CNH
            print('CNH atualizada com sucesso\n')

        motoristas[cpf] = motorista
        with open("motoristas.json", 'w') as file:
            json.dump(motoristas, file, indent=2)

    def delete(self, motorista: dict):
        cpf = motorista["cpf"]
        del motoristas[cpf]
        with open("motoristas.json", 'w') as file:
            json.dump(motoristas, file, indent=2)


dao_motorista = MotoristasDAO()


class VeiculosDAO(Base_DAO_1):
    def add(self, veiculo: Veiculos):
        placa = veiculo.placa
        veiculo = {
            "marca": veiculo.marca,
            "modelo": veiculo.modelo,
            "ano": veiculo.ano,
            "chassi": veiculo.chassi,
            "cor": veiculo.cor,
            "placa": placa
        }
        veiculos[placa] = veiculo
        with open("veiculos.json", 'w') as file:
            json.dump(veiculos, file, indent=2)

    def pesquisar(self, placa: str):
        with open("veiculos.json") as file:
            data = json.load(file)
        veiculo = data.get(placa)
        if veiculo:
            return veiculo
        else:
            print('Veiculo não encontrado\n')

    def edit(self, veiculo: dict):
        placa = veiculo["placa"]

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

        veiculos[placa] = veiculo
        with open("veiculos.json", "w") as file:
            json.dump(veiculos, file, indent=2)

    def delete(self, veiculo: Veiculos):
        placa = veiculo["placa"]
        del veiculos[placa]
        with open("veiculos.json", "w") as file:
            json.dump(veiculos, file, indent=2)


dao_veiculo = VeiculosDAO()


class ViagensDAO(Base_DAO_2):
    def add(self, viagem: Viagens):
        viagem = {
            "destino": viagem.destino,
            "origem": viagem.origem,
            "distancia": viagem.km,
            "motorista": dao_motorista.pesquisar(viagem.motorista.cpf),
            "veiculo": dao_veiculo.pesquisar(viagem.veiculo.placa)
        }
        viagens[codigo_viagem] = viagem
        with open("viagens.json", 'w') as file:
            json.dump(viagens, file, indent=2)

    def pesquisar(self, codigo_viagem):
        with open("viagens.json") as file:
            data = json.load(file)
        viagem = data.get(codigo_viagem)
        if viagem:
            return viagem
        else:
            print('Viagem não encontrada\n')

    def edit(self, destino, origem, distancia, motorista_novo: Motoristas, veiculo_novo: Veiculos):
        if destino != '':
            self.destino = destino
        if origem != '':
            self.origem = origem
        if distancia != '':
            self.distancia = distancia
        if origem != '':
            self.origem = origem
        if origem != '':
            self.origem = origem


# class ManuntencaoDAO(BaseDAO):
#     def add(self,manutencao: Manutencao):
#         veiculo = manutencao.veiculo
#         data = manutencao.data
#         tipo = manutencao.tipo
#         custo = manutencao.custo
#         codigo_manutencao = manutencao.codigo_manutencao
#         manutencao = {
#         "veiculo": veiculo,
#         "data": data,
#         "tipo": tipo,
#         "custo": custo
#        }
#         print(f"O codigo da manutencao é {codigo_manutencao}")
#         manutencoes[codigo_manutencao] = manutencao
#     def pesquisar(self, codigo_manutencao: int):
#         # retornar uma manutencao
#         manutencao = manutencoes.get(codigo_manutencao)
#         if manutencao:
#             return manutencao
#         else:
#             print('manutencao não encontrada\n')
#     def edit(self):
#         return super().edit()
#     def delete(self):
#         return super().delete()

# class AbastecimentoDAO(BaseDAO):
#     def add(self, abastecimento: Abastecimento):
#         pass
#     def pesquisar(self):
#         return super().pesquisar()
#     def edit(self):
#         return super().edit()
#     def delete(self):
#         return super().delete()
