class Aluno:
    def __init__(self, nome,ra,notas):
        self.nome= nome
        self.ra = ra
        self.notas = notas
       
    def mostrarSituacao(self):
        media = sum(self.notas) / len(self.notas)

        if media < 5:
            return "REPROVADO"
        elif media >=5 and media <= 6.9:
            return "EXAME"
        else:
            return "APROVADO"
        
notas = []
nome = input("DIGITE O NOME: ")
ra = int(input("DIGITE O RA: "))

i = 0
while i < 4:
    nota = float(input("DIGITE A NOTA: "))
    notas.append(nota)
    i = i + 1

a = Aluno(nome,ra,notas)
print(a.mostrarSituacao())

