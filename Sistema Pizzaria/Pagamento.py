import qrcode
from Endereco import *
from Cartao import *

from Cartao import *

class Pagamento: 
    def __init__(self):
        self.__cliente = None
        self.__carrinho = None

    def pagar(self):
        self.gera_qr()
        print("Pedido pago!")
        carrinho = self.__carrinho
        # carrinho.pago()
    def forma_pag(self):
        print("\t|1-Dinheiro em espécie   |\n"
          "\t|2-Cartão de crédito         |\n"
          "\t|3-Cartão de débito          |\n"
          "\t|4-Pagamento via pix         |\n"
          "\t|5-sair da forma de pagamento|\n")
        forma = int(input("informe a forma de pagamento que deseja !"))
        return  forma

    def gera_qr(self):
        dados = "Pagamento do pedido de pizza !"
        qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,)
        qr.add_data(dados)
        qr.make(fit=True)
        imagem_qr = qr.make_image(fill_color="black", back_color="white")
        imagem_qr.show()

    def mostra_info(self):
        print(f"Modalidade: {self.__tipo} Número: {self.__numero}")

    @property
    def cliente(self):
        return self.__cliente

    @cliente.setter
    def cliente(self,cliente):
        self.__cliente = cliente

    