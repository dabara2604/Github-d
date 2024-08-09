# Lista para almacenar las tareas
tareas = []

def agregar_tarea(tarea):
    tareas.append(tarea)
    print(f'Tarea "{tarea}" agregada.')

def ver_tareas():
    if tareas:
        print("Tareas:")
        for i, tarea in enumerate(tareas, 1):
            print(f"{i}. {tarea}")
    else:
        print("No hay tareas.")

def eliminar_tarea(indice):
    try:
        tarea = tareas.pop(indice - 1)
        print(f'Tarea "{tarea}" eliminada.')
    except IndexError:
        print("Índice de tarea inválido.")

# Ciclo principal de la aplicación
while True:
    print("\nAdministrador de Tareas")
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Eliminar tarea")
    print("4. Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        tarea = input("Ingrese la tarea: ")
        agregar_tarea(tarea)
    elif opcion == "2":
        ver_tareas()
    elif opcion == "3":
        try:
            indice = int(input("Ingrese el número de la tarea a eliminar: "))
            eliminar_tarea(indice)
        except ValueError:
            print("Por favor, ingrese un número válido.")
    elif opcion == "4":
        print("Saliendo...")
        break
    else:
        print("Opción no válida. Intente de nuevo.")
