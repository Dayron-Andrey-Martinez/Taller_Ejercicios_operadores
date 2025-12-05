# zona de funciones

def capturar_num1():
    numero_1 = float(input("Digite el primer número: "))
    return numero_1

def capturar_num2():
    numero_2 = float(input("Digite el segundo número: "))
    return numero_2

def analizar_datos(numero_1, numero_2):
    suma = numero_1 + numero_2
    return suma

def mostrar_resultados(suma):
    print("La suma es:", suma)


# código principal
numero_1= capturar_num1()
numero_2 = capturar_num2()
suma = analizar_datos(numero_1, numero_2)
mostrar_resultados(suma)
