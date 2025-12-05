# zona de funciones

def capturar_base():
    base = float(input("Digite la base del triángulo: "))
    return base

def capturar_altura():
    altura = float(input("Digite la altura del triángulo: "))
    return altura

def capturar_ancho():
    ancho = float(input("Digite el ancho del prisma: "))
    return ancho

def analizar_datos(base, altura, ancho):
    volumen = ((base * altura) / 2) * ancho
    return volumen

def mostrar_resultados(volumen):
    print("El volumen del prisma triangular es:", volumen)


# código principal
base = capturar_base()
altura= capturar_altura()
ancho = capturar_ancho()
volumen = analizar_datos(base, altura, ancho)
mostrar_resultados(volumen)
