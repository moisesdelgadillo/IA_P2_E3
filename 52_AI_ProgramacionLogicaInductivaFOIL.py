# ERICK MOISES DELGADILLO LARA
# R: 21310139 - 6E1

def encontrar_regla(datos_entrenamiento, atributos):
    reglas = []
    # Iterar sobre cada atributo
    for atributo in atributos:
        valores_posibles = set([dato[atributo] for dato in datos_entrenamiento])
        # Iterar sobre cada valor posible del atributo
        for valor in valores_posibles:
            regla = {atributo: valor}
            reglas.append(regla)
    return reglas

# Ejemplo de datos de entrenamiento
datos_entrenamiento = [
    {'Outlook': 'sunny', 'Temperature': 'hot', 'Humidity': 'high', 'Windy': 'false', 'Class': 'negativa'},
    {'Outlook': 'sunny', 'Temperature': 'hot', 'Humidity': 'high', 'Windy': 'true', 'Class': 'negativa'},
    {'Outlook': 'overcast', 'Temperature': 'hot', 'Humidity': 'high', 'Windy': 'false', 'Class': 'positiva'},
    {'Outlook': 'rainy', 'Temperature': 'mild', 'Humidity': 'high', 'Windy': 'false', 'Class': 'positiva'},
    {'Outlook': 'rainy', 'Temperature': 'cool', 'Humidity': 'normal', 'Windy': 'false', 'Class': 'positiva'},
    {'Outlook': 'rainy', 'Temperature': 'cool', 'Humidity': 'normal', 'Windy': 'true', 'Class': 'negativa'},
    {'Outlook': 'overcast', 'Temperature': 'cool', 'Humidity': 'normal', 'Windy': 'true', 'Class': 'positiva'},
    {'Outlook': 'sunny', 'Temperature': 'mild', 'Humidity': 'high', 'Windy': 'false', 'Class': 'negativa'},
    {'Outlook': 'sunny', 'Temperature': 'cool', 'Humidity': 'normal', 'Windy': 'false', 'Class': 'positiva'},
    {'Outlook': 'rainy', 'Temperature': 'mild', 'Humidity': 'normal', 'Windy': 'false', 'Class': 'positiva'},
    {'Outlook': 'sunny', 'Temperature': 'mild', 'Humidity': 'normal', 'Windy': 'true', 'Class': 'positiva'},
    {'Outlook': 'overcast', 'Temperature': 'mild', 'Humidity': 'high', 'Windy': 'true', 'Class': 'positiva'},
    {'Outlook': 'overcast', 'Temperature': 'hot', 'Humidity': 'normal', 'Windy': 'false', 'Class': 'positiva'},
    {'Outlook': 'rainy', 'Temperature': 'mild', 'Humidity': 'high', 'Windy': 'true', 'Class': 'negativa'}
]

atributos = ['Outlook', 'Temperature', 'Humidity', 'Windy']

reglas_encontradas = encontrar_regla(datos_entrenamiento, atributos)
print("Reglas encontradas:")
for regla in reglas_encontradas:
    print(regla)
