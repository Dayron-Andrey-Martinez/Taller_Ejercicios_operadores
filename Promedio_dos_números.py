# zona de funciones
def capturar_datos_1():
    num1 = float(input("Digite el primer número: "))
    return num1

def capturar_datos_2():
    num2 = float(input("Digite el segundo número: "))
    return num2

def analizar_datos(num1, num2):
    promedio = (num1 + num2) / 2
    return promedio

def mostrar_resultados(prom):
    print("El promedio es:", prom)

# código principal
num1 = capturar_datos_1()
num2 = capturar_datos_2()
prom = analizar_datos(num1, num2)
mostrar_resultados(prom)
