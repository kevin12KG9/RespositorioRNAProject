# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 20:42:56 2023

@author: User
"""

import tkinter as tk
from tkinter import filedialog

def seleccionar_archivo():
    archivo = filedialog.askopenfilename(filetypes=[("Archivos de Excel", "*.xlsx"), ("Todos los archivos", "*.*")])
    if archivo:
        entrada_archivo.delete(0, tk.END)
        entrada_archivo.insert(0, archivo)

def pronosticar_demanda():
    archivo_seleccionado = entrada_archivo.get()
    # Aquí puedes agregar el código para procesar el archivo seleccionado y realizar el pronóstico de demanda
    
# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Pronóstico de Demanda")

# Crear un frame
frame = tk.Frame(ventana)
frame.pack(padx=20, pady=20)

# Etiqueta para el archivo
etiqueta_archivo = tk.Label(frame, text="Seleccionar archivo:")
etiqueta_archivo.pack()

# Entrada de texto para mostrar la ruta del archivo
entrada_archivo = tk.Entry(frame, width=40)
entrada_archivo.pack()

# Botón para seleccionar archivo
boton_seleccionar = tk.Button(frame, text="Seleccionar archivo", command=seleccionar_archivo)
boton_seleccionar.pack()

# Botón para pronosticar demanda
boton_pronosticar = tk.Button(frame, text="Pronosticar Demanda", command=pronosticar_demanda)
boton_pronosticar.pack()

# Ejecutar la aplicación
ventana.mainloop()
