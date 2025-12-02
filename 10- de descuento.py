def capturar_datos_1():
    precio = float(input("Digite el precio del artículo: "))
    return precio

def analizar_datos(precio):
    descuento = precio * 0.10
    return descuento

def mostrar_resultados(descuento):
    print("El descuento del 10% es:", descuento)


precio = capturar_datos_1()
descuento = analizar_datos(precio)
mostrar_resultados(descuento)
