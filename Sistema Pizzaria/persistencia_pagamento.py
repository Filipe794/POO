import json
from Endereco import *
from Cartao import *
from carrinho import *
from Cartao import *
from Pagamento import *
from abc import ABC, abstractmethod

pagamentos = {}


class baseDAO(ABC):
    @abstractmethod
    def adicionar(self):
        pass

    @abstractmethod
    def pesquisar(self):
        pass

class PagamentoDAO(baseDAO):
    def adicionar(self, pagamento: Pagamento):
        id = pagamento.id
        cliente = pagamento.cliente
        carrinho = pagamento.carrinho
        
        pagamento_dict = {
        "cliente": cliente,
        "carrinho": carrinho,
        "id": id}
        pagamentos[id] = pagamento_dict

        try:
            with open("pagamento.json", 'w') as file:
                json.dump(pagamentos, file, indent=2)
        except FileNotFoundError:
            print("Erro: O arquivo não foi encontrado.")
        finally:
            file.close()
        
    def pesquisar(self, id):

        try:
            with open("pagamentos.json") as file:
                        data = json.load(file)
                        pagamento = data.get(id)
                        if pagamento:
                            return pagamento
                        else:
                            print("não encontrado")

        except FileNotFoundError:
               print("Erro: O arquivo não foi encontrado.")
        finally:
               file.close()
     