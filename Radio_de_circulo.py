# zona de funciones

def capturar_radio():
    radio = float(input("Digite el radio del círculo: "))
    return radio

def analizar_datos(radio):
    area = 3.1416 * (radio ** 2)
    return area

def mostrar_resultados(area):
    print("El área del círculo es:", area)


# código principal
radio = capturar_radio()
area = analizar_datos(radio)
mostrar_resultados(area)
