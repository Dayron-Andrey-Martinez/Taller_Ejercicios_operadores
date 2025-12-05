# zona de funciones

def capturar_celsius():
    celsius = float(input("Digite los grados Celsius: "))
    return celsius

def analizar_datos(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def mostrar_resultados(fahrenheit):
    print("Los grados Fahrenheit son:", fahrenheit)


# código principal
celsius = capturar_celsius()
fahrenheit = analizar_datos(celsius)
mostrar_resultados(fahrenheit)
