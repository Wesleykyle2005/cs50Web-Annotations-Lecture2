# Definir un diccionario
mi_dict = {
"nombre": "Juan",
"edad": 30, 
"ciudad": "Madrid"
  
}

# Mostrar el diccionario completo
print("Diccionario completo:", mi_dict)

# Acceso a elementos del diccionario por clave
nombre = mi_dict["nombre"]  # Acceder al valor asociado a la clave "nombre"
print("Nombre:", nombre)

# Mutabilidad: Actualizar el valor de una clave existente
mi_dict["edad"] = 35  # Actualizar la edad a 35
print("Diccionario actualizado:", mi_dict)

# Agregar un nuevo par clave-valor al diccionario
mi_dict["profesion"] = "Ingeniero"  # Agregar una nueva clave "profesion" con valor "Ingeniero"
print("Diccionario con nueva clave:", mi_dict)

# Eliminar un par clave-valor del diccionario
del mi_dict["ciudad"]  # Eliminar la clave "ciudad" y su valor asociado
print("Diccionario sin clave 'ciudad':", mi_dict)

# Iteración sobre las claves del diccionario
print("Claves del diccionario:")
for clave in mi_dict:
    print(clave)

# Iteración sobre los pares clave-valor del diccionario
print("Pares clave-valor del diccionario:")
for clave, valor in mi_dict.items():
    print(clave, ":", valor)

# Verificar si una clave existe en el diccionario
if "nombre" in mi_dict:
    print("La clave 'nombre' existe en el diccionario")
else:
    print("La clave 'nombre' no existe en el diccionario")

# Conversiones entre diccionarios y listas de tuplas
lista_de_tuplas = [("a", 1), ("b", 2), ("c", 3)]
diccionario_desde_lista = dict(lista_de_tuplas)
print("Diccionario creado a partir de una lista de tuplas:", diccionario_desde_lista)

# Convertir un diccionario en una lista de tuplas (pares clave-valor)
lista_de_tuplas = list(mi_dict.items())
print("Lista de tuplas creada a partir del diccionario:", lista_de_tuplas)
