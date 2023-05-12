# Associação Simples
class Proprietario:
  def __init__(self,nome, cpf, endereco):
    self.nome = nome
    self.cpf = cpf
    self.endereco = endereco

class Carro:
  def __init__(self,modelo,ano, proprietario: Proprietario):
    self.marca = modelo
    self.ano = ano
    self.proprietario = proprietario

joao=Proprietario("Joao","001.154.458-22", "Rua da carniça")
c=Carro("Gol",2019,joao)

print(f'{joao.nome} tem um {c.modelo}')