# ERICK MOISES DELGADILLO LARA
# R: 21310139 - 6E1

# Definición de la clase Planificacion para representar una planificación condicional
class Planificacion:
    def __init__(self, tarea, precondiciones, acciones):
        self.tarea = tarea  # Tarea a realizar
        self.precondiciones = precondiciones  # Condiciones que deben cumplirse para realizar la tarea
        self.acciones = acciones  # Acciones a realizar si se cumplen las condiciones

# Función para ejecutar la planificación condicional
def ejecutar_planificacion(plan):
    # Verificar si se cumplen las precondiciones
    if all(condicion for condicion in plan.precondiciones):
        # Ejecutar las acciones
        print(f"Se están realizando las acciones para la tarea: {plan.tarea}")
        for accion in plan.acciones:
            print(f"Realizando acción: {accion}")
    else:
        print("No se cumplen las condiciones para realizar la tarea.")

# Definición de la planificación para el viaje en automóvil
plan_viaje = Planificacion(
    tarea="Viajar en automóvil",
    precondiciones=[True, True],  # Condiciones: gasolina y aceite suficientes
    acciones=["Cargar gasolina", "Verificar aceite", "Iniciar viaje"]
)

# Ejecutar la planificación para el viaje en automóvil
print("Planificación para el viaje en automóvil:")
ejecutar_planificacion(plan_viaje)
