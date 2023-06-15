from abc import ABC, abstractmethod
from classes import Motoristas, Veiculos, Manutencao, Abastecimento, Viagens
import json

# cada objeto vira um dicionario e cada dicionario é armazenado dentro de outro dicionario

# manutencao e abastecimento apenas adicionam, pesquisa
# viagem tem adicionar, pesquisar e editar

# modo de arquivo +a

class BaseDAO(ABC):
    @abstractmethod
    def add(): ...
    @abstractmethod
    def pesquisar(): ...
    @abstractmethod
    def edit(): ...
    @abstractmethod
    def delete(): ...

# motoristas = {}
# veiculos = {}
# manutencoes = {}
# abastecimentos = {}
# viagens = {}

motorista = Motoristas("Filipe", "134134", "134134", "134134")

motorista1 = {
        "nome": "caua",
        "CPF": "134134",
        "RG": "134134",
        "CNH": "134134"
       }

motorista2 = {
        "nome": "bet",
        "CPF": "134134",
        "RG": "134134",
        "CNH": "134134"
       }


class MotoristasDAO(BaseDAO):
    def add(self,motorista: Motoristas):
       motorista = {
        "nome": motorista.nome,
        "CPF": motorista.cpf,
        "RG": motorista.rg,
        "CNH": motorista.cnh
       }

       with open("motoristas.json", 'w') as file:
        json.dump(motorista, file, indent=2)
        json.dump(motorista1, file, indent=2)
        json.dump(motorista2, file, indent=2)

    
    def pesquisar(self):
       pass
    def edit(self):
       pass
    def delete(self):
       pass

file_motorista = MotoristasDAO()
file_motorista.add(motorista)

#     def pesquisar(self, cpf: str):
#         # pesquisar no dicionario pelo cpf e retornar o motorista
#         motorista = motoristas.get(cpf)
#         if motorista:
#             return motorista
#         else:
#             print('Motorista não encontrado\n')
#     def edit(self, motorista: Motoristas):
#         # receber o motorista que foi pesquisado e editar
#         print('Atualizando dados, deixe os campos vazios para manter os valores ja cadastrados')
#         nome = input('\nDigite o novo nome: ')
#         if nome != '':
#             motorista["nome"] = nome
#             print('Nome atualizado com sucesso\n')
#         RG = input('Insira o novo RG: ')
#         if RG != '':
#             motorista["RG"] = RG
#             print('RG atualizado com sucesso\n')
#         CNH = input('Insira a nova CNH: ')
#         if CNH != '':
#             motorista["CNH"] = CNH
#             print('CNH atualizada com sucesso\n')
#     def delete(self,motorista: Motoristas):
#         # receber um motorista e excluir do dicionario
#         cpf = motorista["CPF"]
#         del motoristas[cpf]

# class VeiculosDAO(BaseDAO):
#     def add(self,veiculo: Veiculos):
#         marca = veiculo.marca
#         modelo = veiculo.modelo
#         ano = veiculo.ano
#         chassi = veiculo.chassi
#         cor = veiculo.cor
#         placa = veiculo.placa
#         veiculo = {
#             "marca": marca,
#             "modelo": modelo,
#             "ano": ano,
#             "chassi": chassi,
#             "cor": cor,
#             "placa": placa
#         }
#         veiculos[placa] = veiculo
#     def pesquisar(self,placa: str):
#         # pesquisar no dicionario por placa e retornar
#         veiculo = veiculos.get(placa)
#         if veiculo:
#             return veiculo
#         else:
#             print('Veiculo não encontrado\n')
#     def edit(self,veiculo: Veiculos):
#         # receber um veiculo e editar
#         print('Atualizando dados, deixe os campos vazios para manter os valores ja cadastrados')
#         marca = input('\nDigite a marca: ')
#         if marca != '':
#             veiculo["marca"] = marca
#             print('Marca atualizado com sucesso\n')
#         modelo = input('\nInsira o novo modelo: ')
#         if modelo != '':
#             veiculo["modelo"] = modelo
#             print('Modelo atualizado com sucesso\n')
#         ano = input('Insira o ano: ')
#         if ano != '':
#             veiculo["ano"] = ano
#             print('Ano atualizado com sucesso\n')
              
#         chassi = input('Insira a nova chassi: ')
#         if chassi != '':
#             veiculo["chassi"] = chassi
#             print('Chassi atualizado com sucesso\n')
       
#         cor = input('Insira a nova cor: ')
#         if cor != '':
#             veiculo["cor"] = cor
#             print('Cor atualizada com sucesso\n') 
#     def delete(self,veiculo: Veiculos):
#         # receber um veiculo e excluir do dicionario
#         placa = veiculo["placa"]
#         del veiculos[placa]

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
    
# class ViagensDAO(BaseDAO):
#     def add(self, viagem: Viagens):
#         pass
#     def pesquisar(self):
#         return super().pesquisar()
#     def edit(self):
#         return super().edit()
#     def delete(self):
#         return super().delete()
    