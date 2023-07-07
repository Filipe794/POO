from item_carrinho import *
from pizza import *
import json
from copy import deepcopy
import json
from Pagamento import *

class Carrinho:
    def __init__(self):
        self.__cliente = None
        self.__pedidos = {}
        self.__ferramenta = None

    def atualiza_arquivo(self):
        with open("arc_carrinho", 'w') as arquivo:
            json.dump(self.__pedidos, arquivo, indent=2, default=lambda obj: obj.to_dict())

    def add_pedido(self, item_carrinho, pizza):
        id_pedido = item_carrinho.id_ped
        if id_pedido not in self.__pedidos:
            self.__pedidos[id_pedido] = []

        for pedido in self.__pedidos[id_pedido]:
            if pedido["adicionais"] == item_carrinho.get_adicionais() and pedido["pizza"] == pizza.to_dict():
                return

        novo_pedido = {
            "pedido": {
                "quantidade": item_carrinho.get_quant()
            },
            "adicionais": deepcopy(item_carrinho.get_adicionais()),
            "pizza": pizza.to_dict(),
        }
        self.__pedidos[id_pedido].append(novo_pedido)
        self.atualiza_arquivo()

    def pedido_cliente(self, cpf):
        with open("arc_carrinho", 'r') as arquivo:
            pedidos = json.load(arquivo)
        carro = []
        for chave, lis_pedidos in pedidos.items():
            for pedido in lis_pedidos:
                if pedido["pizza"]["cpf"] == cpf:
                    carro.append((chave, pedido))
        return carro

    def total_carrinho(self, cpf):
        total = 0.0
        with open("arc_carrinho", 'r') as arquivo:
            pedidos = json.load(arquivo)
        for chave, lista_pedidos in pedidos.items():
            for pedido in lista_pedidos:
                if pedido["pizza"]["cpf"] == cpf:
                    preco_pizza = pedido["pizza"]["preco"]
                    quant = pedido["pedido"]["quantidade"]
                    preco_adicionais = sum([adicional["preco"] for adicional in pedido["adicionais"]])
                    total += (preco_pizza + preco_adicionais) * quant
        return total

    def calcular_preco_pedido(self, chave):
        with open("arc_carrinho", 'r') as arquivo:
            pedidos = json.load(arquivo)

        if chave in pedidos:
            pedido = pedidos[chave][0]  # Acessa o primeiro item da lista de pedidos
            preco_pizza = pedido["pizza"]["preco"]
            quantidade = pedido["pedido"]["quantidade"]
            preco_adicionais = sum([adicional["preco"] for adicional in pedido["adicionais"]])

            preco_total = (preco_pizza + preco_adicionais) * quantidade
            return preco_total
        else:
            print(f"Chave {chave} não encontrada.")
            return None

    def imprime_ped(self, pedidos):
        if pedidos:
            print("Pedidos do cliente")
            for chave, pedido in pedidos:
                print("ID do pedido:", chave)
                print(json.dumps(pedido, indent=2))
                print("-" * 30)
        else:
            print("O cliente não tem pedidos")

    def deletar_pedido(self, id):
        with open("arc_carrinho", 'r') as arquivo:
            pedidos = json.load(arquivo)

        if id in pedidos:
            del pedidos[id]
            with open("arc_carrinho", 'w') as arquivo:
                json.dump(pedidos, arquivo, indent=2)
            print(f"O pedido de ID: {id} foi removido do carrinho")
        else:
            print(f"Pedido não encontrado, verifique se o ID: {id} é o correto")

    @property
    def ferramenta(self):
        return self.__ferramenta
    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self.__ferramenta = ferramenta
    @property
    def cliente(self):
        return self.__cliente

    @property
    def item_ped(self):
        return self.__item_ped

    @item_ped.setter
    def item_ped(self, item):
        self.__item_ped = item