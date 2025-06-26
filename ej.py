lista = []
minimo_caracteres = 8

def registrar_usuario(users):
    nombre = input("Ingrese nombre de usuario: ")
    # Verificar si el nombre ya existe
    if nombre in [usuario["nombre"] for usuario in users]:
        print("Error: El nombre ya existe.")
        return users
    
    sexo = input("Ingrese sexo: ")
    contrasena = input("Ingrese contraseña: ").strip()
    
    # Validar que la contraseña tenga al menos 8 caracteres
    while len(contrasena) < minimo_caracteres:
        print(f"La contraseña debe superar los {minimo_caracteres} caracteres. Inténtalo de nuevo.")
        contrasena = input("Ingrese contraseña: ").strip()
    
    print("Contraseña válida")
    
    # Agregar usuario a la lista
    usuario = {"nombre": nombre, "sexo": sexo, "contrasena": contrasena}
    users.append(usuario)
    return users

def buscar_usuario(users):
    nombre_buscar = input("Ingrese nombre del usuario a buscar: ").strip().lower()
    for usuario in users:
        if usuario["nombre"].lower() == nombre_buscar:
            print("Usuario encontrado:")
            print(f"Nombre: {usuario['nombre']}")
            print(f"Sexo: {usuario['sexo']}")
            print(f"Contraseña: {usuario['contrasena']}")
            return
    print("Usuario no encontrado.")

def eliminar_usuario(users):
    usuario_eliminar = input("Ingrese nombre de usuario a eliminar: ").strip().lower()
    for i, p in enumerate(users):
        if p['nombre'].lower() == usuario_eliminar:
            del users[i]
            print("Usuario eliminado correctamente.\n")
            return
    print("Usuario no encontrado.")

def menu():
    while True:
        print("\n++++ Menú ++++")
        print("1) Ingresar usuario")
        print("2) Buscar usuario")
        print("3) Eliminar usuario")
        print("4) Salir")
        try:
            opcion = int(input("Ingrese opción: "))
        except ValueError:
            print("Opción inválida. Por favor ingrese un número.")
            continue
        
        if opcion == 1:
            lista = registrar_usuario(lista)
        elif opcion == 2:
            buscar_usuario(lista)
        elif opcion == 3:
            eliminar_usuario(lista)
        elif opcion == 4:
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida.")

menu()
