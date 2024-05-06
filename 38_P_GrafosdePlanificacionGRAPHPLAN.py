# ERICK MOISES DELGADILLO LARA
# R: 21310139 - 6E1

# Definición de la clase Tarea para representar una tarea en la planificación
class Tarea:
    def __init__(self, nombre, predecesoras=[]):
        self.nombre = nombre  # Nombre de la tarea
        self.predecesoras = predecesoras  # Lista de tareas predecesoras

# Función para encontrar la planificación utilizando el algoritmo GRAPHPLAN
def planificar(tareas, objetivo):
    plan = []  # Lista para almacenar las tareas planificadas
    acciones = []  # Lista para almacenar las acciones posibles
    estados = [{tarea.nombre} for tarea in tareas]  # Lista de conjuntos de estados
    while objetivo not in estados[-1] and acciones != plan:
        # Añadir las acciones posibles al plan
        for tarea in tareas:
            if all(predecesora in estados[-1] for predecesora in tarea.predecesoras):
                acciones.append(tarea.nombre)
        # Actualizar los estados con las acciones
        nuevos_estados = set()
        for estado in estados[-1]:
            for accion in acciones:
                nuevos_estados.add(estado + accion)
        estados.append(nuevos_estados)
        plan.append(acciones)
        acciones = []
    return plan

# Definición de las tareas para la planificación de la fiesta
tareas_fiesta = [
    Tarea("Comprar_ingredientes"),
    Tarea("Preparar_comida", ["Comprar_ingredientes"]),
    Tarea("Decorar_lugar", ["Comprar_ingredientes"]),
    Tarea("Invitar_amigos"),
    Tarea("Preparar_música", ["Invitar_amigos"]),
    Tarea("Terminar_preparativos", ["Preparar_comida", "Decorar_lugar", "Preparar_música"])
]

# Objetivo: todos los invitados están en la fiesta
objetivo = "Invitar_amigosTerminar_preparativos"

# Obtener el plan utilizando el algoritmo GRAPHPLAN
plan = planificar(tareas_fiesta, objetivo)

# Mostrar el plan generado
if plan:
    print("Plan para la fiesta:")
    for i, acciones in enumerate(plan, start=1):
        print(f"Paso {i}: {', '.join(acciones)}")
else:
    print("No se pudo encontrar un plan para la fiesta.")
