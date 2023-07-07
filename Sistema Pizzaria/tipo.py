from sabor import *
from ingrediente import *

class Tipo:
    def __init__(self, sabores: list, precoP:float, precoM:float, precoG:float, nome:str) -> None:
        self.__sabores= sabores
        self.__precoP = precoP
        self.__precoM = precoM
        self.__precoG = precoG
        self.nome = nome

    @property   
    def precoP(self):
        return self.__precoP
    @precoP.setter
    def precoP(self,precoP):
        self.__precoP=precoP

    @property    
    def precoM(self):
        return self.__precoM 
    def precoM(self,precoM):
        self.__precoM=precoM

    @property    
    def precoG(self):
        return self.__precoG
    
    @precoG.setter
    def precoG(self,precoG):
        self.__precoG=precoG

    def imprime_sabor(self):
        for sabor in self.__sabores:
            sabor.imprime_sabor()

    def imprime_valor(self):
        print("P: R$",self.__precoP) 
        print("M: R$",self.__precoM) 
        print("G: R$",self.__precoG)
    
    def to_dict(self):
        list_sabores = []
        for sabor in self.__sabores:
            sabor_dict = sabor.to_dict()
            list_sabores.append(sabor_dict)
        return {
            "nome": self.nome,
            "sabores": list_sabores,
            "precoP": self.precoP,
            "precoG": self.precoG,
            "precoM": self.precoM
        }