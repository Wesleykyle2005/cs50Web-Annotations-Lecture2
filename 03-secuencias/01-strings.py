# Definir una cadena de caracteres
mi_cadena = "Hola, mundo!"

# Mostrar la cadena completa
print("Cadena completa:", mi_cadena)

# Acceso a caracteres por índice
primer_caracter = mi_cadena[0]  # Acceder al primer carácter
ultimo_caracter = mi_cadena[-1]  # Acceder al último carácter

# Mostrar caracteres accedidos por índice
print("Primer carácter:", primer_caracter)
print("Último carácter:", ultimo_caracter)

# Longitud de la cadena
longitud = len(mi_cadena)

# Mostrar la longitud de la cadena
print("Longitud de la cadena:", longitud)

# Concatenación de cadenas
cadena_concatenada = "Hola" + ", " + "mundo!"

# Mostrar la cadena concatenada
print("Cadena concatenada:", cadena_concatenada)

# Iteración sobre los caracteres de la cadena
print("Caracteres de la cadena:")
for caracter in mi_cadena:
    print(caracter)

# Verificar si una subcadena está presente en la cadena
if "mundo" in mi_cadena:
    print("La subcadena 'mundo' está presente en la cadena")
else:
    print("La subcadena 'mundo' no está presente en la cadena")

# Reemplazar una subcadena por otra en la cadena
cadena_modificada = mi_cadena.replace("mundo", "Python")

# Mostrar la cadena modificada
print("Cadena modificada:", cadena_modificada)

# Dividir la cadena en una lista de subcadenas utilizando un separador
subcadenas = mi_cadena.split(", ")

# Mostrar las subcadenas
print("Subcadenas separadas por ',':", subcadenas)

# Convertir una lista de subcadenas en una cadena utilizando un separador
cadena_desde_lista = ", ".join(subcadenas)

# Mostrar la cadena creada a partir de la lista
print("Cadena creada a partir de la lista:", cadena_desde_lista)

# Convertir la cadena a mayúsculas y minúsculas
cadena_mayusculas = mi_cadena.upper()
cadena_minusculas = mi_cadena.lower()

# Mostrar las cadenas convertidas
print("Cadena en mayúsculas:", cadena_mayusculas)
print("Cadena en minúsculas:", cadena_minusculas)
