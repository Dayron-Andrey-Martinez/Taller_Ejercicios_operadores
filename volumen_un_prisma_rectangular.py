# zona de funciones

def capturar_longitud():
    longitud = float(input("Digite la longitud del prisma: "))
    return longitud

def capturar_ancho():
    ancho = float(input("Digite el ancho del prisma: "))
    return ancho

def capturar_altura():
    altura = float(input("Digite la altura del prisma: "))
    return altura

def analizar_datos(longitud, ancho, altura):
    volumen = longitud * ancho * altura
    return volumen

def mostrar_resultados(volumen):
    print("El volumen del prisma rectangular es:", volumen)


# código principal
Longitud = capturar_longitud()
Ancho = capturar_ancho()
altura = capturar_altura()
volumen = analizar_datos(Longitud, Ancho, altura)
mostrar_resultados(volumen)
