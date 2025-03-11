
class GestorNumeros:
    def __init__(self):
        self.numeros_ingresados = [] 

    def incrementar_contador(self, numero):
    
        self.numeros_ingresados.append(numero)
        return len(self.numeros_ingresados) 