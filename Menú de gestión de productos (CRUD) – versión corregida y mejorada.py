import os

lista = []
codigo = 1

def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")

def registrar_producto():
    global codigo
    try:
        descripcion = input("Ingrese descripción: ").strip()
        precio = float(input("Ingrese precio: "))
        cantidad = int(input("Ingrese cantidad: "))

        producto = {
            "codigo": codigo,
            "descripcion": descripcion,
            "precio": precio,
            "cantidad": cantidad
        }

        lista.append(producto)
        print("Producto registrado con éxito.")
        codigo += 1
    except ValueError:
        print("Error: ingrese valores numéricos válidos para precio y cantidad.")

def buscar_producto():
    try:
        buscado = int(input("¿Qué código quieres buscar?: "))
        for prod in lista:
            if prod["codigo"] == buscado:
                print(f"Producto encontrado: {prod}")
                return
        print("Producto no encontrado.")
    except ValueError:
        print("Error: debe ingresar un número de código válido.")

def imprimir_productos():
    if not lista:
        print("No hay productos registrados.")
    else:
        print("Lista de productos:")
        for prod in lista:
            print(f"Código: {prod['codigo']}, Descripción: {prod['descripcion']}, Precio: ${prod['precio']}, Cantidad: {prod['cantidad']}")

def editar_producto():
    try:
        codigo_editar = int(input("Ingrese el código del producto a editar: "))
        for prod in lista:
            if prod["codigo"] == codigo_editar:
                print(f"Producto actual: {prod}")
                print("¿Qué deseas editar?")
                print("1) Descripción")
                print("2) Precio")
                print("3) Cantidad")
                editar_opcion = input("Seleccione opción: ")

                if editar_opcion == "1":
                    prod["descripcion"] = input("Nueva descripción: ").strip()
                elif editar_opcion == "2":
                    prod["precio"] = float(input("Nuevo precio: "))
                elif editar_opcion == "3":
                    prod["cantidad"] = int(input("Nueva cantidad: "))
                else:
                    print("Opción inválida.")
                    return
                print("Producto actualizado.")
                return
        print("Producto no encontrado.")
    except ValueError:
        print("Error: Ingrese valores válidos.")

def menu():
    while True:
        print("++++ Menú ++++")
        print("1) Registrar producto")
        print("2) Buscar producto por código")
        print("3) Imprimir productos")
        print("4) Editar producto")
        print("5) Salir")
        opcion = input("Ingrese una opción: ").strip()

        limpiar_pantalla()

        if opcion == "1":
            registrar_producto()
        elif opcion == "2":
            buscar_producto()
        elif opcion == "3":
            imprimir_productos()
        elif opcion == "4":
            editar_producto()
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida.")

menu()
