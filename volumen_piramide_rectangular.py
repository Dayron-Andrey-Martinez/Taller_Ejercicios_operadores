# zona de funciones

def capturar_longitud():
    longitud = float(input("Digite la longitud de la base: "))
    return longitud

def capturar_ancho():
    ancho = float(input("Digite el ancho de la base: "))
    return ancho

def capturar_altura():
    altura = float(input("Digite la altura de la pirámide: "))
    return altura

def analizar_datos(longitud, ancho, altura):
    volumen = (longitud * ancho * altura) / 3
    return volumen

def mostrar_resultados(volumen):
    print("El volumen de la pirámide es:", volumen)


# código principal
Longitud = capturar_longitud()
Ancho = capturar_ancho()
altura = capturar_altura()
volumen = analizar_datos(Longitud, Ancho, altura)
mostrar_resultados(volumen)
