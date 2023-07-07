from abc import ABC, abstractmethod
from Endereco import *
import json

class Base_DAO_1(ABC):
    @abstractmethod
    def add(): ...
    def pesquisar(): ...


enderecos = {}

class Endereco_DAO(Base_DAO_1):
    def add(self, endereco: Endereco):
        endereco_dict = endereco.to_dict()
        enderecos[endereco.id] = endereco_dict
        try:
            with open("enderecos.json", 'a+') as file:
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
        finally:
            file.close()
    
    def lista_enderecos_cliente(self,id_cliente):
        enderecos = []
        with open("enderecos.json") as file:
            data = json.load(file)
            for endereco_dict in data.values():
                if endereco_dict["id"] == id_cliente:
                    endereco = Endereco(endereco_dict["descricao"],endereco_dict["id"])
                    enderecos.append(endereco)
            return enderecos
