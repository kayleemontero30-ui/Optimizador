#Solo para iniciar el programa, no tiene nada que ver con la lógica del optimizador.

def main():
    print("Bienvenido al optimizador de rutas para el delivery de comida.")
    print("Por favor, ingrese los datos necesarios para calcular la ruta óptima.")
    # Aquí podrías llamar a funciones de menu.py para obtener los datos del usuario
    # y luego a funciones de datos.py para procesar esos datos y calcular la ruta óptima.
if __name__ == "__main__":
    main()
    while True:
        print(""" 
              ~~~ Optimizador de Rutas ~~~
            1. Mostrar Tareas Pendientes
            2. Agregar Tarea
            3. Eliminar Tarea
            4. Salir
              """)
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            # Aquí podrías llamar a una función de menu.py para mostrar las tareas pendientes
            pass
        elif opcion == "2":
            # Aquí podrías llamar a una función de menu.py para agregar una tarea
            pass
        elif opcion == "3":
            # Aquí podrías llamar a una función de menu.py para eliminar una tarea
            pass
        elif opcion == "4":
            print("Gracias por usar el optimizador de rutas. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, intente nuevamente.")