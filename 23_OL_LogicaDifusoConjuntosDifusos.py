# ERICK MOISES DELGADILLO LARA
# R: 21310139 - 6E1

import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

# Definir el universo del discurso y las funciones de pertenencia para las variables lingüísticas
x = np.arange(0, 11, 1)
y = np.arange(0, 11, 1)
z = np.arange(0, 11, 1)

# Definir las funciones de pertenencia para las variables lingüísticas
bajo = fuzz.trimf(x, [0, 0, 5])
medio = fuzz.trimf(x, [0, 5, 10])
alto = fuzz.trimf(x, [5, 10, 10])

# Visualizar las funciones de pertenencia
plt.plot(x, bajo, 'b', linewidth=1.5, label='Bajo')
plt.plot(x, medio, 'g', linewidth=1.5, label='Medio')
plt.plot(x, alto, 'r', linewidth=1.5, label='Alto')
plt.title('Funciones de pertenencia')
plt.legend()
plt.show()
