import tkinter as tk
from Suma import Calculadora  

class Ventana:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de Suma")
        self.root.geometry("320x220")  
        self.crear_interfaz()  

    def crear_interfaz(self):
        """Configura la interfaz gráfica."""
        self.label = tk.Label(self.root, text="Introduce un número entero:")
        self.label.pack(pady=8)

        self.entry = tk.Entry(self.root)
        self.entry.pack(pady=8)

        self.button = tk.Button(self.root, text="Obtener Suma", command=self.calcular)
        self.button.pack(pady=8)

        self.result_label = tk.Label(self.root, text="Resultado: ", fg="blue")
        self.result_label.pack(pady=8)

    def calcular(self):
        """Ejecuta la función al presionar el botón."""
        try:
            cantidad = int(self.entry.get())
            calculo = Calculadora(cantidad)
            resultado = calculo.obtener_suma()  

            if resultado is not None:
                self.result_label.config(text=f"Resultado: {resultado}", fg="green")
            else:
                self.result_label.config(text="Número inválido", fg="red")  

            self.entry.delete(0, tk.END)  

        except ValueError:
            self.result_label.config(text="Ingrese un número válido", fg="red")  
            self.entry.delete(0, tk.END)
