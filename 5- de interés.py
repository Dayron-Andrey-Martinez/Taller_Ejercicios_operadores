def capturar_datos_1():
    dinero = float(input("Digite la cantidad de dinero: "))
    return dinero

def analizar_datos(dinero):
    interes = dinero * 0.05
    return interes

def mostrar_resultados(interes):
    print("El interés del 5% es:", interes)


dinero = capturar_datos_1()
interes = analizar_datos(dinero)
mostrar_resultados(interes)
