from ingrediente import* 

class Sabor:
    def __init__(self,nome:str, ingredientes: list,sabor_id:int, tipo: str): 
       self.__nome=nome
       self.__ingredientes=ingredientes
       self.id=sabor_id
       self.tipo = tipo
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self,nome):
        self.__nome=nome

    @property
    def ingredientes(self):
          return self.__ingredientes 

    @ingredientes.setter
    def ingredientes(self,ingredientes: list):
          self.__ingredientes=ingredientes
    
    def imprime_sabor(self):
        print(self.__nome + ": ")
        for ingrediente in self.__ingredientes:
            print(ingrediente.nome())

    def to_dict(self):
        # transformar em dicionario usando o to dict dos ingredientes
        list_dict_ingredientes = []
        for ingrediente in self.__ingredientes:
            dict_ingrediente = ingrediente.to_dict()
            list_dict_ingredientes.append(dict_ingrediente)
        return {
            "nome": self.__nome,
            "id": self.id,
            "ingredientes": list_dict_ingredientes,
            "tipo": self.tipo
        }