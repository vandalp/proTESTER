class Carro:
    def __init__(self,modelo,marca,cor,ano,valor,nivel= 5):
        self.modelo = modelo
        self.marca =  marca
        self.cor = cor 
        self.ano = ano
        self.valor = valor
        self.nivel = nivel

    def calcular_imposto(self):
            imposto = (self.valor * 3) / 100
            return imposto

    def ligar(self):
        print(f" {self.modelo}Ligado!!!!!")

    def abastecer(self,qtde_litros):
         self.nivel = self.nivel + qtde_litros

    def andar(self):
         print("estou andando.....")


car1 = Carro("jetta","volks", "prata",2022,120000)
print(car1.calcular_imposto())
car1.ligar()
print("NIVEL DE GASOLINA", car1.nivel, "litros")
car1.abastecer(45)
print("NIVEL DE GASOLINA", car1.nivel, "litros")
car1.andar()