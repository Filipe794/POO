from sabor import *
from ingrediente import *
from tipo import *
from persistencia_classes_pizza import SaborDAO,IngredientesDAO,TipoDAO

dao_sabor = SaborDAO()
dao_ingredientes = IngredientesDAO()
dao_tipo = TipoDAO()

# ingredientes
cebola = Ingrediente("Cebola")
dao_ingredientes.adicionar(cebola)

tomate = Ingrediente("Tomate")
dao_ingredientes.adicionar(tomate)

azeitona = Ingrediente("Azeitona")
azeitona.definir_preco(5)
dao_ingredientes.adicionar(azeitona)

presunto = Ingrediente("Presunto")
dao_ingredientes.adicionar(presunto)

champignon = Ingrediente("Champignon")
dao_ingredientes.adicionar(champignon)

tofupiry = Ingrediente("Tofupiry")
dao_ingredientes.adicionar(tofupiry)

molho_tomate = Ingrediente("Molho de tomate")
dao_ingredientes.adicionar(molho_tomate)

catupiry = Ingrediente("Catupiry")
catupiry.definir_preco(3)
dao_ingredientes.adicionar(catupiry)

provolone = Ingrediente("Provolone")
dao_ingredientes.adicionar(provolone)

cheddar = Ingrediente("cheddar")
cheddar.definir_preco(3)
dao_ingredientes.adicionar(cheddar)

parmesão = Ingrediente("Parmesão")
dao_ingredientes.adicionar(parmesão)

frango = Ingrediente("Frango")
dao_ingredientes.adicionar(frango)

requeijão = Ingrediente("Requeijão")
dao_ingredientes.adicionar(requeijão)

banana = Ingrediente("Banana")
dao_ingredientes.adicionar(banana)

leite_condensado = Ingrediente("Leite condensado")
dao_ingredientes.adicionar(leite_condensado)

canela = Ingrediente("Canela")
dao_ingredientes.adicionar(canela)

maçã = Ingrediente("Maçã")
dao_ingredientes.adicionar(maçã)

goiabada = Ingrediente("Goiabada")
dao_ingredientes.adicionar(goiabada)

milho = Ingrediente("Milho")
milho.definir_preco(3)
dao_ingredientes.adicionar(milho)

palmito = Ingrediente("Palmito")
dao_ingredientes.adicionar(palmito)

ervilha = Ingrediente("Ervilha")
dao_ingredientes.adicionar(ervilha)

tomate_seco = Ingrediente("Tomate seco")
dao_ingredientes.adicionar(tomate_seco)

molho_especial = Ingrediente("Molho Especial")
dao_ingredientes.adicionar(molho_especial)

mussarela = Ingrediente("Mussarela")
dao_ingredientes.adicionar(mussarela)

ovo = Ingrediente("Ovo")
dao_ingredientes.adicionar(ovo)

manjericão = Ingrediente("Manjericão")
dao_ingredientes.adicionar(manjericão)

azeitona_preta = Ingrediente("Azeitona Preta")
azeitona_preta.definir_preco(5)
dao_ingredientes.adicionar(azeitona_preta)

parma = Ingrediente("Parma")
dao_ingredientes.adicionar(parma)

tomate_cereja = Ingrediente("Tomate Cereja")
dao_ingredientes.adicionar(tomate_cereja)

peperoni = Ingrediente("Peperoni")
peperoni.definir_preco(8)
dao_ingredientes.adicionar(peperoni)

camarão = Ingrediente("Camarão")
dao_ingredientes.adicionar(camarão)

orégano = Ingrediente("Orégano")
dao_ingredientes.adicionar(orégano)


# sabores
cinco_queijos = [molho_tomate, catupiry, mussarela, provolone, cheddar, parmesão]
sabor_cinco_queijos = Sabor("Cinco Queijos", cinco_queijos, 101, "especial")
dao_sabor.adicionar(sabor_cinco_queijos)

frango_cremoso = [molho_tomate, mussarela, frango, cebola, requeijão, orégano]
sabor_frango_cremoso = Sabor("Frango Cremoso", frango_cremoso, 102,"especial")
dao_sabor.adicionar(sabor_frango_cremoso)

banana_pizza = [mussarela, banana, leite_condensado, canela]
sabor_banana = Sabor("Banana", banana_pizza, 103,"especial")
dao_sabor.adicionar(sabor_banana)

maca = [maçã, leite_condensado, canela]
sabor_maca = Sabor("Maçã", maca, 104,"especial")
dao_sabor.adicionar(sabor_maca)

bella_vegana = [tofupiry, milho, palmito, champignon, ervilha, tomate_seco]
sabor_bella_vegana = Sabor("Bella Vegana", bella_vegana, 105,"especial")
dao_sabor.adicionar(sabor_bella_vegana)

camarão = [molho_tomate, mussarela, camarão, parmesão, manjericão]
sabor_camarão = Sabor("Camarão", camarão, 106,"especial")
dao_sabor.adicionar(sabor_camarão)

sabores_especiais = [
    sabor_cinco_queijos,
    sabor_frango_cremoso,
    sabor_banana,
    sabor_maca,
    sabor_bella_vegana,
    sabor_camarão
]

especial = Tipo(sabores_especiais, 35.00, 45.00, 57.00, "especiais")

marguerita = [molho_especial, mussarela, tomate, manjericão]
sabor_marguerita = Sabor("Marguerita", marguerita, 107, "tradicional")
dao_sabor.adicionar(sabor_marguerita)

da_casa = [molho_especial, mussarela, azeitona_preta, parma, tomate_cereja]
sabor_da_casa = Sabor("Da Casa", da_casa, 108, "tradicional")
dao_sabor.adicionar(sabor_da_casa)

list_peperoni = [molho_tomate, cheddar, peperoni]
sabor_peperoni = Sabor("Peperoni", list_peperoni, 109, "tradicional")
dao_sabor.adicionar(sabor_peperoni)

portuguesa = [molho_especial, mussarela, presunto, ovo, cebola, azeitona]
sabor_portuguesa = Sabor("Portuguesa", portuguesa, 110, "tradicional")
dao_sabor.adicionar(sabor_portuguesa)

dois_queijos = [molho_tomate, mussarela, catupiry, orégano]
sabor_dois_queijos = Sabor("Dois Queijos", dois_queijos, 111, "tradicional")
dao_sabor.adicionar(sabor_dois_queijos)

frango_catupiry = [mussarela, frango, catupiry, orégano]
sabor_frango_catupiry = Sabor("Frango com Catupiry", frango_catupiry, 112, "tradicional")
dao_sabor.adicionar(sabor_frango_catupiry)

sabores_tradicionais = [
    sabor_portuguesa,
    sabor_marguerita,
    sabor_da_casa,
    sabor_peperoni,
    sabor_dois_queijos,
    sabor_frango_catupiry
]

tradicionais = Tipo(sabores_tradicionais, 27.50, 37.50, 49.50,"tradicionais")