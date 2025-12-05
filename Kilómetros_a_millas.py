# zona funciones
def capturar_datos_1():
    km = float(input("Digite los kilómetros: "))
    return km

def analizar_datos(km):
    millas = km * 0.621371
    return millas

def mostrar_resultados(millas):
    print("Equivalen a", millas, "millas")

# código principal
km = capturar_datos_1()
millas = analizar_datos(km)
mostrar_resultados(millas)
