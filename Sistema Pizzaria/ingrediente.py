class Ingrediente:
    def __init__(self,nome):
        self.nome=nome
        self.preco = None
    def definir_preco(self, valor):
        self.preco = valor
        
    def display(self):
        print(f"{self.nome} R${self.preco}\n")

    def to_dict(self):
        return {
            "nome": self.nome,
            "preco": self.preco
        }