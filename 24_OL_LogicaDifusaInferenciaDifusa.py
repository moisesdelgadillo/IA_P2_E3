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

# Definir las reglas difusas
regla1 = fuzz.interp_membership(x, bajo, 2)
regla2 = fuzz.interp_membership(y, medio, 3)
regla3 = fuzz.interp_membership(z, alto, 7)

# Realizar la inferencia difusa utilizando el operador MIN para combinar las reglas
resultado = fuzz.fuzzy_and([regla1, regla2, regla3])

# Visualizar el resultado
plt.plot(x, resultado, 'm', linewidth=1.5, label='Resultado')
plt.title('Resultado de la inferencia difusa')
plt.legend()
plt.show()
