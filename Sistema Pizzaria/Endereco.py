class Endereco:
    def __init__(self,descricao, id_endereco):
        self.__descricao = descricao
        self.__cliente = id_endereco
        self.id = id_endereco

    @property
    def descricao(self):
        return self.__descricao
    
    def set_descricao(self,descricao):
        self.__descricao = descricao
    
    def set_cliente(self,cliente):
        self.__cliente = cliente

    @property
    def cliente(self):
        return self.__cliente

    def to_dict(self):
        return {
            "descricao": self.__descricao,
            "id": self.id
        }