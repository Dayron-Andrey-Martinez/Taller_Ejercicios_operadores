# zona de funciones
def capturar_datos_1():
    num1 = float(input("Digite el primer número: "))
    return num1

def capturar_datos_2():
    num2 = float(input("Digite el segundo número: "))
    return num2

def analizar_datos(n1, n2):
    residuo = n1 % n2
    return residuo

def mostrar_resultados(residuo):
    print("El residuo es:", residuo)

# código principal
num1 = capturar_datos_1()
num2 = capturar_datos_2()
residuo = analizar_datos(num1, num2)
mostrar_resultados(residuo)
