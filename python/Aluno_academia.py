class Aluno_Academia:
    def __init__(self, nome, idade, peso, altura, mensalidade=120.00):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
        self.mensalidade = mensalidade

    def calcular_imc(self):
        imc = self.peso / (self.altura ** 2)
        return imc

    def obter_valor_mensalidade(self):
        if self.idade < 18:
            desconto = 0.10
            valor_com_desconto = self.mensalidade * (1 - desconto)
            return valor_com_desconto
        return self.mensalidade

    def exibir_informacoes(self):
        imc = self.calcular_imc()
        mensalidade = self.obter_valor_mensalidade()
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Peso: {self.peso} kg")
        print(f"Altura: {self.altura} m")
        print(f"IMC: {imc:.2f}")
        print(f"Mensalidade: R${mensalidade:.2f}")


nome = input("Informe o nome do aluno: ")
idade = int(input("Informe a idade do aluno: "))
peso = float(input("Informe o peso do aluno (em kg): "))
altura = float(input("Informe a altura do aluno (em metros): "))

aluno = Aluno_Academia(nome=nome, idade=idade, peso=peso, altura=altura)

aluno.exibir_informacoes()
