def pedir_float(mensaje, minimo=None, maximo=None):
    while True:
        try:
            valor = float(input(mensaje))
            if minimo is not None and valor < minimo:
                print(f"Debe ser mayor o igual a {minimo}")
                continue
            if maximo is not None and valor > maximo:
                print(f"Debe ser menor o igual a {maximo}")
                continue
            return valor
        except ValueError:
            print("Error: Ingrese un número válido.")

def pedir_int(mensaje, minimo=None, maximo=None):
    while True:
        try:
            valor = int(input(mensaje))
            if minimo is not None and valor < minimo:
                print(f"Debe ser mayor o igual a {minimo}")
                continue
            if maximo is not None and valor > maximo:
                print(f"Debe ser menor o igual a {maximo}")
                continue
            return valor
        except ValueError:
            print("Error: Ingrese un número entero válido.")

def calcular_descuentos():
    arancel = 1_800_000
    matricula = 90_000

    promedio = pedir_float("Ingrese su promedio final: ", 1.0, 7.0)
    quintil = pedir_int("Ingrese el quintil (1 a 5): ", 1, 5)

    descuento_arancel = 0
    descuento_matricula = 0

    # Descuento en arancel
    if promedio > 6.0:
        if quintil in [1, 2]:
            descuento_arancel = 0.20
            print("Descuento en arancel: 20%")
        elif quintil in [3, 4]:
            descuento_arancel = 0.15
            print("Descuento en arancel: 15%")
    elif 5.0 < promedio <= 6.0:
        if quintil in [1, 2]:
            descuento_arancel = 0.10
            print("Descuento en arancel: 10%")

    arancel_final = arancel * (1 - descuento_arancel)

    # Descuento en matrícula
    if quintil in [1, 2, 3]:
        descuento_matricula = 0.10
        print("Descuento en matrícula: 10%")
    if promedio >= 5.5:
        descuento_matricula += 0.05
        print("Descuento adicional por promedio >= 5.5: 5%")

    if descuento_matricula > 1.0:
        descuento_matricula = 1.0  # Máximo 100%

    matricula_final = matricula * (1 - descuento_matricula)

    print(f"\nArancel final: ${arancel_final:,.0f}")
    print(f"Matrícula final: ${matricula_final:,.0f}")

calcular_descuentos()
