# zona funciones
def capturar_datos_1():
    horas = float(input("Digite las horas: "))
    return horas

def analizar_datos(horas):
    minutos = horas * 60
    return minutos

def mostrar_resultados(minutos):
    print("Equivalen a", minutos, "minutos")

# código principal
horas = capturar_datos_1()
minutos = analizar_datos(horas)
mostrar_resultados(minutos)
