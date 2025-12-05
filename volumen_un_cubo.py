# zona de funciones

def capturar_lado():
    lado = float(input("Digite el lado del cubo: "))
    return lado

def analizar_datos(lado):
    volumen = lado ** 3
    return volumen

def mostrar_resultados(volumen):
    print("El volumen del cubo es:", volumen)


# código principal
lado = capturar_lado()
volumen = analizar_datos(lado)
mostrar_resultados(volumen)
