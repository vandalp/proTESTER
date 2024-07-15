class Pessoa:
    def __init__(self,id = 0, nome=""):
        self.id = id
        self.nome = nome

    def hello(self):
        print("Olá")

pes1 =Pessoa()
print(pes1.id)

print("bom dia!!!")
name = input("digite seu nome: ")

pes1.nome=name

pes1.hello()
        
