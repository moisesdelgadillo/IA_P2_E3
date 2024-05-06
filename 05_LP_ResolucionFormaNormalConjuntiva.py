# ERICK MOISES DELGADILLO LARA
# R: 21310139 - 6E1

# Función para determinar qué actividades hacer en un día de viaje
def determinar_actividades(dia1, dia2):
    """Determina las actividades para dos días de viaje."""
    actividades_comunes = []
    for actividad in dia1:
        if actividad not in dia2 and actividad not in actividades_comunes:
            actividades_comunes.append(actividad)
    for actividad in dia2:
        if actividad not in dia1 and actividad not in actividades_comunes:
            actividades_comunes.append(actividad)
    return actividades_comunes

# Función para planificar una lista de actividades para un viaje
def planificar_viaje(actividades):
    """Planifica una lista de actividades para un día de viaje."""
    # Aquí implementarías tu algoritmo para planificar el día de viaje
    # Por simplicidad, asumimos que las actividades ya están planificadas
    return actividades

# Ejemplo de uso
dia1 = ['visitar museo', 'comer en restaurante', 'pasear por el parque']
dia2 = ['comer en restaurante', 'ver una película']
print("Actividades para el Día 1:", dia1)
print("Actividades para el Día 2:", dia2)
print()

# Determinar actividades comunes para ambos días
actividades_comunes = determinar_actividades(dia1, dia2)
print("Actividades comunes:", actividades_comunes)

# Planificar las actividades para un día de viaje
actividades_dia = ['visitar museo', 'comer en restaurante', 'pasear por el parque']
planificacion = planificar_viaje(actividades_dia)
print("Planificación del día de viaje:", planificacion)
