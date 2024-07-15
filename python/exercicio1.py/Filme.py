class Filme:
    def __init__(self,nome,duracao):
        self.nome = nome 
        self.duracao = duracao

    def setNome(self,novo_nome):
        self.nome = novo_nome

    def getNome(self):
        return self.nome
    
    def play(self):
        print(f"{self.nome}começou...")

    def getDuracao(self):
        return self.duracao
    
class Drama(Filme):
    def __init__(self, nome, duracao,ator):
        super().__init__(nome, duracao)
        self.ator = ator 

    def play(self):
        print(f"{self.nome} comecou a chorar...")


class Terror(Filme):
    def __init__(self, nome, duracao,ator):
        super().__init__(nome, duracao)
        self.ator = ator 

    def play(self):
        print(f"{self.nome} comecou a ficar com medo...")        

