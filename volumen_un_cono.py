#   zona de funciones
def capturar_radio():
    radio = float(input("Digite el radio del cono: "))
    return radio

def capturar_altura():
    altura = float(input("Digite la altura del cono: "))
    return altura

def analizar_datos(radio, altura):
    volumen = (1/3) * 3.1416 * (radio ** 2) * altura
    return volumen

def mostrar_resultados(volumen):
    print("El volumen del cono es:", volumen)


# código principal
radio = capturar_radio()
altura = capturar_altura()
volumen = analizar_datos(radio, altura)
mostrar_resultados(volumen)
