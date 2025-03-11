class Acumulador:
    def __init__(self):
        self.suma_total = 0

    def sumar_valor(self, valor):
        if valor != 0:
            self.suma_total += valor
        return self.suma_total