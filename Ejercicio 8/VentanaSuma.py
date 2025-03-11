import tkinter as tk
from Acumulador import Acumulador  

class VentanaSuma:
    def __init__(self, root):
        self.root = root
        self.root.title("Suma Progresiva")  
        self.root.geometry("320x220")  
        self.acumulador = Acumulador()  

        self.crear_interfaz()

    def crear_interfaz(self):
        """Configura la interfaz gráfica"""
        self.label = tk.Label(self.root, text="Ingrese un número (0 para finalizar):")
        self.label.pack(pady=8)

        self.entry = tk.Entry(self.root)
        self.entry.pack(pady=8)

        self.button = tk.Button(self.root, text="Añadir", command=self.agregar_valor)
        self.button.pack(pady=8)

        self.result_label = tk.Label(self.root, text="Total acumulado: 0", fg="blue")
        self.result_label.pack(pady=8)

    def agregar_valor(self):
        """Función que se ejecuta al presionar el botón"""
        try:
            valor = int(self.entry.get())  
            total = self.acumulador.sumar_valor(valor)  

            if valor == 0:
                self.label.config(text="Cálculo finalizado. Total:")
                self.button.config(state=tk.DISABLED)
                self.entry.config(state=tk.DISABLED)

            self.result_label.config(text=f"Total acumulado: {total}")  
            self.entry.delete(0, tk.END)  

        except ValueError:
            self.result_label.config(text="Ingrese un número válido", fg="red")  
            self.entry.delete(0, tk.END)