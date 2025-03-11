
import tkinter as tk
from GestorNumeros import GestorNumeros  

class VentanaPrincipal:
    def __init__(self, root):
        self.root = root
        self.root.title("Registro de Números")  
        self.root.geometry("320x280")  
        self.root.configure(bg="#f0f0f0")  
        self.gestor = GestorNumeros()  
        self.crear_interfaz()

    def crear_interfaz(self):
        
        tk.Label(self.root, text="Ingrese un número:", font=("Arial", 12, "bold"), bg="#f0f0f0").pack(pady=10)

        self.entrada = tk.Entry(self.root, font=("Arial", 12))
        self.entrada.pack(pady=5)

        self.boton = tk.Button(self.root, text="Agregar", font=("Arial", 10), bg="#4CAF50", fg="white",
                               command=self.validar_entrada)
        self.boton.pack(pady=10)

        self.mensaje = tk.Label(self.root, text="", font=("Arial", 10), bg="#f0f0f0", fg="green")
        self.mensaje.pack()

        self.contador_label = tk.Label(self.root, text="Números registrados: 0", font=("Arial", 12, "bold"), bg="#f0f0f0", fg="blue")
        self.contador_label.pack(pady=10)

    def validar_entrada(self):
        """Procesa la entrada del usuario y actualiza el contador."""
        try:
            numero = float(self.entrada.get())  
            total = self.gestor.incrementar_contador(numero)

            self.mensaje.config(text=f"Número registrado: {numero}")
            self.contador_label.config(text=f"Números registrados: {total}")  
            self.entrada.delete(0, tk.END) 
        except ValueError:
            self.mensaje.config(text="Entrada no válida", fg="red")
            self.entrada.delete(0, tk.END)  
