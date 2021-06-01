class Relogio():
    def __init__(self):  # método para calcular o tempo
        self.horas = 7
        self.minutos = 0
        self.dia = 1

    def __str__(self):
        return f'{self.horas:02d}:{self.minutos:02d} do dia {self.dia:02d}'

    def avancaTempo(self, minutos):
        self.minutos += minutos
        while self.minutos >= 60:
            self.minutos -= 60
            self.horas += 1
        if self.horas >= 24:
            self.dia += 1
            self.horas -= 20

    def passarDia(self):  # Função para passar +1 dia
        self.horas += 8

    def get_data(self):
        if self.dia == 7 and self.horas >= 7:
            return 1

    def get_noite(self):
        if self.horas >= 20 or self.horas <= 6:
            print('Perigos espreitam a noite... é melhor se abrigar.')
            return True
        else:
            return False
