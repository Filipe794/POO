from abc import ABC, abstractmethod
from classes import *
import json

class Base_DAO_1(ABC):
    @abstractmethod
    def add(): ...
    @abstractmethod
    def pesquisar(): ...
    @abstractmethod
    def edit(): ...

clientes = {}

class Cliente_DAO(Base_DAO_1):
    def add(self, cliente: Cliente):
        cliente_dict = {
            "nome": cliente.nome,
            "telefone": cliente.telefone,
            "email": cliente.email,
            "endereco": cliente.endereco
        }
        clientes[cliente.nome] = cliente_dict

        try:
            with open("clientes.json", 'w') as file:
                json.dump(clientes, file, indent=2)
        except FileNotFoundError:
            print("Erro: O arquivo não foi encontrado.")
        finally:
            file.close()
    def pesquisar():
        pass
    def edit():
        pass
