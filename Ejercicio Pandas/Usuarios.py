import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd

usuarios_data = pd.read_csv("usuarios.csv")

def mostrar_ventana_consultas():
    global tabla_datos  

    ventana_consultas = tk.Tk()
    ventana_consultas.title("Sistema de Análisis Financiero")
    ventana_consultas.geometry("700x500")
    ventana_consultas.configure(bg="#D0F0C0")

    datos_financieros = pd.read_csv("datos_financieros.csv")

    frame_input = tk.Frame(ventana_consultas, bg="#98FB98")
    frame_input.pack(pady=15)

    lbl_consulta = tk.Label(frame_input, text="Ingrese consulta (Ej: ingresos > 2500):", font=("Arial", 10), bg="#98FB98", fg="black")
    lbl_consulta.pack(side="left", padx=5)

    entrada_consulta = tk.Entry(frame_input, width=40)
    entrada_consulta.pack(side="left", padx=5)

    btn_ejecutar = tk.Button(frame_input, text="Ejecutar", bg="#6A5ACD", fg="white", command=lambda: ejecutar_consulta(entrada_consulta.get(), datos_financieros))
    btn_ejecutar.pack(side="left", padx=5)

    frame_output = tk.Frame(ventana_consultas, bg="#8A2BE2")
    frame_output.pack(pady=10, expand=True, fill="both")

    columnas = list(datos_financieros.columns)
    tabla_datos = ttk.Treeview(frame_output, columns=columnas, show="headings")
    for col in columnas:
        tabla_datos.heading(col, text=col)
        tabla_datos.column(col, width=120)
    tabla_datos.pack(expand=True, fill="both")

    ventana_consultas.mainloop()

def ejecutar_consulta(consulta, datos):
    try:
        resultado = datos.query(consulta)
        for fila in tabla_datos.get_children():
            tabla_datos.delete(fila)
        for _, fila in resultado.iterrows():
            tabla_datos.insert("", "end", values=list(fila))
    except Exception as e:
        messagebox.showerror("Error de consulta", f"Error al ejecutar la consulta: {e}")

def validar_credenciales():
    usuario = entrada_usuario.get().strip()
    clave = entrada_clave.get().strip()
    
    usuarios_data["usuario"] = usuarios_data["usuario"].astype(str).str.strip()
    usuarios_data["contraseña"] = usuarios_data["contraseña"].astype(str).str.strip()

    if ((usuarios_data["usuario"].eq(usuario)) & (usuarios_data["contraseña"].eq(clave))).any():
        messagebox.showinfo("Acceso concedido", f"Bienvenido, {usuario}")
        ventana_inicio.destroy()
        mostrar_ventana_consultas()
    else:
        messagebox.showerror("Error", "Usuario o contraseña incorrectos")

ventana_inicio = tk.Tk()
ventana_inicio.title("Inicio de Sesión")
ventana_inicio.geometry("300x150")
ventana_inicio.configure(bg="#D0F0C0")

tk.Label(ventana_inicio, text="Usuario:", font=("Arial", 10), bg="#D0F0C0", fg="black").grid(row=0, column=0, pady=5, padx=5)
entrada_usuario = tk.Entry(ventana_inicio)
entrada_usuario.grid(row=0, column=1, pady=5, padx=5)

tk.Label(ventana_inicio, text="Contraseña:", font=("Arial", 10), bg="#D0F0C0", fg="black").grid(row=1, column=0, pady=5, padx=5)
entrada_clave = tk.Entry(ventana_inicio, show="*")
entrada_clave.grid(row=1, column=1, pady=5, padx=5)

btn_ingresar = tk.Button(ventana_inicio, text="Ingresar", bg="#6A5ACD", fg="white", command=validar_credenciales)
btn_ingresar.grid(row=2, column=0, columnspan=2, pady=10)

ventana_inicio.mainloop()

