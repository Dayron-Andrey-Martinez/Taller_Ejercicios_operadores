# zona de funciones
def capturar_datos_1():
    radio = float(input("Digite el radio: "))
    return radio

def analizar_datos(radio):
    circunferencia = 2 * 3.1416 * radio
    return circunferencia

def mostrar_resultados(circunferencia):
    print("La circunferencia es:", circunferencia)

# código principal
radio = capturar_datos_1()
circunferencia = analizar_datos(radio)
mostrar_resultados(circunferencia)
