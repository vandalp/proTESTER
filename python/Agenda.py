from datetime import datetime

class Agenda:
    def __init__(self, dia, mes, ano, anotacao=""):
        self.dia = dia
        self.mes = mes
        self.ano = ano
        self.anotacao = anotacao

    def validar_data(self):
        try:
            datetime(year=self.ano, month=self.mes, day=self.dia)
            return True
        except ValueError:
            return False

    def anotar_tarefa(self, nova_anotacao):
        if self.validar_data():
            self.anotacao = nova_anotacao
            print("Anotação registrada com sucesso.")
        else:
            print("Data inválida. Não é possível registrar a anotação.")

    def mostrar_anotacao(self):
        if self.anotacao:
            print(f"Anotação para {self.dia}/{self.mes}/{self.ano}: {self.anotacao}")
        else:
            print(f"Não há anotação para {self.dia}/{self.mes}/{self.ano}.")


agenda = Agenda(dia=5, mes=7, ano=2024)
if agenda.validar_data():
    print("Data válida.")
else:
    print("Data inválida.")

agenda.anotar_tarefa("Reunião com o cliente às 10h.")
agenda.mostrar_anotacao()


agenda_invalida = Agenda(dia=31, mes=2, ano=2024)
if agenda_invalida.validar_data():
    print("Data válida.")
else:
    print("Data inválida.")

agenda_invalida.anotar_tarefa("Reunião importante.")
agenda_invalida.mostrar_anotacao()
