# zona de funciones

def capturar_base():
    base = float(input("Digite la base del triángulo: "))
    return base

def capturar_altura():
    altura = float(input("Digite la altura del triángulo: "))
    return altura

def analizar_datos(base, altura):
    area = (base * altura) / 2
    return area

def mostrar_resultados(area):
    print("El área del triángulo es:", area)

# código principal
base = capturar_base()
altura = capturar_altura()
area = analizar_datos(base, altura)
mostrar_resultados(area)
