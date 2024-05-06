# ERICK MOISES DELGADILLO LARA
# R: 21310139 - 6E1

# Definición de la clase Actividad para representar una actividad en la planificación
class Actividad:
    def __init__(self, nombre, predecesoras=None):
        self.nombre = nombre  # Nombre de la actividad
        self.predecesoras = set(predecesoras) if predecesoras else set()  # Conjunto de actividades predecesoras

# Función para encontrar el orden parcial de las actividades
def orden_parcial(actividades):
    orden = []  # Lista para almacenar el orden parcial de actividades
    pendientes = set(actividades)  # Conjunto de actividades pendientes
    while pendientes:
        # Encontrar actividades sin predecesoras
        sin_predecesoras = [act for act in pendientes if not act.predecesoras]
        # Si no hay actividades sin predecesoras, hay un ciclo en las dependencias
        if not sin_predecesoras:
            print("Error: Se ha detectado un ciclo en las dependencias.")
            return None
        # Seleccionar una actividad sin predecesoras y agregarla al orden parcial
        actividad = sin_predecesoras[0]
        orden.append(actividad.nombre)
        pendientes.remove(actividad)
        # Actualizar las predecesoras de las actividades restantes
        for act in pendientes:
            act.predecesoras.discard(actividad.nombre)
    return orden

# Definición de las actividades para la planificación de la fiesta
actividades_fiesta = [
    Actividad("Comprar ingredientes"),
    Actividad("Preparar comida", ["Comprar ingredientes"]),
    Actividad("Decorar lugar", ["Comprar ingredientes"]),
    Actividad("Invitar amigos"),
    Actividad("Preparar música", ["Invitar amigos"]),
    Actividad("Terminar preparativos", ["Preparar comida", "Decorar lugar", "Preparar música"])
]

# Obtener el orden parcial de las actividades para la fiesta
orden = orden_parcial(actividades_fiesta)

# Mostrar el orden parcial de las actividades
if orden:
    print("Orden parcial de actividades para la fiesta:")
    for i, actividad in enumerate(orden, start=1):
        print(f"{i}. {actividad}")
