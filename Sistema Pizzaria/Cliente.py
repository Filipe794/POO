from Endereco import *
from Cartao import *
from Endereco import *
from Carrinho import *

class Cliente:
    def __init__(self,nome,email,cpf,telefone):
        self.__nome = nome
        self.cpf = cpf
        self.__enderecos = []
        # endereço é um objeto
        self.__telefone = telefone
        #telefone é uma lista de objeto
        self.__email = email
        self.__cartoes = []
        self.ferramenta = None

    @property
    def nome(self):
        return self.__nome
        
    @property
    def email(self):
        return self.__email

    def imprime_info(self):
        print(f"Nome: {self.__nome} CPF: {self.cpf} Email: {self.__email} Telefone: {self.__telefone}")

    def imprime_enderecos(self):
        for endereco in self.__enderecos:
            print(endereco.descricao)
    
    def imprime_cartao(self):
        for cartao in self.__cartoes:
            print(cartao.mostra_info())

    @property
    def cartoes(self):
        return self.__cartoes

    @property
    def telefone(self):
        return self.__telefone
    
    def telefone(self,telefone):
        self.__telefone = telefone
    
    @property
    def enderecos(self):
        return self.__enderecos

    def enderecos(self,enderecos: list):
        self.__enderecos = enderecos

    def add_endereco(self,endereco):
        endereco.set_cliente(self)
        self.__enderecos.append(endereco)
    
    def add_cartoes(self,cartao):
        self.__cartoes.append(cartao)
    
    def to_dict(self):
        return {
            "nome": self.__nome,
            "cpf": self.cpf,
            "telefone": self.__telefone,
            "email": self.__email
        }

