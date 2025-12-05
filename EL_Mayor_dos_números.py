#zona de funciones
def capturar_datos_1():
    num1 = float(input("Digite el primer número: "))
    return num1

def capturar_datos_2():
    num2 = float(input("Digite el segundo número: "))
    return num2

def analizar_datos(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2

def mostrar_resultados(mayor):
    print("El número mayor es:", mayor)

#código principal
num1 = capturar_datos_1()
num2 = capturar_datos_2()
mayor = analizar_datos(num1, num2)
mostrar_resultados(mayor)
