import matplotlib.pyplot as plt

def agregar_tarea(tareas, id_tarea, datos):
    tareas[id_tarea] = datos


def agregar_relacion(grafo, origen, destino, coste):
    if origen not in grafo:
        grafo[origen] = {}

    grafo[origen][destino] = coste #--- IGNORE ---