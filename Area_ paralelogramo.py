# zona de funciones
def capturar_base():
    base = float(input("Digite la base: "))
    return base

def capturar_altura():
    altura = float(input("Digite la altura: "))
    return altura

def analizar_datos(base, altura):
    area = base * altura
    return area

def mostrar_resultados(area):
    print("El área del paralelogramo es:", area)


# código principal                              
base = capturar_base()
altura= capturar_altura()
area = analizar_datos(base, altura)
mostrar_resultados(area)
