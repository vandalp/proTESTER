class Nota_Fiscal:
    def __init__(self, numero, tipo, serie, cnpj, razao_social, data, valor_produtos, icms, frete, ipi):
        self.numero = numero
        self.tipo = tipo
        self.serie = serie
        self.cnpj = cnpj
        self.razao_social = razao_social
        self.data = data
        self.valor_produtos = valor_produtos
        self.icms = icms
        self.frete = frete
        self.ipi = ipi
        self.valor_total = 0.0

    def obter_numero(self):
        return self.numero

    def obter_data_emissao(self):
        return self.data

    def alterar_razao_social(self, nova_razao_social):
        self.razao_social = nova_razao_social

    def calcular_valor_total(self):
        self.valor_total = self.valor_produtos + self.frete + self.icms + self.ipi

    def exibir_informacoes(self):
        self.calcular_valor_total()
        print(f"Numero: {self.numero}")
        print(f"Tipo: {self.tipo}")
        print(f"Série: {self.serie}")
        print(f"CNPJ: {self.cnpj}")
        print(f"Razão Social: {self.razao_social}")
        print(f"Data: {self.data}")
        print(f"Valor Produtos: R${self.valor_produtos:.2f}")
        print(f"ICMS: R${self.icms:.2f}")
        print(f"Frete: R${self.frete:.2f}")
        print(f"IPI: R${self.ipi:.2f}")
        print(f"Valor Total: R${self.valor_total:.2f}")


numero = int(input("Informe o número da Nota Fiscal: "))
tipo = input("Informe o tipo da Nota Fiscal (Entrada/Saída): ")
serie = int(input("Informe a série da Nota Fiscal (1, 2 ou 3): "))
cnpj = input("Informe o CNPJ: ")
razao_social = input("Informe a razão social: ")
data = input("Informe a data de emissão (dd/mm/yyyy): ")
valor_produtos = float(input("Informe o valor dos produtos: "))
icms = float(input("Informe o valor do ICMS: "))
frete = float(input("Informe o valor do frete: "))
ipi = float(input("Informe o valor do IPI: "))

nota_fiscal = Nota_Fiscal(numero, tipo, serie, cnpj, razao_social, data, valor_produtos, icms, frete, ipi)


nota_fiscal.exibir_informacoes()


nova_razao_social = input("Informe a nova razão social: ")
nota_fiscal.alterar_razao_social(nova_razao_social)
nota_fiscal.exibir_informacoes()
