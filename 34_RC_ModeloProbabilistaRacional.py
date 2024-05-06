# ERICK MOISES DELGADILLO LARA
# R: 21310139 - 6E1

# Definición de la clase PronosticoClima
class PronosticoClima:
    def __init__(self, fecha, temperatura, humedad, probabilidad_lluvia):
        self.fecha = fecha  # Fecha del pronóstico
        self.temperatura = temperatura  # Temperatura pronosticada
        self.humedad = humedad  # Humedad pronosticada
        self.probabilidad_lluvia = probabilidad_lluvia  # Probabilidad de lluvia pronosticada

# Función para predecir el clima actual
def predecir_clima_actual(datos_historicos, condiciones_actuales):
    probabilidades = []
    for pronostico in datos_historicos:
        # Calcular la similitud entre las condiciones actuales y los pronósticos históricos
        similitud = calcular_similitud(condiciones_actuales, pronostico)
        # Calcular la probabilidad de que el clima actual sea similar al pronóstico histórico
        probabilidad = similitud * pronostico.probabilidad_lluvia
        probabilidades.append(probabilidad)
    # Calcular la probabilidad total
    probabilidad_total = sum(probabilidades)
    # Normalizar las probabilidades
    probabilidades_normalizadas = [probabilidad / probabilidad_total for probabilidad in probabilidades]
    return probabilidades_normalizadas

# Función para calcular la similitud entre las condiciones actuales y un pronóstico histórico
def calcular_similitud(condiciones_actuales, pronostico):
    similitud_temperatura = abs(condiciones_actuales["temperatura"] - pronostico.temperatura)
    similitud_humedad = abs(condiciones_actuales["humedad"] - pronostico.humedad)
    return 1 / (1 + similitud_temperatura + similitud_humedad)

# Datos históricos de pronósticos de clima
pronosticos_historicos = [
    PronosticoClima("2022-05-01", 25, 60, 0.3),
    PronosticoClima("2022-05-02", 24, 65, 0.5),
    PronosticoClima("2022-05-03", 23, 70, 0.8)
]

# Condiciones climáticas actuales
condiciones_actuales = {
    "temperatura": 26,
    "humedad": 55
}

# Predecir el clima actual
probabilidades_clima_actual = predecir_clima_actual(pronosticos_historicos, condiciones_actuales)

# Mostrar las probabilidades de clima actual
print("Probabilidades de clima actual:")
for i, pronostico in enumerate(pronosticos_historicos):
    print(f"- Pronóstico para {pronostico.fecha}: {probabilidades_clima_actual[i]}")
