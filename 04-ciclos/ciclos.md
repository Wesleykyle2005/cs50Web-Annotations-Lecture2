# Ciclos

Los ciclos se utilizan para recorrer listas de elementos o repetir acciones hasta que se cumplan condiciones establecidas.

## For

Los ciclos for se componen por:

```
for i in [lista de elementos]:
    print(i)
``` 
En la variable $i$ se almacena el valor de cada uno de los elementos individuales de la lista temporalmente y se actualiza cada vez que se corre el bucle. 
```
for i in range(3)
    print(i)
```
En el ejemplo anterior se usa range para recorrer una lista de numeros de 0 a 3, aunque tambien se puede usar:
```
for i in range(3,6)
    print(i)
```
En este ejemplo se recorren desde la posicion inicial, hasta la final, pero sin incluirla.  range(a,b) recorre b-1. Tambien hay que tener en cuenta que a < b ya que si son iguales o a es mayor, genera vacio.

## While
El ciclo while se usa para ejecutar un bloque de código mientras la condición establecida se cumpla
Sintaxis:
```
while condicion:
    # Bloque de código a ejecutar mientras la condición sea verdadera
```

```
# Inicializar una variable booleana para controlar el ciclo
continuar = True

# Ejecutar el ciclo while mientras la variable continuar sea verdadera
while continuar:
    respuesta = input("¿Quieres continuar? (s/n): ")
    if respuesta.lower() == "n":
        continuar = False  # Establecer continuar como False para salir del ciclo

print("¡Fin del programa!")

```
