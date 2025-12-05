# zona de funciones

def capturar_litros():
    litros = float(input("Digite los litros: "))
    return litros

def analizar_datos(litros):
    galones = litros * 0.264172
    return galones

def mostrar_resultados(galones):
    print("Los galones son:", galones)


# codigo principal
litros = capturar_litros()
galones = analizar_datos(litros)
mostrar_resultados(galones)
