# ERICK MOISES DELGADILLO LARA
# R: 21310139 - 6E1

from collections import defaultdict

# Ejemplos de secuencias de palabras
ejemplos = [
    "el gato caza al ratón",
    "el perro ladra al gato",
    "el ratón corre rápido"
]

# Definir una gramática simple
gramatica = defaultdict(list)

# Procesar los ejemplos y aprender la gramática
for ejemplo in ejemplos:
    palabras = ejemplo.split()
    for i in range(len(palabras) - 1):
        gramatica[palabras[i]].append(palabras[i+1])

# Imprimir la gramática aprendida
for palabra, siguientes in gramatica.items():
    print(f"{palabra} -> {' '.join(siguientes)}")
