#zona de funciones
def capturar_datos_1():
    num = int(input("Digite un número: "))
    return num

def analizar_datos(num):
    if num % 2 == 0:
        return "El número es PAR"
    else:
        return "El número es IMPAR"

def mostrar_resultados(resultado):
    print(resultado)

#cofigo principal
num = capturar_datos_1()
resultado = analizar_datos(num)
mostrar_resultados(resultado)
