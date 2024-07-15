import math

class Triangulo:
    def __init__(self, ladoA, ladoB, ladoC):
        self.ladoA = ladoA
        self.ladoB = ladoB
        self.ladoC = ladoC

    def calcular_perimetro(self):
        return self.ladoA + self.ladoB + self.ladoC

    def get_maior_lado(self):
        return max(self.ladoA, self.ladoB, self.ladoC)

    def calcular_area(self):
        
        semi_perimetro = self.calcular_perimetro() / 2
        area = math.sqrt(semi_perimetro * (semi_perimetro - self.ladoA) * 
                         (semi_perimetro - self.ladoB) * (semi_perimetro - self.ladoC))
        return area


ladoA = float(input("Informe o valor do lado A do triângulo: "))
ladoB = float(input("Informe o valor do lado B do triângulo: "))
ladoC = float(input("Informe o valor do lado C do triângulo: "))


triangulo = Triangulo(ladoA, ladoB, ladoC)


print(f"Perímetro do triângulo: {triangulo.calcular_perimetro():.2f}")
print(f"Área do triângulo: {triangulo.calcular_area():.2f}")
print(f"Maior lado do triângulo: {triangulo.get_maior_lado():.2f}")
