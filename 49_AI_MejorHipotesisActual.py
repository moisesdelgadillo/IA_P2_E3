# ERICK MOISES DELGADILLO LARA
# R: 21310139 - 6E1

# Definimos una función para calcular la mejor hipótesis actual
def mejor_hipotesis(datos_entrenamiento, atributos_clase):
    # Inicializamos la mejor hipótesis como None
    mejor_hipotesis = None
    # Iteramos sobre cada instancia en los datos de entrenamiento
    for instancia in datos_entrenamiento:
        # Si es la primera instancia, la tomamos como la mejor hipótesis
        if mejor_hipotesis is None:
            mejor_hipotesis = instancia
        else:
            # Comparamos cada atributo de clase y actualizamos la mejor hipótesis si es necesario
            for i in range(len(atributos_clase)):
                if instancia[i] != mejor_hipotesis[i]:
                    mejor_hipotesis[i] = '?'
    # Devolvemos la mejor hipótesis encontrada
    return mejor_hipotesis

# Ejemplo de datos de entrenamiento
datos_entrenamiento = [
    ['soleado', 'caliente', 'alta', 'debil', 'no'],
    ['soleado', 'caliente', 'alta', 'fuerte', 'no'],
    ['nublado', 'caliente', 'alta', 'debil', 'si'],
    ['lluvioso', 'templado', 'alta', 'debil', 'si'],
    ['lluvioso', 'frio', 'normal', 'debil', 'si'],
    ['lluvioso', 'frio', 'normal', 'fuerte', 'no'],
    ['nublado', 'frio', 'normal', 'fuerte', 'si'],
    ['soleado', 'templado', 'alta', 'debil', 'no'],
    ['soleado', 'frio', 'normal', 'debil', 'si'],
    ['lluvioso', 'templado', 'normal', 'debil', 'si'],
    ['soleado', 'templado', 'normal', 'fuerte', 'si'],
    ['nublado', 'templado', 'alta', 'fuerte', 'si'],
    ['nublado', 'caliente', 'normal', 'debil', 'si'],
    ['lluvioso', 'templado', 'alta', 'fuerte', 'no']
]

# Lista de atributos de clase
atributos_clase = ['?', '?', '?', '?']

# Calculamos la mejor hipótesis actual
mejor_hipotesis_actual = mejor_hipotesis(datos_entrenamiento, atributos_clase)

# Imprimimos la mejor hipótesis actual
print("Mejor Hipótesis Actual:", mejor_hipotesis_actual)
