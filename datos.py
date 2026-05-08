#guardar y cargar datos 
import json

def guardar_datos(tareas, grafo):
    with open("datos.json", "w") as archivo:
        json.dump({"tareas": tareas, "grafo": grafo}, archivo, indent=4)


def cargar_datos():
    with open("datos.json", "r") as archivo:
        return json.load(archivo)# --- IGNORE ---