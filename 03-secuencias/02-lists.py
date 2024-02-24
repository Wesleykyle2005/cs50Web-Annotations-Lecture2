# Crear una lista
lista = [3, 1, 4, 1, 5, 9]

# append(): Agregar un elemento al final de la lista
lista.append(2)

# extend(): Extender la lista agregando elementos de otra lista al final
lista.extend([6, 5, 3])

# insert(): Insertar un elemento en una posición específica
lista.insert(3, 8)

# remove(): Eliminar la primera ocurrencia de un elemento específico
lista.remove(1)

# pop(): Eliminar y devolver el elemento en la posición especificada
elemento_eliminado = lista.pop(2)

# index(): Devolver la posición de la primera ocurrencia de un elemento
posicion = lista.index(5)

# count(): Contar el número de veces que aparece un elemento en la lista
veces = lista.count(5)

# sort(): Ordenar los elementos de la lista en su lugar
lista.sort()

# reverse(): Invertir el orden de los elementos en la lista
lista.reverse()

# clear(): Eliminar todos los elementos de la lista
lista.clear()

# Imprimir la lista resultante y otros valores obtenidos
print("Lista resultante:", lista)
print("Elemento eliminado:", elemento_eliminado)
print("Posición de la primera ocurrencia de '5':", posicion)
print("Número de veces que aparece '5' en la lista:", veces)
