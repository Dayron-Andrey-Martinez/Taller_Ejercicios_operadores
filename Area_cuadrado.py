# zona de funciones

def capturar_lado():
    lado = float(input("Digite el lado del cuadrado: "))
    return lado

def analizar_datos(lado):
    area = lado * lado
    return area

def mostrar_resultados(area):
    print("El área del cuadrado es:", area)


# código principal
lado = capturar_lado()
area = analizar_datos(lado)
mostrar_resultados(area)
