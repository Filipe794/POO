from abc import ABC, abstractmethod
from Cartao import *
import json

class Base_DAO_1(ABC):
    @abstractmethod
    def add(): ...
    def pesquisar(): ...

cartoes = {}

class Cartao_DAO(Base_DAO_1):
    def add(self, cartao: Cartao):
        cartao_dict = cartao.to_dict()
        cartoes[cartao.id] = cartao_dict
        try:
            with open("cartoes.json", 'a+') as file:
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
        finally:
            file.close()
    
    def lista_cartoes_cliente(self,id_cliente):
        cartoes = []
        with open("cartoes.json") as file:
            data = json.load(file)
            for cartao_dict in data.values():
                if cartao_dict["id"] == id_cliente:
                    cartao = Cartao(cartao_dict["tipo"], cartao_dict["numero"], cartao_dict["id"])
                    cartoes.append(cartao)
            return cartoes
