# zona de funciones
def capturar_datos_1():
    num1 = int(input("Digite el primer número: "))
    return num1

def capturar_datos_2():
    num2 = int(input("Digite el segundo número: "))
    return num2

def analizar_datos(num1, num2):
    if num1 % num2 == 0:
        return "Es múltiplo"
    else:
        return "No es múltiplo"

def mostrar_resultados(resultado):
    print(resultado)

# código principal
num1 = capturar_datos_1()
num2 = capturar_datos_2()
res = analizar_datos(num1, num2)
mostrar_resultados(res)
