# ERICK MOISES DELGADILLO LARA
# R: 21310139 - 6E1

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Antecedentes: mediciones de CO2 y humedad relativa
co2 = ctrl.Antecedent(np.arange(0, 1501, 1), 'CO2')
humedad = ctrl.Antecedent(np.arange(0, 101, 1), 'Humedad')

# Consecuente: calidad del aire
calidad_aire = ctrl.Consequent(np.arange(0, 11, 1), 'Calidad del Aire')

# Funciones de membresía para el CO2
co2['bajo'] = fuzz.trapmf(co2.universe, [0, 0, 300, 600])
co2['medio'] = fuzz.trimf(co2.universe, [300, 600, 900])
co2['alto'] = fuzz.trapmf(co2.universe, [600, 900, 1500, 1500])

# Funciones de membresía para la humedad
humedad['baja'] = fuzz.trapmf(humedad.universe, [0, 0, 30, 50])
humedad['normal'] = fuzz.trimf(humedad.universe, [30, 50, 80])
humedad['alta'] = fuzz.trapmf(humedad.universe, [50, 80, 100, 100])

# Funciones de membresía para la calidad del aire
calidad_aire['mala'] = fuzz.trapmf(calidad_aire.universe, [0, 0, 3, 5])
calidad_aire['regular'] = fuzz.trimf(calidad_aire.universe, [3, 5, 7])
calidad_aire['buena'] = fuzz.trapmf(calidad_aire.universe, [5, 7, 10, 10])

# Reglas difusas
regla1 = ctrl.Rule(co2['bajo'] & humedad['baja'], calidad_aire['buena'])
regla2 = ctrl.Rule(co2['medio'] | humedad['normal'], calidad_aire['regular'])
regla3 = ctrl.Rule(co2['alto'] | humedad['alta'], calidad_aire['mala'])

# Sistema de control
sistema_control = ctrl.ControlSystem([regla1, regla2, regla3])
calidad_aire_ctrl = ctrl.ControlSystemSimulation(sistema_control)

# Entradas del usuario (mediciones de CO2 y humedad)
co2_input = 800
humedad_input = 60

# Definir las entradas
calidad_aire_ctrl.input['CO2'] = co2_input
calidad_aire_ctrl.input['Humedad'] = humedad_input

# Computar la salida
calidad_aire_ctrl.compute()

# Mostrar el resultado
print("Calidad del aire:", calidad_aire_ctrl.output['Calidad del Aire'])
