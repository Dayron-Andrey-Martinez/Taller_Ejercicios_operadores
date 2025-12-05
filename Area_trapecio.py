# zona de funciones
def capturar_base_mayor():
    Base_mayor = float(input("Digite la base mayor del trapecio: "))
    return Base_mayor

def capturar_base_menor():
    base_menor = float(input("Digite la base menor del trapecio: "))
    return base_menor

def capturar_altura():
    altura = float(input("Digite la altura del trapecio: "))
    return altura

def analizar_datos(Base_mayor, basa_menor, altura):
    area = ((Base_mayor + basa_menor) * altura) / 2
    return area

def mostrar_resultados(area):
    print("El área del trapecio es:", area)


# código principal
Base_mayor = capturar_base_mayor()
base_menor = capturar_base_menor()
altura = capturar_altura()
area = analizar_datos(Base_mayor, base_menor, altura)
mostrar_resultados(area)
