class Conta:
    def __init__(self, nome, cpf, numero, saldo=0):
        self.nome = nome
        self.cpf = cpf
        self.numero = numero
        self.saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("Valor de depósito inválido.")

    def sacar(self, valor):
        if valor > 0:
            if self.saldo >= valor:
                self.saldo -= valor
                print(f"Saque de R${valor:.2f} realizado com sucesso.")
            else:
                print("Saldo insuficiente para realizar o saque.")
        else:
            print("Valor de saque inválido.")

    def imprimir_saldo(self):
        print(f"Saldo atual: R${self.saldo:.2f}")


conta = Conta(nome="João Silva", cpf="123.456.789-00", numero="12345-6", saldo=1000.0)
conta.imprimir_saldo()
conta.depositar(500.0)
conta.imprimir_saldo()
conta.sacar(200.0)
conta.imprimir_saldo()
conta.sacar(2000.0) 
conta.imprimir_saldo()
