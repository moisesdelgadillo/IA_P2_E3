# ERICK MOISES DELGADILLO LARA
# R: 21310139 - 6E1

import random

# Datos de entrenamiento (ejemplo simple)
datos_entrenamiento = [
    (2, 3, 1),
    (3, 1, 0),
    (5, 4, 1),
    (7, 2, 0),
    (10, 1, 0),
    (11, 4, 1),
    (13, 6, 1),
    (15, 3, 0),
    (16, 5, 1),
    (18, 2, 0)
]

# Clase del modelo de Boosting
class BoostingModelo:
    def __init__(self):
        self.modelos = []

    def entrenar(self, datos, num_modelos=3):
        for i in range(num_modelos):
            modelo = self.entrenar_modelo(datos)
            self.modelos.append(modelo)

    def predecir(self, entrada):
        # Suma de las predicciones de los modelos individuales
        suma_predicciones = sum(modelo.predict(entrada) for modelo in self.modelos)
        # Si la suma es mayor o igual a la mitad de los modelos, predicción positiva (1), de lo contrario negativa (0)
        return 1 if suma_predicciones >= len(self.modelos) / 2 else 0

    def entrenar_modelo(self, datos):
        # Un modelo simple que elige una característica al azar para predecir
        indice_caracteristica = random.randint(0, len(datos[0]) - 2)  # Excluir el último valor (etiqueta)
        umbral = sum(d[indice_caracteristica] for d in datos) / len(datos)
        return ModeloSimple(indice_caracteristica, umbral)

# Clase de un modelo simple para Boosting
class ModeloSimple:
    def __init__(self, indice_caracteristica, umbral):
        self.indice_caracteristica = indice_caracteristica
        self.umbral = umbral

    def predict(self, entrada):
        valor_caracteristica = entrada[self.indice_caracteristica]
        return 1 if valor_caracteristica >= self.umbral else 0

# Entrenamiento y predicción
boosting = BoostingModelo()
boosting.entrenar(datos_entrenamiento)
nueva_entrada = (14, 3)
prediccion = boosting.predecir(nueva_entrada)
print("Predicción para la entrada", nueva_entrada, ":", prediccion)
 
