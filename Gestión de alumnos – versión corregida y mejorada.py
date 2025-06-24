# Lista para almacenar alumnos
lista_alumnos = []

def pedir_float(mensaje, minimo=1.0, maximo=7.0):
    while True:
        try:
            valor = float(input(mensaje))
            if not (minimo <= valor <= maximo):
                print(f"Debe ingresar un número entre {minimo} y {maximo}.")
                continue
            return valor
        except ValueError:
            print("Error: ingrese un número válido.")

def pedir_int(mensaje, minimo=1):
    while True:
        try:
            valor = int(input(mensaje))
            if valor < minimo:
                print(f"Debe ser mayor o igual a {minimo}.")
                continue
            return valor
        except ValueError:
            print("Error: ingrese un número entero válido.")

def agregar_alumno():
    nombre = input("Ingrese nombre del alumno: ").strip()
    edad = pedir_int("Ingrese edad del alumno: ", minimo=3)

    notas = []
    for i in range(3):
        nota = pedir_float(f"Ingrese nota {i+1} (1.0 - 7.0): ")
        notas.append(nota)

    alumno = {
        "nombre": nombre,
        "edad": edad,
        "notas": notas
    }

    lista_alumnos.append(alumno)
    print("Alumno registrado con éxito.\n")

def mostrar_lista():
    if not lista_alumnos:
        print("No hay alumnos registrados.\n")
        return
    print("--- Lista de alumnos ---")
    for alumno in lista_alumnos:
        print(f"Nombre: {alumno['nombre']}")
        print(f"Edad: {alumno['edad']}")
        print(f"Notas: {alumno['notas']}")
        promedio = sum(alumno['notas']) / len(alumno['notas'])
        print(f"Promedio: {promedio:.2f}")
        print("-" * 30)

def buscar_alumno():
    nombre_buscar = input("Ingrese nombre del alumno a buscar: ").strip().lower()
    for alumno in lista_alumnos:
        if alumno["nombre"].lower() == nombre_buscar:
            print("Alumno encontrado:")
            print(f"Nombre: {alumno['nombre']}")
            print(f"Edad: {alumno['edad']}")
            print(f"Notas: {alumno['notas']}")
            promedio = sum(alumno['notas']) / len(alumno['notas'])
            print(f"Promedio: {promedio:.2f}\n")
            return
    print("Alumno no encontrado.\n")

def calcular_promedio_general():
    if not lista_alumnos:
        print("No hay alumnos registrados.\n")
        return
    total = sum(sum(alumno['notas']) for alumno in lista_alumnos)
    cantidad = sum(len(alumno['notas']) for alumno in lista_alumnos)
    promedio_general = total / cantidad
    print(f"Promedio general de todos los alumnos: {promedio_general:.2f}\n")

# Menú principal
def menu_alumnos():
    while True:
        print("\n*** Menú de Alumnos ***")
        print("1) Agregar alumno")
        print("2) Ver lista de alumnos")
        print("3) Buscar alumno por nombre")
        print("4) Calcular promedio general")
        print("5) Salir")

        opcion = input("Ingrese una opción: ").strip()
        if opcion == "1":
            agregar_alumno()
        elif opcion == "2":
            mostrar_lista()
        elif opcion == "3":
            buscar_alumno()
        elif opcion == "4":
            calcular_promedio_general()
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente de nuevo.\n")

menu_alumnos()
