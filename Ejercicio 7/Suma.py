
class Calculadora:
    def __init__(self, cantidad):
        self.cantidad = cantidad  

    def obtener_suma(self):
        return (self.cantidad * (self.cantidad + 1)) // 2  

    def procesar_numero(self):
        return self.obtener_suma()
