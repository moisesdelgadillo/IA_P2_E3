# ERICK MOISES DELGADILLO LARA
# R: 21310139 - 6E1

# Definición de la clase Proyecto para representar un proyecto de construcción
class Proyecto:
    def __init__(self, tarea_actual, tareas_pendientes):
        self.tarea_actual = tarea_actual  # Tarea actual en ejecución
        self.tareas_pendientes = tareas_pendientes  # Lista de tareas pendientes

# Función para vigilar la ejecución del proyecto y replanificar si es necesario
def vigilar_ejecucion_proyecto(proyecto):
    if proyecto.tarea_actual.completada:
        # Si la tarea actual se ha completado, pasar a la siguiente tarea
        if proyecto.tareas_pendientes:
            proyecto.tarea_actual = proyecto.tareas_pendientes.pop(0)
            print(f"Tarea actual completada. Nueva tarea: {proyecto.tarea_actual.nombre}")
        else:
            print("¡Proyecto completado con éxito!")
    else:
        # Si la tarea actual no se ha completado, replanificar
        print(f"La tarea {proyecto.tarea_actual.nombre} no se ha completado. Replanificando...")
        # Aquí se implementaría la lógica de replanificación según las condiciones específicas del proyecto

# Definición de las tareas del proyecto de construcción
class Tarea:
    def __init__(self, nombre, completada=False):
        self.nombre = nombre
        self.completada = completada

# Creación de un proyecto de construcción
tareas_pendientes = [Tarea("Excavación"), Tarea("Cimentación"), Tarea("Estructura"), Tarea("Acabados")]
proyecto_construccion = Proyecto(tareas_pendientes[0], tareas_pendientes[1:])

# Simulación de la vigilancia de la ejecución y replanificación del proyecto
print("Vigilando la ejecución del proyecto de construcción:")
vigilar_ejecucion_proyecto(proyecto_construccion)
vigilar_ejecucion_proyecto(proyecto_construccion)
