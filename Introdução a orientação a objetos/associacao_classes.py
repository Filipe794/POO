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

# Agregação

class Aluno:
    def __init__(self, nome: str, matricula: str, nota: float):
        self.nome = nome
        self.matricula = matricula
        self.nota = nota
class Curso:
    def __init__(self, nome: str, professor: str):
        self.nome = nome
        self.professor = professor
        self.__alunos = []

    def adicionar_aluno(self, aluno: 'Aluno') -> None:
        self.__alunos.append(aluno)

    def remover_aluno(self, aluno:Aluno) -> None:
        if aluno in self._alunos:
            self.__alunos.remove(aluno)

    def obter_alunos(self):
        return self.__alunos

# Composição

class Contato:
    def __init__(self, email: str, telefone: str):
        self.email = email
        self.telefone = telefone
    def __del__(self):
      print("Apagando...")

class Cliente:
    def __init__(self, nome: str, cnpj: str, contato=[]):
        self.nome = nome
        self.cnpj = cnpj
        self.contato = contato
    

    def add_contato(self, email: str, telefone: str) -> None:
        novo_contato = Contato(email, telefone)
        self.contato.append(novo_contato)

    def detalhes(self) -> None:
        print(f"{self.nome}, CNPJ: {self.cnpj}")
        print("Contatos:")
        for contato in self.contato:
            print(f" E-mail: {contato.email}, Telefone: {contato.telefone}")

meu_cliente = Cliente("João Silva", "00.000.000/0001-00")
meu_cliente.add_contato("joao.silva@hotmail.com", "+55 11 1234-5678")
meu_cliente.add_contato("joao.silva@gmail.com", "+55 11 9876-5432")
meu_cliente.detalhes()