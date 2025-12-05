# zona de funciones

def capturar_radio():
    radio = float(input("Digite el radio del cilindro: "))
    return radio

def capturar_altura():
    altura = float(input("Digite la altura del cilindro: "))
    return altura

def analizar_datos(radio, altura):
    volumen = 3.1416 * (radio ** 2) * altura
    return volumen

def mostrar_resultados(volumen):
    print("El volumen del cilindro es:", volumen)


# código principal
radio = capturar_radio()
altura = capturar_altura()
volumen= analizar_datos(radio, altura)
mostrar_resultados(volumen)
