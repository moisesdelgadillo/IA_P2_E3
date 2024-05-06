# ERICK MOISES DELGADILLO LARA
# R: 21310139 - 6E1

# Definir un diccionario para representar las relaciones familiares
relaciones_familiares = {
    'padre': [('Juan', 'Pedro'), ('Pedro', 'Luis'), ('Pedro', 'Ana')],
    'madre': [('María', 'Pedro'), ('María', 'Luis'), ('María', 'Ana')]
}

# Definir una función para verificar si alguien es padre de alguien
def es_padre(padre, hijo):
    return (padre, hijo) in relaciones_familiares['padre']

# Definir una función para verificar si alguien es madre de alguien
def es_madre(madre, hijo):
    return (madre, hijo) in relaciones_familiares['madre']

# Verificar quién es el padre de Luis
for padre, hijo in relaciones_familiares['padre']:
    if hijo == 'Luis':
        print(f"{padre} es el padre de Luis")

# Verificar quién es la madre de Ana
for madre, hija in relaciones_familiares['madre']:
    if hija == 'Ana':
        print(f"{madre} es la madre de Ana")
