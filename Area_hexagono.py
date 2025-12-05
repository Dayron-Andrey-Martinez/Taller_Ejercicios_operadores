# zona de funciones
def capturar_lado():
    lado = float(input("Digite el lado del hexágono: "))
    return lado

def analizar_datos(lado):
    area = (3 * 1.73205 * (lado ** 2)) / 2
    return area

def mostrar_resultados(area):
    print("El área del hexágono es:", area)


# código principal
lado = capturar_lado()
area = analizar_datos(lado)
mostrar_resultados(area)
