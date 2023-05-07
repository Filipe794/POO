class Aluno:
    qnt_alunos = 0
    def __init__(self,nome):
        self.nome = nome
        Aluno.qnt_aluno+=1

a1 = Aluno("Filipe",134234)
a2 = Aluno("Bet",763234)