from abc import ABC, abstractmethod
from classes import Motoristas, Veiculos, Manutencao, Abastecimento, Viagens

# cada objeto vira um dicionario e cada dicionario é armazenado dentro de outro dicionario


class BaseDAO(ABC):
    @abstractmethod
    def add(self): ...
    @abstractmethod
    def pesquisar(self): ...
    @abstractmethod
    def edit(self): ...
    @abstractmethod
    def delete(self): ...


motoristas = {}
veiculos = {}
manutencoes = {}
abastecimentos = {}
viagens = {}

class MotoristasDAO(BaseDAO):
    def add(self, motorista: Motoristas):
       nome = motorista.nome
       cpf = motorista.cpf
       rg = motorista.rg
       cnh = motorista.cnh
       motorista = {
        "nome": nome,
        "CPF": cpf,
        "RG": rg,
        "CNH": cnh
       }
       motoristas[cpf] = motorista
    def pesquisar(self, cpf: str):
        # pesquisar no dicionario pelo cpf e retornar o motorista
        motorista = motoristas.get(cpf)
        if motorista:
            return motorista
        else:
            print('Motorista não encontrado\n')
    def edit(self, motorista: Motoristas):
        # receber o motorista que foi pesquisado e editar
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
    def delete(self,motorista: Motoristas):
        # receber um motorista e excluir do dicionario
        cpf = motorista["CPF"]
        del motoristas[cpf]

class VeiculosDAO(BaseDAO):
    def add(self,veiculo: Veiculos):
        marca = veiculo.marca
        modelo = veiculo.modelo
        ano = veiculo.ano
        chassi = veiculo.chassi
        cor = veiculo.cor
        placa = veiculo.placa
        veiculo = {
            "marca": marca,
            "modelo": modelo,
            "ano": ano,
            "chassi": chassi,
            "cor": cor,
            "placa": placa
        }
        veiculos[placa] = veiculo
    def pesquisar(self,placa: str):
        # pesquisar no dicionario por placa e retornar
        veiculo = veiculos.get(placa)
        if veiculo:
            return veiculo
        else:
            print('Veiculo não encontrado\n')
    def edit(self,veiculo: Veiculos):
        # receber um veiculo e editar
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
    def delete(self,veiculo: Veiculos):
        # receber um veiculo e excluir do dicionario
        placa = veiculo["placa"]
        del veiculos[placa]

class ManuntencaoDAO(BaseDAO):
    def add(self,manutencao: Manutencao):
        pass
    def pesquisar(self):
        # retornar uma manutencao
        pass
    def edit(self):
        return super().edit()
    def delete(self):
        return super().delete()
    
class AbastecimentoDAO(BaseDAO):
    def add(self, abastecimento: Abastecimento):
        pass
    def pesquisar(self):
        return super().pesquisar()
    def edit(self):
        return super().edit()
    def delete(self):
        return super().delete()
    
class ViagensDAO(BaseDAO):
    def add(self, viagem: Viagens):
        pass
    def pesquisar(self):
        return super().pesquisar()
    def edit(self):
        return super().edit()
    def delete(self):
        return super().delete()
    