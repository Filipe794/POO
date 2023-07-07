class Cartao:
    def __init__(self,tipo,numero,id):
        self.__tipo = tipo
        self.id = id
        self.__numero = numero
        self.__cliente = id

    def mostra_info(self):
        print(f"Modalidade: {self.__tipo} Número: {self.__numero}")
    
    @property
    def cliente(self):
        return self.__cliente
    
    def to_dict(self):
        return {
            "tipo": self.__tipo,
            "numero": self.__numero,
            "id": self.id
        }

