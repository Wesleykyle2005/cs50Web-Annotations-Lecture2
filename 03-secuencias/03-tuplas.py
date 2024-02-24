# Definir una tupla
mi_tupla = (1, 2, 3, "a", "b", "c")

# Acceso a elementos de la tupla por índice
primer_elemento = mi_tupla[0]  # Devuelve 1
ultimo_elemento = mi_tupla[-1]  # Devuelve "c"

# Mostrar la tupla y los elementos accedidos
print("Tupla completa:", mi_tupla)
print("Primer elemento:", primer_elemento)
print("Último elemento:", ultimo_elemento)

# Longitud de la tupla
longitud = len(mi_tupla)  # Devuelve 6

# Iteración sobre los elementos de la tupla
print("Elementos de la tupla:")
for elemento in mi_tupla:
    print(elemento)

# Crear una tupla
tupla_empaquetada = (1, 2, 3)

# Desempaquetar una tupla
a, b, c = tupla_empaquetada

# Mostrar la tupla empaquetada y los valores desempaquetados
print("Tupla empaquetada:", tupla_empaquetada)
print("Desempaquetado: a =", a, ", b =", b, ", c =", c)
