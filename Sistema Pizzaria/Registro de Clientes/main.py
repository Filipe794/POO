from classes import *
from persistencia import *

dao_cliente = Cliente_DAO()

def cadastrar_cliente():
    print("Olá! Vamos iniciar seu cadastro: ")
    nome = input("Seu nome: ")
    telefone = input("Seu telefone pra contato: ")
    email = input("Seu email: ")

    enderecos = []
    rua = input("Nome da rua: ")
    bairro = input("Bairro: ")
    numero = input("Numero da casa: ")
    ponto_referencia = input("Ponto de referencia: ")
    endereco = {
        "rua": rua,
        "numero": numero,
        "bairro": bairro,
        "ponto_referencia": ponto_referencia
    }
    enderecos.append(endereco)

    print("Adicionar outro endereço?")
    op = input("1- Sim\n2- Nao\n")
    while op == "1" or op == "sim" or op == "sim":
        rua = input("Nome da rua: ")
        bairro = input("Bairro: ")
        numero = input("Numero da casa: ")
        ponto_referencia = input("Ponto de referencia: ")
        endereco = {
            "rua": rua,
            "numero": numero,
            "bairro": bairro,
            "ponto_referencia": ponto_referencia
        }
        enderecos.append(endereco)
        print("Adicionar outro endereço?")
        op = input("1- Sim\n2- Nao\n")
    
    cliente = Cliente(nome,enderecos,telefone,email)
    return cliente

#criar uma classe pedido, vai armazenar sabor da pizza, tamanho, cliente e endereco
# o endereco o cliente seleciona
# imprimir os enderecos q ele tem cadastrado e pedir pra ele selecionar
# definir taxa de entrega
# funcao pra calcular o valor total do pedido (pizzas, ingredientes adicionais e taxa de entrega)
# adicionar o objeto de pedido pra dentro do carrinho
# oq vai ter dentro do carrinho?
# onde armazenar o carrinho?


def menu():
    cliente = cadastrar_cliente()
    dao_cliente.add(cliente)

menu()