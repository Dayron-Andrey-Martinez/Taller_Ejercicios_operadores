# zona de funciones

def capturar_km():
    km = float(input("Digite los kilómetros: "))
    return km

def analizar_datos(km):
    millas = km * 0.621371
    return millas

def mostrar_resultados(millas):
    print("Las millas son:", millas)


# código principal
kilometros = capturar_km()
millas = analizar_datos(kilometros)
mostrar_resultados(millas)
