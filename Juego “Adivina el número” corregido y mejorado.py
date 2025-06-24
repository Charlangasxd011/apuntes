from random import randint

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

def juego_adivinar():
    print("Bienvenido al juego 'Adivina el número'")
    
    while True:
        ran1 = pedir_entero("Ingrese un número entero menor o igual a 20 y mayor que 0 (límite inferior): ")
        ran2 = pedir_entero("Ingrese un número entero mayor que el anterior y hasta 20 (límite superior): ")

        if ran1 is None or ran2 is None:
            print("No se pudo iniciar el juego por entradas inválidas.")
            return

        if ran1 <= 0:
            print("El número inferior debe ser mayor que 0.")
            continue
        if ran2 > 20:
            print("El número superior no debe ser mayor que 20.")
            continue
        if ran1 >= ran2:
            print("El número inferior debe ser menor que el número superior.")
            continue
        break

    numero = randint(ran1, ran2)
    intentos_restantes = 3

    while intentos_restantes > 0:
        intento = pedir_entero(f"Adivina el número (te quedan {intentos_restantes} intentos): ")
        if intento is None:
            intentos_restantes -= 1
            continue

        if intento == numero:
            print(f"¡Excelente! Adivinaste el número: {numero}")
            return
        elif intento < numero:
            print("El número es mayor.")
        else:
            print("El número es menor.")
        intentos_restantes -= 1

        if intentos_restantes == 0:
            print(f"Perdiste. El número correcto era {numero}.")
            break
        else:
            print("Aquí hay una pista:")
            dist_intento = abs(numero - intento)
            print(f"Estás a {dist_intento} unidades del número.")

if __name__ == "__main__":
    juego_adivinar()
