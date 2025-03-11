import tkinter as tk
from Comprobador import Comprobador  

class Ventana:
    def __init__(self, root):
        self.root = root
        self.root.title("Comprobador de Valores")
        self.root.geometry("300x200")
        self.verificador = Comprobador() 
        self.crear_interfaz()

    def crear_interfaz(self):
        self.etiqueta = tk.Label(self.root, text="Ingrese un número entre 0 y 20")
        self.etiqueta.pack(pady=10)

        self.campo_texto = tk.Entry(self.root)
        self.campo_texto.pack(pady=10)

        self.boton_verificar = tk.Button(self.root, text="Comprobar", command=self.verificar_numero)
        self.boton_verificar.pack(pady=10)

    def verificar_numero(self):
        try:
            valor = int(self.campo_texto.get())
            if self.verificador.es_valido(valor):
                self.etiqueta.config(text=f"Valor correcto: {valor}", fg="green")
            else:
                self.etiqueta.config(text="Número fuera de rango", fg="red")
            self.campo_texto.delete(0, tk.END)
        except ValueError:
            self.etiqueta.config(text="Entrada no válida", fg="red")
            self.campo_texto.delete(0, tk.END)

# Bloque para ejecutar la aplicación
if __name__ == "__main__":
    raiz = tk.Tk()
    app = Ventana(raiz)
    raiz.mainloop()
