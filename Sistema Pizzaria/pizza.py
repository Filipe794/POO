from sabor import *
from ingrediente import *
from sabor import *
from tipo import *


class Pizza:
    def __init__(self, sabor: Sabor, tipo: Tipo, tamanho: str, preco: float, cpf: int):
        self.__sabor = sabor
        self.__tipo = tipo
        self.__tamanho = tamanho
        self.__preco = preco
        self.cpf = cpf

    @property
    def sabor(self):
        return self.__sabor

    @property
    def tipo(self):
        return self.__tipo

    @property
    def tamanho(self):
        return self.__tamanho

    @property
    def preco(self):
        return self.__preco

    def to_dict(self):
        pizza_dict = {
            'sabor': self.__sabor.nome,
            'tipo': self.__tipo.nome,
            'tamanho': self.__tamanho,
            'preco': self.__preco,
            'cpf': self.cpf
        }
        return pizza_dict