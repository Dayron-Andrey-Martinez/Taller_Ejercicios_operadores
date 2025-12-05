# zona de funciones
def capturar_datos_1():
    num = float(input("Digite un número: "))
    return num

def analizar_datos(num):
    raiz = num ** 0.5
    return raiz

def mostrar_resultados(raiz):
    print("La raíz cuadrada es:", raiz)

# código principal
num = capturar_datos_1()
raiz = analizar_datos(num)
mostrar_resultados(raiz)
