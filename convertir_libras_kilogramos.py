#zona de funciones

def capturar_libras():
    libra = float(input("Digite las libras: "))
    return libra

def analizar_datos(libra):
    kg = libra * 0.453592
    return kg

def mostrar_resultados(kg):
    print("Los kilogramos son:", kg)


# codigo principal
libra = capturar_libras()
kg = analizar_datos(libra)
mostrar_resultados(kg)
