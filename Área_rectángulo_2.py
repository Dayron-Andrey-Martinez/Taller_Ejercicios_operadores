# zona de funciones
def capturar_datos_1():
    largo = float(input("Digite la longitud: "))
    return largo

def capturar_datos_2():
    ancho = float(input("Digite el ancho: "))
    return ancho

def analizar_datos(l, a):
    area = l * a
    return area

def mostrar_resultados(area):
    print("El área del rectángulo es:", area)

# código principal
largo = capturar_datos_1()
ancho = capturar_datos_2()
resultado = analizar_datos(largo, ancho)
mostrar_resultados(resultado)
