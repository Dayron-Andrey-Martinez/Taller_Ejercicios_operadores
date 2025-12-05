# zona de funciones

def capturar_pulgadas():
    pulgada = float(input("Digite las pulgadas: "))
    return pulgada

def analizar_datos(pulgada):
    cm = pulgada * 2.54
    return cm

def mostrar_resultados(cm):
    print("Los centímetros son:", cm)


# código principal
pulgada = capturar_pulgadas()
cm = analizar_datos(pulgada)
mostrar_resultados(cm)
