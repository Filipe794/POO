import json

# String em formato JSON
data_JSON =  """
{
	"size": "Medium",
	"price": 15.67,
	"toppings": ["Mushrooms", "Extra Cheese", "Pepperoni", "Basil"],
	"client": {
		"name": "Jane Doe",
		"phone": "455-344-234",
		"email": "janedoe@email.com"
	}
}
"""

# Converter a string em JSON para um dicionário
data_dict = json.loads(data_JSON)

# Dicionário em Python
client = {
    "name": "Nora",
    "age": 56,
    "id": "45355",
    "eye_color": "green",
    "wears_glasses": False
}

# Obter uma string formatada em JSON
client_JSON = json.dumps(client)


# imprimir com identação
client_JSON = json.dumps(client, indent=4)

# ordernar as chaves
client_JSON = json.dumps(client, sort_keys=True)

# Abrir o arquivo json
# with open("orders.json") as file:
#     # Carregar seu conteúdo e torná-lo um novo dicionário
#     data = json.load(file)
data = "filipe"
# Abrir (ou criar) um arquivo orders_new.json 
# e armazenar a nova versão dos dados.
with open("orders_new.json", 'w') as file:
    json.dump(data, file, indent = 4)