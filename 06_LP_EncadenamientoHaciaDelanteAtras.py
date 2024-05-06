# ERICK MOISES DELGADILLO LARA
# R: 21310139 - 6E1

# Función para el encadenamiento hacia adelante
def encadenamiento_hacia_adelante(tareas_pendientes, reglas):
    """Realiza el encadenamiento hacia adelante para planificar las tareas."""
    tareas_realizadas = []
    while tareas_pendientes:
        tarea_actual = tareas_pendientes.pop(0)
        if tarea_actual in reglas:
            tareas_pendientes.extend(reglas[tarea_actual])
        tareas_realizadas.append(tarea_actual)
    return tareas_realizadas

# Función para el encadenamiento hacia atrás
def encadenamiento_hacia_atras(tarea_final, reglas):
    """Realiza el encadenamiento hacia atrás para planificar las tareas."""
    tareas_pendientes = [tarea_final]
    tareas_realizadas = []
    while tareas_pendientes:
        tarea_actual = tareas_pendientes.pop()
        if tarea_actual in reglas:
            tareas_pendientes.extend(reglas[tarea_actual])
        tareas_realizadas.append(tarea_actual)
    return tareas_realizadas

# Ejemplo de uso
reglas_mudanza = {
    'revisar pertenencias': ['empacar cajas'],
    'empacar cajas': ['alquilar camión', 'solicitar ayuda amigos'],
    'alquilar camión': ['cargar cajas'],
    'solicitar ayuda amigos': ['cargar cajas'],
    'cargar cajas': ['conducir al nuevo hogar'],
    'conducir al nuevo hogar': ['descargar cajas', 'desempacar cajas'],
    'descargar cajas': [],
    'desempacar cajas': ['organizar pertenencias']
}

# Planificación hacia adelante desde el inicio de la mudanza
tareas_iniciales = ['revisar pertenencias']
tareas_planificadas_adelante = encadenamiento_hacia_adelante(tareas_iniciales, reglas_mudanza)
print("Planificación hacia adelante desde el inicio de la mudanza:")
print(tareas_planificadas_adelante)

# Planificación hacia atrás desde el final de la mudanza
tarea_final = 'descargar cajas'
tareas_planificadas_atras = encadenamiento_hacia_atras(tarea_final, reglas_mudanza)
print("\nPlanificación hacia atrás desde el final de la mudanza:")
print(tareas_planificadas_atras)
