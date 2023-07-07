from ingrediente import *
from pizza import Pizza
from objetos import *
import random

class Item_Carrinho():
    def __init__(self, quant: int, cpf: str, adicionais: dict, id_ped: str):
        self.__cpf = cpf
        self.__id_ped = id_ped
        self.__quant = quant
        self.__adicionais = adicionais
        self.__pizza = None
        self.__pedido = {}
    @property
    def pedido(self):
        return self.__pedido
    @pedido.setter
    def pedido(self, pizza: Pizza):
        self.__pizza = pizza
    def get_quant(self):
        return self.__quant
    def get_cpf(self):
        return self.__cpf
    def get_adicionais(self):
        return self.__adicionais

    def get_pizza(self):
        return self.__pizza

    def add_pizza(self, pizza: Pizza):
        self.__pizza = pizza
        self.__pedido["pizza"] = pizza.to_dict()

    @property
    def quantidade(self):
        return self.__quant
    @quantidade.setter
    def quantidade(self, quant):
        self.__quant = quant
        self.__pedido["quantidade"] = quant
    @property
    def id_ped(self):
        return  self.__id_ped
    @id_ped.setter
    def id_ped(self, id):
        self.__id_ped =id
        self.__id_ped["id"] = id
    @property
    def adicionais(self):
        return self.__adicionais

    @adicionais.setter
    def adicionais(self, adicionais):
        self.__adicionais = adicionais
        self.__pedido["adicionais"] = adicionais

    def add_adicional(self, ingrediente: Ingrediente):
        self.__adicionais[ingrediente.id] = ingrediente
        self.__pedido["adicionais"] = list(self.__adicionais.values())

    def imprime_pedido(self):
        print(f"CPF: {self.__cpf}")
        print(f"Quantidade: {self.__quant}")
        print(f"Adicionais: {self.__adicionais}")

    def imprime_pizza(self):
        print("Pizza:")
        print(f"CPF: {self.__pizza['cpf']}")
        print(f"Sabor: {self.__pizza['sabor']}")
        print(f"Tamanho: {self.__pizza['tamanho']}")


# a classe ingrediente deve ter uma função que retorna o objeto de ingrediente
# item1 = Item_Carrinho(2, "555", [molho_tomate], gera_id())
# item2 = Item_Carrinho(3, "444", [catupiry], gera_id())
# item3 = Item_Carrinho(4, "333", [mussarela], gera_id())
# item4 = Item_Carrinho(5, "555", [molho_tomate], gera_id())
#codigo apenas para teste
'''print('-'*30)
ingrediente1 = Ingrediente("queijo", 2.00, "555")
ingrediente2 = Ingrediente("chedar", 5.00, "444")

"isso pode ser substituido por " \
"pedido.add_adicionais(ingrediente1) como devera ser feita apos a função de retornar objeto ser feito no arquivo " \
"de ingredientes"

pedido = Item_Carrinho(10, "555", [ingrediente2])
pedido2 = Item_Carrinho(15, "444", [ingrediente1])

# criando uma instancia de pizza
pizza = Pizza("4queijos", "tradicional", "media", 35.5, "555")
pizza2 = Pizza("frango", "especial", "fome do marcony", 40.5, "444")

# adicionando o pedido na lista
pedido.add_pizza(pizza2)
pedido.add_pizza(pizza)
'''




