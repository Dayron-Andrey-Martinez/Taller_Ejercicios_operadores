# zona de funciones

def capturar_longitud():
    longitud = float(input("Digite la longitud del rectángulo: "))
    return longitud

def capturar_ancho():
    ancho = float(input("Digite el ancho del rectángulo: "))
    return ancho

def analizar_datos(longitud, ancho):
    area = longitud * ancho
    return area

def mostrar_resultados(area):
    print("El área del rectángulo es:", area)


# código principal
Longitud= capturar_longitud()
Ancho = capturar_ancho()
area = analizar_datos(Longitud, Ancho)
mostrar_resultados(area)
3