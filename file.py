import json
import tkinter as tk
from tkinter import filedialog
import matplotlib.pyplot as plt

def leer_json(filepath):
    with open(filepath, 'r') as file:
        data = json.load(file)
    return data

def graficar_resultados(algoritmo, procesos):
    nombres = [p['nombre'] for p in procesos]
    inicio = [p['tiempo_salida'] for p in procesos]
    duracion = [p['tiempo_final'] - p['tiempo_salida'] for p in procesos]

    plt.barh(nombres, duracion, left=inicio, color='skyblue')
    plt.title(f"Algoritmo {algoritmo}")
    plt.xlabel("Tiempo")
    plt.ylabel("Procesos")
    plt.show()

def seleccionar_archivo():
    filepath = filedialog.askopenfilename(title="Selecciona el archivo JSON",
                                          filetypes=(("JSON files", "*.json"), ("All files", "*.*")))
    return filepath

def main():
    root = tk.Tk()
    root.withdraw()  # Ocultar la ventana principal de Tkinter
    
    archivo = seleccionar_archivo()
    if not archivo:
        print("No se seleccionó ningún archivo.")
        return
    
    data = leer_json(archivo)

    for algoritmo, procesos in data.items():
        graficar_resultados(algoritmo, procesos)

if __name__ == "__main__":
    main()
