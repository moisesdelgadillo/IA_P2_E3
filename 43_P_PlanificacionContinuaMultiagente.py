# ERICK MOISES DELGADILLO LARA
# R: 21310139 - 6E1

# Definición de la clase Tarea para representar una tarea de entrega de paquetes
class Tarea:
    def __init__(self, nombre, agente, duracion):
        self.nombre = nombre  # Nombre de la tarea
        self.agente = agente  # Agente encargado de la tarea
        self.duracion = duracion  # Duración estimada de la tarea en horas

# Función para planificar las tareas de entrega de paquetes de forma continua
def planificar_tareas(tareas):
    for tarea in tareas:
        print(f"Agente {tarea.agente}: Realizando la tarea '{tarea.nombre}' (Duración: {tarea.duracion} horas)")

# Definición de las tareas de entrega de paquetes
tarea1 = Tarea("Recoger paquetes", "Repartidor 1", 2)
tarea2 = Tarea("Transportar paquetes al almacén", "Repartidor 2", 3)
tarea3 = Tarea("Entregar paquetes a los clientes", "Repartidor 1", 4)

# Lista de tareas a planificar
tareas_entrega = [tarea1, tarea2, tarea3]

# Planificar las tareas de entrega de paquetes de forma continua
print("Planificación continua de tareas de entrega de paquetes:")
planificar_tareas(tareas_entrega)
