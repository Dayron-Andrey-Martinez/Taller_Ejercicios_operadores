# zona de funciones

def capturar_radio():
    radio = float(input("Digite el radio de la esfera: "))
    return radio

def analizar_datos(radio):
    volumen = (4/3) * 3.1416 * (radio ** 3)
    return volumen

def mostrar_resultados(volumen):
    print("El volumen de la esfera es:", volumen)


# código principal
radio = capturar_radio()
volumen = analizar_datos(radio)
mostrar_resultados(volumen)
