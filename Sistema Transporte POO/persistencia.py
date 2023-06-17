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

        try:
            with open("motoristas.json", 'w') as file:
                json.dump(motoristas, file, indent=2)
        except FileNotFoundError:
            print("Erro: O arquivo não foi encontrado.")
        finally:
            file.close()

    def pesquisar(self, cpf):
        try:
            with open("motoristas.json") as file:
                data = json.load(file)
            motorista = data.get(cpf)
            if motorista:
                return motorista
            else:
                print('Motorista não encontrado\n')
        except FileNotFoundError:
            print("Erro: O arquivo não foi encontrado.")
        finally:
            file.close()

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
        try:
            with open("motoristas.json", 'w') as file:
                json.dump(motoristas, file, indent=2)
        except FileNotFoundError:
            print("Erro: O arquivo não foi encontrado.")
        finally:
            file.close()

    def delete(self, motorista: dict):
        cpf = motorista["cpf"]
        del motoristas[cpf]
        try:
            with open("motoristas.json", 'w') as file:
                json.dump(motoristas, file, indent=2)
        except FileNotFoundError:
            print("Erro: O arquivo não foi encontrado.")
        finally:
            file.close()
            
    def print(self):
        try:
            with open("motoristas.json") as file:
                data = json.load(file)
            for chave, valor in data.items():
                print(chave, ":", valor)
        except FileNotFoundError:
            print("Erro: O arquivo não foi encontrado.")
        finally:
            file.close()

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
        try:
            with open("veiculos.json", 'w') as file:
                json.dump(veiculos, file, indent=2)
        except FileNotFoundError:
            print("Erro: O arquivo não foi encontrado.")
        finally:
            file.close()

    def pesquisar(self, placa: str):
        try:
            with open("veiculos.json") as file:
                data = json.load(file)
            veiculo = data.get(placa)
            if veiculo:
                return veiculo
            else:
                print('Veiculo não encontrado\n')
        except FileNotFoundError:
            print("Erro: O arquivo não foi encontrado.")
        finally:
            file.close()

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
        try:
            with open("veiculos.json", "w") as file:
                json.dump(veiculos, file, indent=2)
        except FileNotFoundError:
            print("Erro: O arquivo não foi encontrado.")
        finally:
            file.close()

    def delete(self, veiculo: Veiculos):
        placa = veiculo["placa"]
        del veiculos[placa]
        try:
            with open("veiculos.json", "w") as file:
                json.dump(veiculos, file, indent=2)
        except FileNotFoundError:
            print("Erro: O arquivo não foi encontrado.")
        finally:
            file.close()

    def print(self):
        try:
            with open("veiculos.json") as file:
                data = json.load(file)
            for chave, valor in data.items():
                print(chave, ":", valor)
        except FileNotFoundError:
            print("Erro: O arquivo não foi encontrado.")
        finally:
            file.close()

dao_veiculo = VeiculosDAO()

class ViagensDAO(Base_DAO_2):
    def add(self, viagem: Viagens):
        codigo = viagem.codigo_viagem
        viagem = {
            "destino": viagem.destino,
            "origem": viagem.origem,
            "distancia": viagem.distancia,
            "motorista": viagem.motorista,
            "veiculo": viagem.veiculo,
            "codigo_viagem": codigo
        }

        viagens[codigo] = viagem
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

    def edit(self,viagem: dict):
        print('Atualizando dados, deixe os campos vazios para manter os valores ja cadastrados')
        destino = input('\nDigite o destino: ')
        origem = input('Origem: ')
        distancia = input('Distancia percorrida: ')

        cod = viagem["codigo_viagem"]

        if destino != '':
            self.destino = destino
        if origem != '':
            self.origem = origem
        if distancia != '':
            self.distancia = distancia
        
        print("Atualizar Motorista?")
        print("1- Sim")
        print("2- Não")
        op = input()
        if op == 'Sim' or op == "sim" or op == 1:
            cpf = input("insira o cpf do motorista")
            motorista = dao_motorista.pesquisar(cpf)
            viagem["motorista"] = motorista
       
        print("Editar Veiculo?")
        print("1- Sim")
        print("2- Não")
        op = input()
        if op == 'Sim' or op == "sim" or op == 1:
            placa = input("insira a placa do veiculo")
            veiculo = dao_veiculo.pesquisar(placa)
            viagem["veiculo"] = veiculo
         
        viagens[cod] = viagem
        with open("viagens.json", "w") as file:
            json.dump(viagens, file, indent=2)
    
    def print(self):
        with open("viagens.json") as file:
            data = json.load(file)
        for chave, valor in data.items():
            print(chave, ":", valor)

dao_viagens = ViagensDAO()

class ManuntencaoDAO(Base_DAO_3):
    def add(self,manutencao: Manutencao):
        codigo_manutencao = manutencao.codigo_manutencao
        manutencao = {
        "veiculo": manutencao.veiculo,
        "data": manutencao.data,
        "tipo": manutencao.tipo,
        "custo": manutencao.custo
       }
        print(f"O codigo da manutencao é {codigo_manutencao}")
        manutencoes[codigo_manutencao] = manutencao

        try:
            with open("manutencoes.json", 'w') as file:
                json.dump(manutencoes, file, indent=2)
        except FileNotFoundError:
            print("Erro: O arquivo não foi encontrado.")
        finally:
            file.close()

    def print(self):
        try:
            with open("manutencoes.json") as file:
                data = json.load(file)
            for chave, valor in data.items():
                print(chave, ":", valor)
        except FileNotFoundError:
            print("Erro: O arquivo não foi encontrado.")
        finally:
            file.close()

dao_manutencao = ManuntencaoDAO()

class AbastecimentoDAO(Base_DAO_3):
    def add(self, abastecimento: Abastecimento):
        codigo = abastecimento.codigo_abastecimento
        abastecimento = {
        "veiculo": abastecimento.veiculo,
        "valor": abastecimento.valor,
        "data": abastecimento.data,
        "quantidade": abastecimento.quantidade
       }
        
        print(f"O codigo do abastecimento é {codigo}")
        abastecimentos[codigo] = abastecimento
        try:
            with open("abastecimentos.json", 'w') as file:
                json.dump(abastecimentos, file, indent=2)
        except FileNotFoundError:
            print("Erro: O arquivo não foi encontrado.")
        finally:
            file.close()

    def print(self):
        try:
            with open("abastecimentos.json") as file:
                data = json.load(file)
            for chave, valor in data.items():
                print(chave, ":", valor)
        except FileNotFoundError:
            print("Erro: O arquivo não foi encontrado.")
        finally:
            file.close()

dao_abastecimento = AbastecimentoDAO()