# ERICK MOISES DELGADILLO LARA
# R: 21310139 - 6E1

import random

# Ejemplo de datos de entrenamiento
datos_entrenamiento = [
    ([2, 3, 1], 'A'),
    ([3, 1, 0], 'B'),
    ([5, 4, 1], 'A'),
    ([7, 2, 0], 'B'),
    ([10, 1, 0], 'B'),
    ([11, 4, 1], 'A'),
    ([13, 6, 1], 'A'),
    ([15, 3, 0], 'B'),
    ([16, 5, 1], 'A'),
    ([18, 2, 0], 'B')
]

# Clase para el modelo de K-DL
class KDLModelo:
    def __init__(self, k):
        self.k = k
        self.datos_entrenamiento = []

    def entrenar(self, datos_entrenamiento):
        self.datos_entrenamiento = datos_entrenamiento

    def predecir(self, entrada):
        # Calcular la distancia euclidiana entre la entrada y todos los puntos de entrenamiento
        distancias = [(self.distancia_euclidiana(entrada, x), y) for x, y in self.datos_entrenamiento]
        # Ordenar las distancias de menor a mayor
        distancias.sort(key=lambda x: x[0])
        # Tomar los primeros k vecinos más cercanos
        k_vecinos = distancias[:self.k]
        # Contar las etiquetas de los k vecinos
        conteo_etiquetas = {}
        for distancia, etiqueta in k_vecinos:
            conteo_etiquetas[etiqueta] = conteo_etiquetas.get(etiqueta, 0) + 1
        # Devolver la etiqueta con más ocurrencias
        return max(conteo_etiquetas, key=conteo_etiquetas.get)

    def distancia_euclidiana(self, punto1, punto2):
        return sum((x - y) ** 2 for x, y in zip(punto1, punto2)) ** 0.5

# Entrenamiento y predicción
modelo_kdl = KDLModelo(k=3)
modelo_kdl.entrenar(datos_entrenamiento)
nueva_entrada = [14, 3, 1]
prediccion = modelo_kdl.predecir(nueva_entrada)
print("Predicción para la entrada", nueva_entrada, ":", prediccion)
