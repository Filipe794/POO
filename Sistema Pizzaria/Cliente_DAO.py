from abc import ABC, abstractmethod
from Cliente import *
import json
import Endereco_DAO
import Cartao_DAO

DAO_endereco = Endereco_DAO()
DAO_cartao = Cartao_DAO()

class Base_DAO_1(ABC):
    @abstractmethod
    def add(): ...
    def pesquisar(): ...


clientes = {}

class Cliente_DAO(Base_DAO_1):
    def add(self, cliente: Cliente):
        cliente_dict = cliente.to_dict()
        clientes[cliente.cpf] = cliente_dict
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
        finally:
            file.close()
