# zona de funciones

def capturar_dolares():
    dolares = float(input("Digite la cantidad de dólares: "))
    return dolares

def capturar_tasa():
    tasa = 0.86
    return tasa

def analizar_datos(dolares, tasa):
    euros = dolares * tasa
    return euros

def mostrar_resultados(euros):
    print("La cantidad en euros es:", euros)


# código principal
dolares = capturar_dolares()
tasa = capturar_tasa()
euros = analizar_datos(dolares, tasa)
mostrar_resultados(euros)
