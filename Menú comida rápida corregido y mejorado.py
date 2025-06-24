def pedir_entero(mensaje, intentos=3):
    while intentos > 0:
        try:
            valor = int(input(mensaje))
            return valor
        except ValueError:
            intentos -= 1
            print(f"Error: debe ingresar un número entero válido. Intentos restantes: {intentos}")
    print("Ha superado el límite de intentos.")
    return None

def menu_hamburguesas():
    precios = {"chedar": 8, "tocino": 12}
    total = 0
    while True:
        print("*** Hamburguesas ***")
        print("1) Chedar - $8")
        print("2) Tocino - $12")
        print("3) Volver al menú principal")
        opcion = pedir_entero("Seleccione una hamburguesa (1-3): ")
        if opcion is None or opcion == 3:
            break
        if opcion == 1 or opcion == 2:
            tipo = "chedar" if opcion == 1 else "tocino"
            cantidad = pedir_entero(f"¿Cuántas hamburguesas {tipo} llevará?: ")
            if cantidad is None:
                continue
            subtotal = precios[tipo] * cantidad
            print(f"{tipo.capitalize()}: {cantidad} x ${precios[tipo]} = ${subtotal}")
            total += subtotal
        else:
            print("Opción inválida. Intente de nuevo.")
    return total

def menu_pizzas():
    precios = {"napolitana": 20, "peperoni": 15}
    total = 0
    while True:
        print("*** Pizzas ***")
        print("1) Napolitana - $20")
        print("2) Peperoni - $15")
        print("3) Volver al menú principal")
        opcion = pedir_entero("Seleccione una pizza (1-3): ")
        if opcion is None or opcion == 3:
            break
        if opcion == 1 or opcion == 2:
            tipo = "napolitana" if opcion == 1 else "peperoni"
            cantidad = pedir_entero(f"¿Cuántas pizzas {tipo} llevará?: ")
            if cantidad is None:
                continue
            subtotal = precios[tipo] * cantidad
            print(f"{tipo.capitalize()}: {cantidad} x ${precios[tipo]} = ${subtotal}")
            total += subtotal
        else:
            print("Opción inválida. Intente de nuevo.")
    return total

def menu_bebidas():
    precios = {"cocacola": 2, "pepsi": 1}
    total = 0
    while True:
        print("*** Bebidas ***")
        print("1) Cocacola - $2")
        print("2) Pepsi - $1")
        print("3) Volver al menú principal")
        opcion = pedir_entero("Seleccione una bebida (1-3): ")
        if opcion is None or opcion == 3:
            break
        if opcion == 1 or opcion == 2:
            tipo = "cocacola" if opcion == 1 else "pepsi"
            cantidad = pedir_entero(f"¿Cuántas bebidas {tipo} llevará?: ")
            if cantidad is None:
                continue
            subtotal = precios[tipo] * cantidad
            print(f"{tipo.capitalize()}: {cantidad} x ${precios[tipo]} = ${subtotal}")
            total += subtotal
        else:
            print("Opción inválida. Intente de nuevo.")
    return total

def menu_principal():
    total_general = 0
    while True:
        print("**** Menú Principal - Comida Rápida ****")
        print("1) Hamburguesas")
        print("2) Pizzas")
        print("3) Bebidas")
        print("4) Salir y mostrar total")
        opcion = pedir_entero("Seleccione una opción (1-4): ")
        if opcion is None:
            continue
        if opcion == 1:
            total_general += menu_hamburguesas()
        elif opcion == 2:
            total_general += menu_pizzas()
        elif opcion == 3:
            total_general += menu_bebidas()
        elif opcion == 4:
            print(f"Total a pagar: ${total_general}")
            print("Gracias por su compra.")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

menu_principal()
