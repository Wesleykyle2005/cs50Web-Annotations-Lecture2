# Función para dividir dos números y manejar excepciones
def dividir_numeros(a, b):
    try:
        resultado = a / b
        print("El resultado de la división es:", resultado)
    except ZeroDivisionError:
        print("¡Error! No se puede dividir entre cero.")

# Ejemplo de uso de la función con if-elif-else
def verificar_division(a, b):
    if b == 0:
        print("¡Error! No se puede dividir entre cero.")
    elif a % b == 0:
        print("La división es exacta.")
    else:
        dividir_numeros(a, b)

# Llamadas a la función
verificar_division(10, 2)  # La división es exacta
verificar_division(10, 3)  # La división no es exacta
verificar_division(10, 0)  # Se produce una excepción ZeroDivisionError
