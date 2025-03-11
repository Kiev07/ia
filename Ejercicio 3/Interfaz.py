import tkinter as tk
from tkinter import messagebox
from descuento import Descuento  

class Aplicacion:
    def __init__(self, root):
        self.root = root
        self.root.title("Cálculo de Descuento")

        
        self.mes_label = tk.Label(self.root, text="Introduce el mes:")
        self.mes_label.pack(pady=10)

        self.mes_entry = tk.Entry(self.root)
        self.mes_entry.pack(pady=10)

        self.importe_label = tk.Label(self.root, text="Introduce el importe de la compra:")
        self.importe_label.pack(pady=10)

        self.importe_entry = tk.Entry(self.root)
        self.importe_entry.pack(pady=10)

        
        self.calcular_button = tk.Button(self.root, text="Calcular", command=self.calcular)
        self.calcular_button.pack(pady=10)

    def calcular(self):
        try:
            mes = self.mes_entry.get()  
            importe = float(self.importe_entry.get())  

            # Crear una instancia de la clase Descuento
            descuento_obj = Descuento(mes, importe)
            total_con_descuento = descuento_obj.calcular_descuento()

            # Mostrar el resultado
            messagebox.showinfo("Resultado", f"El total a cobrar es: {total_con_descuento:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Por favor ingresa un valor numérico válido para el importe.")


