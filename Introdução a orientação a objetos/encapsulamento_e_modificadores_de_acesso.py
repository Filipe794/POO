class ArmazenarDados:
  __dados={}
  def add_dados(self, cod:int, nome:str):
    self._ArmazenarDados__dados[cod] = nome
    
  def ver_dados(self):
        for cod,nome in self._ArmazenarDados__dados.items():
          print(f'{cod}: {nome}')
    
  def del_dados(self, cod:int):
       del self._ArmazenarDados__dados[cod]

# db=ArmazenarDados()
# db.add_dados(1,"Francois") 
# db.add_dados(2,"Maria") 
# db.add_dados(3,"Ana") 

# print('__Antes__')
# db.ver_dados()
# db.del_dados(2)

# print('__depois__')
# db.ver_dados()

class ContaBancaria:
  def __init__(self,saldo):
    if saldo < 0:
      print('Saldo nao pode ser negativo')
    else:
      self.__saldo = saldo
  
  @property
  def saldo(self):
    return self.__saldo

  @saldo.setter
  def saldo(self,saldo):
    if saldo < 0:
      print('Saldo nao pode ser negativo')
    else:
      self.__saldo = saldo