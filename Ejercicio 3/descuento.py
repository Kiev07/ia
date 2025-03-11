class Descuento:
    def __init__(self, mes, importe):
        self.mes = mes
        self.importe = importe

    def calcular_descuento(self):
        if self.mes.lower() == "octubre":
            descuento = 0.15 * self.importe
            total_con_descuento = self.importe - descuento
            return total_con_descuento
        else:
            return self.importe
