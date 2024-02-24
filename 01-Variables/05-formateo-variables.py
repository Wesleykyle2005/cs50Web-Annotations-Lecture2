# Solicitar al usuario que ingrese su nombre como cadena de caracteres
name = input("Name: ")

# Solicitar al usuario que ingrese su edad como cadena de caracteres y convertir a entero
age_str = input("Age: ")
age_int = int(age_str)

# Solicitar al usuario que ingrese su peso como cadena de caracteres y convertir a flotante
weight_str = input("Weight (kg): ")
weight_float = float(weight_str)


print(f"Hola, {name}. su edad es: {age_str} + su peso es {weight_float}")