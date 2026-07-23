# Función para validar que el usuario ingrese un texto.
def leer_texto(mensaje):
    while True:
        texto = input(mensaje).strip()

        if texto == "":
            print("Error: el dato no puede quedar vacío.")
            continue

        return texto

#validar números enteros iguales o mayores que cero.
def leer_entero_no_negativo(mensaje):
    while True:
        try:
            numero = int(input(mensaje))

            if numero < 0:
                print("Error: el número no puede ser negativo.")
                continue

            return numero

        except ValueError:
            print("Error: debe ingresar un número entero.")


#validar números mayores que cero.
def leer_numero_positivo(mensaje):
    while True:
        try:
            numero = float(input(mensaje).replace(",", "."))

            if numero <= 0:
                print("Error: el número debe ser mayor que cero.")
                continue

            return numero

        except ValueError:
            print("Error: debe ingresar un valor numérico.")

#validar las opciones de un menú.
def leer_opcion(mensaje, opciones_validas):
    while True:
        opcion = input(mensaje).strip()

        if opcion not in opciones_validas:
            print("Error: opción inválida.")
            continue

        return opcion