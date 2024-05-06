# ERICK MOISES DELGADILLO LARA
# R: 21310139 - 6E1

# Definición de la clase Tarea para representar una tarea en la planificación
class Tarea:
    def __init__(self, nombre, sub_tareas=[]):
        self.nombre = nombre  # Nombre de la tarea
        self.sub_tareas = sub_tareas  # Lista de sub-tareas

# Función para mostrar las tareas jerárquicamente
def mostrar_tareas(tarea, nivel=0):
    print("  " * nivel + tarea.nombre)  # Mostrar el nombre de la tarea con indentación
    for sub_tarea in tarea.sub_tareas:
        mostrar_tareas(sub_tarea, nivel + 1)  # Mostrar las sub-tareas con mayor indentación

# Definición de las tareas para la planificación de la fiesta
tarea_fiesta = Tarea("Organizar Fiesta", [
    Tarea("Preparativos", [
        Tarea("Comprar Ingredientes"),
        Tarea("Decorar Lugar")
    ]),
    Tarea("Invitaciones", [
        Tarea("Enviar Invitaciones"),
        Tarea("Seguir Confirmaciones")
    ]),
    Tarea("Preparar Entretenimiento", [
        Tarea("Preparar Música"),
        Tarea("Organizar Juegos")
    ])
])

# Mostrar las tareas jerárquicamente
print("Tareas para organizar la fiesta:")
mostrar_tareas(tarea_fiesta)
