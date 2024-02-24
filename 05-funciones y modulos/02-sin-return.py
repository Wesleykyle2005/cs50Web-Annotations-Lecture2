variable_global = 10

def modificar_variable_global():
    global variable_global
    variable_global = 20

# Ejemplo de uso
print("Valor antes de la modificación:", variable_global)
modificar_variable_global()
print("Valor después de la modificación:", variable_global)