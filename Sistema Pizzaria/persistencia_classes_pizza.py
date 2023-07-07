import json
from pizza import *
from sabor import *
from tipo import *
from ingrediente import *
from abc import ABC, abstractmethod

sabores = {}
ingredienteS = {}
tipos = {}

class baseDAO(ABC):
    @abstractmethod
    def adicionar(self):
        pass

    @abstractmethod
    def pesquisar(self):
        pass

class SaborDAO(baseDAO):
    def adicionar(self, sabor: Sabor):
        sabor_dict = sabor.to_dict()
        sabores[sabor_dict["id"]] = sabor_dict
        try:
            with open("sabor.json", 'w') as file:
                json.dump(sabores, file, indent=2)
        except FileNotFoundError:
            print("Erro: O arquivo não foi encontrado.")

    def pesquisar(self, sabor_id):
        try:
            with open("sabor.json", "r") as file:
                data = json.load(file)
                sabor_dict = data.get(sabor_id)
            if sabor_dict:
                list_ingredientes = []
                for ingrediente_dict in sabor_dict["ingredientes"]:
                    ingrediente = Ingrediente(ingrediente_dict["nome"])
                    list_ingredientes.append(ingrediente)
                sabor = Sabor(sabor_dict["nome"],list_ingredientes,sabor_dict["id"], sabor_dict["tipo"])
                return sabor
            else:
                print("não encontrado")
        except FileNotFoundError:
               print("Erro: O arquivo não foi encontrado.")

class IngredientesDAO(baseDAO):
    def adicionar(self, ingrediente: Ingrediente):
        ingrediente = ingrediente.to_dict()
        ingredienteS[ingrediente["nome"]] = ingrediente
        try:
            with open("ingredientes.json", 'w') as file:
                json.dump(ingredienteS, file, indent=2)
        except FileNotFoundError:
            print("Erro: O arquivo não foi encontrado.")

    def pesquisar(self, id):
        try:
            with open("ingredientes.json", "r") as file:
                   data = json.load(file)
                   ingrediente = data.get(id)
                   if ingrediente:
                        return ingrediente
                   else:
                        print("não encontrado")
        except FileNotFoundError:
               print("Erro: O arquivo não foi encontrado.")

class TipoDAO(baseDAO):
   def adicionar(self, tipo: Tipo):
        tipo_dict = tipo.to_dict()
        tipos[tipo_dict["nome"]] = tipo_dict

        try:
            with open("tipo.json", 'w') as file:
                json.dump(tipos, file, indent=2)
        except FileNotFoundError:
            print("Erro: O arquivo não foi encontrado.")

   def pesquisar(self, id):
       try:
            with open("tipo.json") as file:
                data = json.load(file)
                tipo = data.get(id)
                if tipo:
                    return tipo
                else:
                    print("não encontrado")
       except FileNotFoundError:
            print("Erro: O arquivo não foi encontrado.")
