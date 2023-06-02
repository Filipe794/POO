from abc import ABC, abstractmethod
from classes import Motoristas, Veiculos, Manutencao, Abastecimento,Viagens

# cada objeto vira um dicionario e cada dicionario é armazenado dentro de outro dicionario
class BaseDAO(ABC):
    @abstractmethod
    def add(self):...
    @abstractmethod
    def pesquisar(self):...
    @abstractmethod
    def edit(self):...
    @abstractmethod
    def delete(self):...

motoristas = {}
veiculos = {}
manutencoes = {}
abastecimentos = {}
viagens = {}

class MotoristasDAO(BaseDAO):
    def add(self,motorista: Motoristas):         
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
    def pesquisar(self,cpf: str):
        # pesquisar no dicionario pelo cpf e retornar o motorista
        pass
    def edit(self, motorista: Motoristas):
        # receber o motorista que foi pesquisado e editar
        pass
    def delete(self, cpf: str):
        # receber um motorista e excluir do dicionario
        pass

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
    def pesquisar(self,veiculo: Veiculos):
        # pesquisar no dicionario por placa e retornar
        pass
    
    def edit(self,veiculo: Veiculos):
        # receber um veiculo e editar
        pass
    
    def delete(self,veiculo: Veiculos):
        # receber um veiculo e excluir do dicionario
        pass

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
    