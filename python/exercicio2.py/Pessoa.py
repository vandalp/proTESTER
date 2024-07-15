class Pessoa:
    def __init__(self,matricula, nome, idade):
        self.cadastro = matricula 
        self.nome = nome 
        self.idade = idade 

    def getDados(self):
        print(self.cadastro)
        print(self.nome)
        print(self.idade)