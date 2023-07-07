# class Aluno:
#     def __init__(self, nome: str, matricula: str):
#         self.nome = nome
#         self.matricula = matricula
# class Curso:
#     def __init__(self, nome: str, codigo):
#         self.nome = nome
#         self.codigo = codigo
#         self.aluno = None

# # Criando objetos Aluno
# aluno1 = Aluno("João", "123")
# aluno2 = Aluno("Maria", "456")

# # Criando objetos Curso
# curso1 = Curso("Python para Iniciantes", "P101")
# curso2 = Curso("Java Avançado", "J201")

# # Associando alunos aos cursos
# curso1.aluno = aluno1
# curso2.aluno = aluno2

# # Exibindo os detalhes dos alunos e cursos
# print(f"Detalhes do Aluno {aluno1.nome}:")
# print(f"Nome: {aluno1.nome}")
# print(f"Matrícula: {aluno1.matricula}")
# print(f"Curso Associado: {curso1.nome}\n")

# print(f"Detalhes do Aluno {aluno2.nome}:")
# print(f"Nome: {aluno2.nome}")
# print(f"Matrícula: {aluno2.matricula}")
# print(f"Curso Associado: {curso2.nome}")


# class Item:
#     def __init__(self,nome : str, preco: float):
#         self.nome = nome
#         self.preco = preco

# class Pedido:
#     def __init__(self, numero: int, data: str):
#         self.numero = numero
#         self.data = data
#         self.itens = []
    
#     def listar_item(self):
#         for item in self.itens:
#             print(f"Produto: {item.nome} Preço: {item.preco}")
    
#     def adicionar_item(self, item: Item):
#         self.itens.append(item)


# class Cliente:
#     def __init__(self, nome: str, email: str):
#         self.nome = nome
#         self.email = email
#         self.pedidos = []

#     def listar_pedidos(self):
#         i = 1
#         for pedido in self.pedidos:
#             print(f"Pedido nº {i}")
#             pedido.listar_item
#             i+=1

#     def adicionar_pedido(self, pedido):
#         self.pedidos.append(pedido)


# # Cadastrando um cliente
# cliente1 = Cliente("João", "joao@example.com")

# # Criando um pedido para o cliente
# pedido1 = Pedido(1, "2023-05-16")

# # Adicionando produtos ao pedido
# produto1 = Item("Camiseta", 29.99)
# produto2 = Item("Calça", 49.99)

# pedido1.adicionar_item(produto1)
# pedido1.adicionar_item(produto2)

# # Associando o pedido ao cliente
# cliente1.adicionar_pedido(pedido1)

# # Exibindo os detalhes do cliente, seus pedidos e os produtos de cada pedido
# print("Detalhes do Cliente:")
# print(f"Nome: {cliente1.nome}")
# print(f"E-mail: {cliente1.email}")

# print("\nPedidos do Cliente:")
# cliente1.listar_pedidos()

# class Projeto:
#     def __init__(self,nome,descricao):
#         self.nome = nome
#         self.descricao = descricao

# class Funcionario:
#     def __init__(self,nome,salario):
#         self.nome = nome
#         self.salario = salario

# class Departamento:
#     def __init__(self,nome,descricao):
#         self.nome = nome
#         self.descricao = descricao
#         self.funcionarios = []
#         self.projeto = None

#     def adicionar_funcionario(self, funcionario):
#         self.funcionarios.append(funcionario)

#     def definir_projeto(self, projeto):
#         self.projeto = projeto
    
#     def listar_funcionarios(self):
#         for funcionario in self.funcionarios:
#             print(f"Funcionario: {funcionario.nome} Salario: {funcionario.salario}")

# class Empresa:
#     def __init__(self, nome, endereco):
#         self.nome = nome
#         self.endereco = endereco
#         self.departamentos = []
#     def adicionar_departamento(self,departamento):
#         self.departamento.append(departamento)
#     def listar_departamentos(self):
#         for departamento in self.departamentos:
#             print(f"Funcionario: {departamento.nome} Salario: {departamento.descricao}")

class Autor:
    def __init__(self, nome, pais):
        self.nome = nome
        self.pais = pais
    def print_info(self):
        print(f"Autor: {self.nome} Pais: {self.pais}")

class Exemplar:
    def __init__(self,numero):
        self.numero = numero
        self.status = True

    def disponivel(self):
        return self.status

    def mudar_status(self):
        if self.status:
            self.status = False
        else:
            self.status = True

    def print_info(self):
        print(f"Numero Exemplar: {self.numero} Status: {self.status}")

class Livro:
    def __init__(self,titulo,ano,autor):
        self.titulo = titulo
        self.ano = ano
        self.autor = autor
        self.exemplares = []

    def adicionar_exemplar(self,codigo_exemplar):
        self.exemplares.append(Exemplar(codigo_exemplar))
    
    def print_info(self):
        print(f"Titulo: {self.titulo} Ano: {self.Ano} Autor: {self.Autor} Quantidade de Exemplares: {len(self.exemplares)}")

class Emprestimo:
    def __init__(self,usuario, data_emprestimo):
        self.usuario = usuario
        self.data_emprestimo = data_emprestimo

    def adicionar_exemplar(self,livro: Livro):
        if len(livro.exemplares) > 0:
            for exemplar in livro.exemplares:
                if exemplar.disponivel:
                    exemplar.mudar_status()
                    self.exemplar.append(exemplar)
                    break               
        else:
            print("Nao tem exemplares cadastrados")

    def finalizar(self):
        for exemplar in self.exemplares:
            exemplar.mudar_status()
    
    def print_info(self):
        print(f"Usuario: {self.usuario} Data Emprestimo: {self.data_emprestimo} Exemplar: {self.exemplar.print_info}")