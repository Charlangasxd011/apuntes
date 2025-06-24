def pedir_numero_positivo(mensaje, intentos=3):
    while intentos > 0:
        try:
            num = float(input(mensaje))
            if num <= 0:
                intentos -= 1
                print(f"No se permiten valores menores o iguales a 0. Intentos restantes: {intentos}")
            else:
                return num
        except ValueError:
            intentos -= 1
            print(f"Error: debe ingresar un número válido. Intentos restantes: {intentos}")
    print("Ha superado el límite de intentos.")
    return None

def validar_texto(mensaje, max_caracteres=7, intentos=3):
    while intentos > 0:
        texto = input(mensaje)
        if len(texto) <= max_caracteres:
            return texto
        else:
            intentos -= 1
            print(f"El texto no debe superar los {max_caracteres} caracteres. Intentos restantes: {intentos}")
    print("Ha superado el límite de intentos.")
    return None

def es_entero(mensaje, intentos=3):
    while intentos > 0:
        valor = input(mensaje)
        try:
            num = float(valor)
            if num.is_integer():
                return True
            else:
                return False
        except ValueError:
            intentos -= 1
            print(f"Error: debe ingresar un número válido. Intentos restantes: {intentos}")
    print("Ha superado el límite de intentos.")
    return None

def solo_decimal(mensaje, intentos=3):
    while intentos > 0:
        valor = input(mensaje)
        try:
            num = float(valor)
            if not num.is_integer():
                return num
            else:
                intentos -= 1
                print(f"Debe ingresar un número con notación decimal (con parte decimal). Intentos restantes: {intentos}")
        except ValueError:
            intentos -= 1
            print(f"Error: debe ingresar un número válido. Intentos restantes: {intentos}")
    print("Ha superado el límite de intentos.")
    return None

def menu():
    while True:
        print("1) División (2 números)")
        print("2) Validar texto (máx 7 caracteres)")
        print("3) Verificar si un número es entero")
        print("4) Sólo permitir números con notación decimal")
        print("5) Salir")
        
        try:
            opcion = int(input("Ingrese una opción: "))
        except ValueError:
            print("Error: debe ingresar un número válido.")
            continue

        if opcion == 1:
            print("Ingrese dos números positivos para la división:")
            n1 = pedir_numero_positivo("Primer número: ")
            if n1 is None:
                break
            n2 = pedir_numero_positivo("Segundo número: ")
            if n2 is None:
                break
            
            resultado = n1 / n2
            print(f"Resultado de la división: {resultado}")

        elif opcion == 2:
            texto = validar_texto("Ingrese texto (máx 7 caracteres): ")
            if texto is None:
                break
            print(f"Texto válido: {texto}")

        elif opcion == 3:
            res = es_entero("Ingrese un número para verificar si es entero: ")
            if res is None:
                break
            print("Es un número entero." if res else "No es un número entero.")

        elif opcion == 4:
            num_decimal = solo_decimal("Ingrese un número con notación decimal: ")
            if num_decimal is None:
                break
            print(f"Número decimal válido: {num_decimal}")

        elif opcion == 5:
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida. Intente de nuevo.")

menu()
