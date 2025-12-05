# zona de funciones

def capturar_num1():
    numero_1 = float(input("Digite el primer número: "))
    return numero_1

def capturar_num2():
    numero_2 = float(input("Digite el segundo número: "))
    return numero_2

def analizar_datos(numero_1, numero_2):
    resta = numero_1 - numero_2
    return resta

def mostrar_resultados(resta):
    print("La resta es:", resta)


# código principal
numero_1= capturar_num1()
numero_2 = capturar_num2()
resta = analizar_datos(numero_1, numero_2)
mostrar_resultados(resta)
