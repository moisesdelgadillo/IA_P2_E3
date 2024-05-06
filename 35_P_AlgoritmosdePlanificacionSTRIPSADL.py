# ERICK MOISES DELGADILLO LARA
# R: 21310139 - 6E1

# Definición de la clase Tarea
class Tarea:
    def __init__(self, nombre, precondiciones, efectos):
        self.nombre = nombre  # Nombre de la tarea
        self.precondiciones = precondiciones  # Precondiciones para ejecutar la tarea
        self.efectos = efectos  # Efectos de ejecutar la tarea

# Función para planificar una serie de tareas utilizando el algoritmo STRIPS
def planificar(tareas, objetivo):
    plan = []  # Lista para almacenar el plan
    estado_actual = set()  # Conjunto para representar el estado actual
    while not all(p in estado_actual for p in objetivo):  # Mientras no se cumplan todas las condiciones del objetivo
        tarea = seleccionar_tarea(tareas, estado_actual, objetivo)  # Seleccionar una tarea que pueda realizarse
        if tarea is None:
            print("No se puede alcanzar el objetivo con las tareas proporcionadas.")
            return None
        plan.append(tarea)  # Agregar la tarea al plan
        estado_actual.update(tarea.efectos)  # Actualizar el estado actual con los efectos de la tarea
    return plan

# Función para seleccionar la siguiente tarea a ejecutar
def seleccionar_tarea(tareas, estado_actual, objetivo):
    for tarea in tareas:
        if tarea.precondiciones.issubset(estado_actual) and any(p in objetivo for p in tarea.efectos):
            return tarea
    return None  # Si no se puede seleccionar ninguna tarea

# Definición de las tareas para planificar la fiesta de cumpleaños
tareas = [
    Tarea("Decorar", {"Salón limpio", "Música preparada"}, {"Salón decorado"}),
    Tarea("Cocinar", {"Ingredientes comprados"}, {"Comida preparada"}),
    Tarea("Invitar amigos", set(), {"Amigos informados"}),
    Tarea("Comprar ingredientes", set(), {"Ingredientes comprados"}),
    Tarea("Limpiar salón", {"Fiesta terminada"}, {"Salón limpio"}),
    Tarea("Terminar fiesta", {"Salón decorado", "Comida servida"}, {"Fiesta terminada"}),
    Tarea("Preparar música", {"Música seleccionada"}, {"Música preparada"}),
    Tarea("Seleccionar música", set(), {"Música seleccionada"})
]

# Objetivo: condiciones que deben cumplirse al finalizar la planificación
objetivo = {"Fiesta terminada"}

# Planificar la fiesta de cumpleaños
plan = planificar(tareas, objetivo)

# Mostrar el plan generado
if plan is not None:
    print("Plan para la fiesta de cumpleaños:")
    for i, tarea in enumerate(plan, start=1):
        print(f"{i}. {tarea.nombre}")
