from Cliente import *
from persistencia_cliente import *
from PIL import Image
import requests
from io import BytesIO
from Carrinho import *
from Pagamento import *
from objetos import *
import string
import random

DAO_cliente = Cliente_DAO()
DAO_endereco = Endereco_DAO()
DAO_cartao = Cartao_DAO()

lista_adicionais = [catupiry, cheddar, milho, azeitona_preta, peperoni]

def gerar_chave_pix():
    tamanho = 20
    caracteres = string.ascii_letters + string.digits + "!@#$%&*()_+=-"
    chave_pix = ''.join(random.choice(caracteres) for _ in range(tamanho))

    return chave_pix

def menu_carrinho():
    print("|1-Ver meus pedidos                  |\n"
          "|2-Deletar pedidos                   |\n"
          "|3-Valor total do carrinho           |\n"
          "|4-Finalizar pedido                  |\n"
          "|5- Sair do gerenciamento de carrinho|\n")

def gera_id():
    num = list(range(1, 101))
    random.shuffle(num)
    return num.pop()

def exibir_cardapio(drive):
    file_id = drive.split("/")[5]
    imagem = f"https://drive.google.com/uc?id={file_id}"
    response = requests.get(imagem)
    imagem = Image.open(BytesIO(response.content))
    imagem.show()

link_cardapio = "https://drive.google.com/file/d/1lInHx40UxXvAYH-mE9UfmeHavPtY1BHZ/view?usp=sharing"

def receber_enderecos(cliente: Cliente):
    enderecos = []
    descricao = input("Digite sua rua e numero: ")
    endereco = Endereco(descricao, cliente.cpf)
    DAO_endereco.add(endereco)
    enderecos.append(endereco)

    print("Adicionar outro endereço?")
    op = input("1- Sim\n2- Nao\n")
    while op == "1" or op == "sim" or op == "sim":
        descricao = input("Digite sua rua e numero: ")
        endereco = Endereco(descricao, cliente.cpf)
        DAO_endereco.add(endereco)
        enderecos.append(endereco)
        print("Adicionar outro endereço?")
        op = input("1- Sim\n2- Nao\n")

    return enderecos

def criar_cartao(cliente: Cliente):
    print("Selecione a modalidade do cartão?")
    print("1- Crédito\n2- Débito\n")
    op = input()
    if op == "1":
        tipo = "Credito"
    elif op == "2":
        tipo = "Debito"

    numero = input("Insira o numero do cartao:")

    cartao = Cartao(tipo, numero, cliente.cpf)
    DAO_cartao.add(cartao)
    return cartao

def cadastrar_cliente():
    print("Olá! Vamos iniciar seu cadastro: ")
    nome = input("Seu nome: ")
    telefone = input("Seu telefone pra contato: ")
    email = input("Seu email: ")
    cpf = input("Seu cpf: ")

    cliente = Cliente(nome, email, cpf, telefone)
    DAO_cliente.add(cliente)

    enderecos = receber_enderecos(cliente)
    cliente.enderecos(enderecos)

    # adicionar cartao
    print("Cadastrar Cartão?")
    print("1- Sim\n2- Não\n")
    op = input()
    if op == "1" or op == "sim" or op == "Sim":
        cartao = criar_cartao(cliente)
        cliente.add_cartoes(cartao)

    return cliente

def menu_inicio():
    op = int(input("1- Fazer Cadastro\n2- Já tenho conta\nEscolha uma opção: "))
    return op

def menu_cliente_cadastrado():
    print("\n")
    print("1- Realizar Pedido")
    print("2- Ver Carrinho")
    print("3- Sair")
    op = int(input("Escolha uma opção:"))
    return op

def decide_tamanho(cate):

    if cate.nome == "tradicional":
        tradicionais.imprime_valor()
        tamanho = int(input("informe o tamanho desejado:"))
        if tamanho == 1:
            tamanho = "P"
        elif tamanho == 2:
            tamanho = "M"
        elif tamanho == 3:
            tamanho = "G"

    elif cate.nome == "especial":
        especial.imprime_valor()
        tamanho = int(input("informe o tamanho desejado:"))
        if tamanho == 1:
            tamanho = "P"
        elif tamanho == 2:
            tamanho = "M"
        elif tamanho == 3:
            tamanho = "G"
    return tamanho

