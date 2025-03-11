import tkinter as tk
from tkinter import messagebox
from Numero import Numero 

class Aplicacion:
    def __init__(self, root):
        self.root = root
        self.root.title("Validador de Número")

        self.numero_label = tk.Label(self.root, text="Introduce un número:")
        self.numero_label.pack(pady=10)

        self.numero_entry = tk.Entry(self.root)
        self.numero_entry.pack(pady=10)

        self.validar_button = tk.Button(self.root, text="Validar", command=self.validar)
        self.validar_button.pack(pady=10)

    def validar(self):
        numero_obj = Numero()
        while True:
            try:
                numero = int(self.numero_entry.get()) 
                if numero_obj.validar_numero(numero):  
                    
                    messagebox.showinfo("Resultado", f"El número ingresado es: {numero}")
                    break 
                else:
                    messagebox.showwarning("Advertencia", "El número debe ser menor que 10. Inténtalo de nuevo.")
                    self.numero_entry.delete(0, tk.END)  
                    break  
            except ValueError:
                messagebox.showerror("Error", "Por favor ingresa un número válido.")
                self.numero_entry.delete(0, tk.END)  


