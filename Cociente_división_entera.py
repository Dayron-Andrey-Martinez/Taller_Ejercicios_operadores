# zona de funciones
def capturar_datos_1():
    num1 = int(input("Digite el primer número: "))
    return num1

def capturar_datos_2():
    num2 = int(input("Digite el segundo número: "))
    return num2

def analizar_datos(num1, num2):
    cociente = num1 // num2
    return cociente

def mostrar_resultados(cociente):
    print("El cociente entero es:", cociente)

# código principal
num1 = capturar_datos_1()
num2 = capturar_datos_2()
cociente = analizar_datos(num1, num2)
mostrar_resultados(cociente)