def decide_preco(tamanho, cate):

    if cate.nome == "tradicionais":
        if tamanho == "P" or tamanho == "p":
            preco = tradicionais.precoP
            return preco
        elif tamanho == "M" or tamanho == "m":
            preco = tradicionais.precoM
            return preco
        elif tamanho == "G" or tamanho == "g":
            preco = tradicionais.precoG
            return preco

    elif cate.nome == "especiais" :
        if tamanho == "P" or tamanho == "p":
            preco = especial.precoP
            return preco
        elif tamanho == "M" or tamanho == "m":
            preco = especial.precoM
            return preco
        elif tamanho == "G" or tamanho == "g":
            preco = especial.precoG
            return preco

def criar_pizza(cliente):

    exibir_cardapio(link_cardapio)
    cod_pizza = input("Insira o codigo da pizza: ")
    sabor = dao_sabor.pesquisar(cod_pizza)

    tamanho = (input("informe o tamanho desejado: (P, M ou G)"))

    if sabor.tipo == "especial":
        tipo = especial
    elif sabor.tipo == "tradicional":
        tipo = tradicionais

    preco_pizza = decide_preco(tamanho, tipo)

    nova_pizza = Pizza(sabor, tipo, tamanho, preco_pizza,cliente.cpf)

    return nova_pizza

def escolhe_adicionais():
    lista_escolha = []
    i = 1
    print(f"{i} - {catupiry.display()}")
    i += 1
    print(f"{i} - {cheddar.display()}")
    i+=1
    print(f"{i} - {milho.display()}")
    i+=1
    print(f"{i} - {azeitona_preta.display()}")
    i+=1
    print(f"{i} - {peperoni.display()}")
    print("0 - Encerrar escolha")

    op = int(input("Insira o codigo do adicional escolhido: "))
    while op != 0:
        op = int(input("Insira o codigo do adicional escolhido: "))
        match op:
            case 1:
                lista_escolha.append(catupiry)
            case 2:
                lista_escolha.append(cheddar)
            case 3:
                lista_escolha.append(milho)
            case 4:
                lista_escolha.append(azeitona_preta)
            case 5:
                lista_escolha.append(peperoni)
    return lista_escolha

op = menu_inicio()
match op:
    case 1:
        cliente = cadastrar_cliente()
    case 2:
        cpf = input("Digite seu cpf: ")
        cliente = DAO_cliente.pesquisar(cpf)

if (cliente):
    loop = True
    while loop:
        op = menu_cliente_cadastrado()
        match op:
            case 1:
                pizza = criar_pizza(cliente)
                qnt = int(input("Quantas dessa pizza deseja pedir? "))
                adicionais = escolhe_adicionais()
                item_carrinho = Item_Carrinho(qnt, cliente.cpf, adicionais, gera_id())
                car = Carrinho()
                car.add_pedido(item_carrinho, pizza)
            case 2:
                aux2 = -1
                while aux2 != 0:
                    menu_carrinho()
                    op2 = int(input("O que deseja fazer?"))
                    match op2:
                        case 1:
                            car = Carrinho()
                            pedidos = car.pedido_cliente(cliente.cpf)
                            car.imprime_ped(pedidos)
                        case 2:
                            car2 = Carrinho()
                            id_remove = input(
                                "informe o id do pedido para remover!")
                            car2.deletar_pedido(id_remove)

                        case 3:
                            car = Carrinho()
                            total = car.total_carrinho(cliente.cpf)
                            print(f"O valor total de seu pedidos sao {total}")

                        case 4:
                            car2 = Carrinho()
                            id_final = input(
                                "informe o id do pedido para finalizar")
                            valor = car2.calcular_preco_pedido(id_final)
                            print(
                                f"O valor total do pedido {id_final} é: {valor}")
                            pagamento = Pagamento()
                            car2.ferramenta = pagamento
                            num = car2.ferramenta.forma_pag()

                            while num != -1:
                                match num:
                                    case 1:
                                        troco = float(input("Quanto de troco o entregador deverá levar?"))
                                        num = -1
                                    case 2:
                                        print("nosso entregador levará a maquina de cartoes ")
                                        num = -1
                                    case 3:
                                        print( "nosso entregador levará a maquina de cartoes ")
                                        num = -1
                                    case 4:
                                        car2.ferramenta.gera_qr()
                                        chave_aleatoria = gerar_chave_pix()
                                        print("Chave PIX aleatória gerada:", chave_aleatoria)
                                        num = -1
                                    case 5:
                                        print("saindo da forma de pagamento !")
                                        num = -1
                        case 5:
                            print("saindo do carrinho")
                            aux2 = 0
            case 3:
                loop = False
