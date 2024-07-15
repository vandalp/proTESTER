class Estudante:
    def __init__(self, matricula, nome, idade, nota):
        self.matricula = matricula
        self.nome = nome
        self.idade = idade
        self.nota = nota

        def hello(self):
            print(f"Olá {self.nome}")


aluno = Estudante(1212, "pedro", 18, 80)
print(aluno.nome)
aluno2 = Estudante(1313, "domittila",22,90)
print(aluno2.nome)

aluno2.hello()