from Pessoa import Pessoa 

class Professor(Pessoa):
    def __init__(self, matricula, nome, idade,formacao,disciplina,cargahora,salario):
        super().__init__(matricula, nome, idade)
        self.formacao = formacao
        self.disciplina = disciplina 
        self.cargahora = cargahora
        self.salario = salario

    def lecionar(self):
        return f'o melhor prof. {self.nome} acordou inspirado para lecionar'