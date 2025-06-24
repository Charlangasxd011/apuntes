lista = []
contador = 0

def agregar_producto():
    global contador
    contador += 1
    producto = input("¿Qué producto desea llevar?: ").strip()
    
    while True:
        try:
            precio = float(input("Precio del producto: "))
            if precio < 0:
                print("El precio no puede ser negativo.")
                continue
            break
        except ValueError:
            print("Ingrese un número válido para el precio.")

    while True:
        try:
            cantidad = int(input("Ingrese cantidad: "))
            if cantidad < 0:
                print("La cantidad no puede ser negativa.")
                continue
            break
        except ValueError:
            print("Ingrese un número entero válido para la cantidad.")

    dicc = {
        "codigo": contador,
        "descripcion": producto,
        "precio": precio,
        "cantidad": cantidad
    }
    lista.append(dicc)
    print("Producto agregado con éxito.\n")

def buscar_producto():
    while True:
        try:
            cod_busqueda = int(input("Ingrese el código del producto a buscar: "))
            break
        except ValueError:
            print("Ingrese un número entero válido.")

    encontrado = False
    for prod in lista:
        if prod["codigo"] == cod_busqueda:
            print("Producto encontrado:")
            for k, v in prod.items():
                print(f"{k.capitalize()}: {v}")
            print()
            encontrado = True
            break
    if not encontrado:
        print("Producto no encontrado.\n")

def imprimir_productos():
    if not lista:
        print("No hay productos registrados.\n")
        return
    print("Listado de productos:")
    for prod in lista:
        print(f"Código: {prod['codigo']}")
        print(f"Descripción: {prod['descripcion']}")
        print(f"Precio: {prod['precio']}")
        print(f"Cantidad: {prod['cantidad']}")
        print("-" * 20)
    print()

def menu():
    while True:
        print("*** Menú de productos ***")
        print("1) Agregar producto")
        print("2) Buscar producto por código")
        print("3) Imprimir todos los productos")
        print("4) Salir")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            buscar_producto()
        elif opcion == "3":
            imprimir_productos()
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente de nuevo.\n")

menu()
