import math

while True:
    # Pedir al usuario que ingrese el radio
    while True:
        try:
            radio = float(input("Ingresa el radio del círculo: "))
            break
        except ValueError:
            print("Ingresa un valor numérico válido")

    # Calcular la circunferencia
    circunferencia = 2 * math.pi * radio

    # Redondear el resultado a 6 decimales
    circunferencia = round(circunferencia, 6)

    # Imprimir el resultado
    print(f"La circunferencia del círculo con radio {radio} es {circunferencia}")

    # Preguntar al usuario si desea calcular otra circunferencia
    while True:
        respuesta = input("¿Deseas calcular otra circunferencia? (s/n): ")
        if respuesta.lower() in ["s", "n"]:
            break
        else:
            print("Ingresa 's' para sí o 'n' para no")

    # Si la respuesta no es "s", salir del bucle
    if respuesta.lower() != "s":
        break
