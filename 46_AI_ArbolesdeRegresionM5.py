# ERICK MOISES DELGADILLO LARA
# R: 21310139 - 6E1

# Definición de la función para calcular la entropía
def calcular_entropia(etiquetas):
    from math import log2

    total = len(etiquetas)
    etiqueta_counts = {}
    for etiqueta in etiquetas:
        if etiqueta not in etiqueta_counts:
            etiqueta_counts[etiqueta] = 0
        etiqueta_counts[etiqueta] += 1

    entropia = 0.0
    for etiqueta in etiqueta_counts:
        probabilidad = etiqueta_counts[etiqueta] / total
        entropia -= probabilidad * log2(probabilidad)

    return entropia

# Definición de la función para dividir el conjunto de datos en subconjuntos
def dividir_conjunto(datos, atributo):
    subconjuntos = {}
    for fila in datos:
        valor = fila[atributo]
        if valor not in subconjuntos:
            subconjuntos[valor] = []
        subconjuntos[valor].append(fila)
    return subconjuntos

# Definición de la función para calcular la ganancia de información
def calcular_ganancia(datos, atributo_objetivo, atributos):
    entropia_total = calcular_entropia([fila[atributo_objetivo] for fila in datos])
    ganancia_maxima = 0.0
    mejor_atributo = None

    for atributo in atributos:
        subconjuntos = dividir_conjunto(datos, atributo)
        entropia_atributo = 0.0
        for valor, subconjunto in subconjuntos.items():
            probabilidad = len(subconjunto) / len(datos)
            entropia_atributo += probabilidad * calcular_entropia([fila[atributo_objetivo] for fila in subconjunto])
        ganancia = entropia_total - entropia_atributo
        if ganancia > ganancia_maxima:
            ganancia_maxima = ganancia
            mejor_atributo = atributo

    return mejor_atributo

# Definición de la función para construir el árbol de decisión utilizando el algoritmo ID3
def construir_arbol(datos, atributo_objetivo, atributos):
    etiquetas = [fila[atributo_objetivo] for fila in datos]
    if len(set(etiquetas)) == 1:
        return etiquetas[0]

    if not atributos:
        return max(set(etiquetas), key=etiquetas.count)

    mejor_atributo = calcular_ganancia(datos, atributo_objetivo, atributos)
    subconjuntos = dividir_conjunto(datos, mejor_atributo)

    arbol = {mejor_atributo: {}}
    for valor, subconjunto in subconjuntos.items():
        nuevo_atributos = [atributo for atributo in atributos if atributo != mejor_atributo]
        arbol[mejor_atributo][valor] = construir_arbol(subconjunto, atributo_objetivo, nuevo_atributos)

    return arbol

# Datos de ejemplo: clasificación de frutas basadas en su color y forma
datos = [
    {'color': 'Rojo', 'forma': 'Redonda', 'tipo': 'Manzana'},
    {'color': 'Naranja', 'forma': 'Redonda', 'tipo': 'Naranja'},
    {'color': 'Amarillo', 'forma': 'Alargada', 'tipo': 'Plátano'},
    {'color': 'Amarillo', 'forma': 'Redonda', 'tipo': 'Limon'}
]

# Atributos disponibles para la clasificación
atributos_disponibles = ['color', 'forma']

# Construir el árbol de decisión
arbol_decision = construir_arbol(datos, 'tipo', atributos_disponibles)

# Imprimir el árbol de decisión resultante
print("Árbol de Decisión:")
print(arbol_decision)
