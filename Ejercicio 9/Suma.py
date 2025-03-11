class Acumulador100:
    def __init__(self):
        self.suma_total = 0  

    def incrementar(self, valor):
        if not self.limite_alcanzado():
            self.suma_total += valor  
        return self.suma_total  

    def limite_alcanzado(self):
        return self.suma_total >= 100