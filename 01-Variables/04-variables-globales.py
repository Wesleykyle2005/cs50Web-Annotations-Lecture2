x = 10 # variable global
def funcion():
    x = 5 # variable local
    print(x)

funcion() # imprime 5
print(x) # imprime 10




y = 10 # variable global
def funcion():
    global y #llamar a la variable global
    y = 5 # redefinir variable global
    print(y)

funcion() # imprime 5
print(y) # imprime 5




y = 10 # variable global
def funcion(y):
    print(y)

funcion(y) # imprime 10
print(y) # imprime 10


