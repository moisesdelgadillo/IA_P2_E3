# ERICK MOISES DELGADILLO LARA
# R: 21310139 - 6E1


# Definir la función que representa la propiedad "y es el doble de x"
def es_doble_de(x, y):
    return y == 2 * x

# Definir una función para verificar la propiedad "para todo x, existe y tal que y es el doble de x"
def para_todo_existe_un(y):
    return any(es_doble_de(x, y) for x in range(-100, 101))

# Verificar si la propiedad se cumple para algún valor de y en el rango [-100, 100]
if any(para_todo_existe_un(y) for y in range(-200, 201)):
    print("La propiedad 'para todo x, existe y tal que y es el doble de x' se cumple.")
else:
    print("La propiedad 'para todo x, existe y tal que y es el doble de x' no se cumple.")
