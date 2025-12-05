# zona de funciones

def capturar_numero():
    numero = float(input("Digite un número: "))
    return numero

def analizar_datos(numero):
    cuadrado = numero * numero
    return cuadrado

def mostrar_resultados(cuadrado):
    print("El cuadrado es:", cuadrado)


# código principal
numero = capturar_numero()
cuadrado = analizar_datos(numero)
mostrar_resultados(cuadrado)
