# zona de funciones
def capturar_datos_1():
    base = float(input("Digite la base del triángulo: "))
    return base

def capturar_datos_2():
    altura = float(input("Digite la altura del triángulo: "))
    return altura

def analizar_datos(base, altura):
    area = (base * altura) / 2
    return area

def mostrar_resultados(area):
    print("El área del triángulo es:", area)

# código principal
base = capturar_datos_1()
altura = capturar_datos_2()
area = analizar_datos(base, altura)
mostrar_resultados(area)
