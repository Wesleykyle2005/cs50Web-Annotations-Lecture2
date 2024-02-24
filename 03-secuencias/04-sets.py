# Definir un conjunto
mi_set = {1, 2, 3, 4, 5}

# Mostrar el conjunto
print("Conjunto completo:", mi_set)

# Agregar un elemento al conjunto (mutabilidad)
mi_set.add(6)

# Eliminar un elemento del conjunto
mi_set.remove(3)

# Mostrar el conjunto actualizado
print("Conjunto después de agregar y eliminar elementos:", mi_set)

# Operaciones de conjuntos
set1 = {1, 2, 3}
set2 = {3, 4, 5}

union = set1 | set2  # Unión de conjuntos
interseccion = set1 & set2  # Intersección de conjuntos
diferencia = set1 - set2  # Diferencia de conjuntos
diferencia_simetrica = set1 ^ set2  # Diferencia simétrica de conjuntos

# Mostrar los resultados de las operaciones de conjuntos
print("Unión de conjuntos:", union)
print("Intersección de conjuntos:", interseccion)
print("Diferencia de conjuntos:", diferencia)
print("Diferencia simétrica de conjuntos:", diferencia_simetrica)

# Iteración sobre un conjunto
print("Elementos del conjunto:")
for elemento in mi_set:
    print(elemento)

# Conversiones entre conjuntos y listas
lista = [1, 2, 3, 3, 4, 5]
conjunto = set(lista)  # Convertir lista a conjunto
lista_nueva = list(conjunto)  # Convertir conjunto a lista

# Mostrar las conversiones
print("Lista original:", lista)
print("Conjunto creado a partir de la lista:", conjunto)
print("Lista creada a partir del conjunto:", lista_nueva)
