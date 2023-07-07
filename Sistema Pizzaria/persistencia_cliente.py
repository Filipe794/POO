from abc import ABC, abstractmethod
from Cartao import *
from Endereco import *
from Cliente import *

import json

class Base_DAO_1(ABC):
    @abstractmethod
    def add(): ...
    def pesquisar(): ...

cartoes = {}

class Cartao_DAO(Base_DAO_1):
    def add(self, cartao: Cartao):
        cartao_dict = cartao.to_dict()
        cartoes[cartao_dict["id"]] = cartao_dict
        try:
            with open("cartoes.json", 'w') as file:
                json.dump(cartoes, file, indent=2)
        except FileNotFoundError:
            print("Erro: O arquivo não foi encontrado.")

    def pesquisar(self, id):
        try:
            with open("cartoes.json") as file:
                data = json.load(file)
            cartao = data.get(id)
            if cartao:
                cartao = cartao(cartao["tipo"],cartao["numero"],cartao["id"])
                return cartao
            else:
                print('cartao não encontrado\n')
        except FileNotFoundError:
            print("Erro: O arquivo não foi encontrado.")
    
    def lista_cartoes_cliente(self,id_cliente):
        cartoes = []
        with open("cartoes.json") as file:
            data = json.load(file)
            for cartao_dict in data.values():
                if cartao_dict["id"] == id_cliente:
                    cartao = Cartao(cartao_dict["tipo"], cartao_dict["numero"], cartao_dict["id"])
                    cartoes.append(cartao)
            return cartoes

enderecos = {}

class Endereco_DAO(Base_DAO_1):
    def add(self, endereco: Endereco):
        endereco_dict = endereco.to_dict()
        enderecos[endereco_dict["id"]] = endereco_dict
        try:
            with open("enderecos.json", 'w') as file:
                json.dump(enderecos, file, indent=2)
        except FileNotFoundError:
            print("Erro: O arquivo não foi encontrado.")

    def pesquisar(self, id):
        try:
            with open("enderecos.json") as file:
                data = json.load(file)
            endereco = data.get(id)
            if endereco:
                endereco = Endereco(endereco["descricao"],endereco["id"])
                return endereco
            else:
                print('endereco não encontrado\n')
        except FileNotFoundError:
            print("Erro: O arquivo não foi encontrado.")
    
    def lista_enderecos_cliente(self,id_cliente):
        enderecos = []
        with open("enderecos.json") as file:
            data = json.load(file)
            for endereco_dict in data.values():
                if endereco_dict["id"] == id_cliente:
                    endereco = Endereco(endereco_dict["descricao"],endereco_dict["id"])
                    enderecos.append(endereco)
            return enderecos


clientes = {}
DAO_endereco = Endereco_DAO()
DAO_cartao = Cartao_DAO()

class Cliente_DAO(Base_DAO_1):
    def add(self, cliente: Cliente):
        cliente_dict = cliente.to_dict()
        clientes[cliente_dict["cpf"]] = cliente_dict
        try:
            with open("clientes.json", 'w') as file:
                json.dump(clientes, file, indent=2)
        except FileNotFoundError:
            print("Erro: O arquivo não foi encontrado.")

    def pesquisar(self, cpf):
        try:
            with open("clientes.json") as file:
                data = json.load(file)
            cliente = data.get(cpf)
            if cliente:
                cliente = Cliente(cliente["nome"],cliente["email"],cliente["cpf"],cliente["telefone"])
                cartoes = DAO_cartao.lista_cartoes_cliente(cliente.cpf)
                for cartao in cartoes:
                    cliente.add_cartoes(cartao)
                enderecos = DAO_endereco.lista_enderecos_cliente(cliente.cpf)
                for endereco in enderecos:
                    cliente.add_endereco(endereco)
                return cliente
            else:
                print('Cliente não encontrado\n')
        except FileNotFoundError:
            print("Erro: O arquivo não foi encontrado.")