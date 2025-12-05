# zona de funciones

def capturar_num1():
    n1 = float(input("Digite el primer número: "))
    return n1

def capturar_num2():
    n2 = float(input("Digite el segundo número: "))
    return n2

def analizar_datos(n1, n2):
    producto = n1 * n2
    return producto

def mostrar_resultados(producto):
    print("El producto es:", producto)


# codigo principal
n1 = capturar_num1()
n2= capturar_num2()
producto = analizar_datos(n1, n2)
mostrar_resultados(producto)
