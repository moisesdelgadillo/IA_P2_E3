# ERICK MOISES DELGADILLO LARA
# R: 21310139 - 6E1

# Definición de la clase Accion para representar una acción en la planificación
class Accion:
    def __init__(self, nombre, precondiciones, efectos):
        self.nombre = nombre  # Nombre de la acción
        self.precondiciones = precondiciones  # Lista de precondiciones necesarias para la acción
        self.efectos = efectos  # Lista de efectos de la acción

# Función para encontrar la planificación utilizando el algoritmo SATPLAN
def satplan(acciones, objetivo):
    # Definir las cláusulas iniciales como las precondiciones del objetivo
    clausulas = objetivo.precondiciones.copy()
    
    # Mientras las precondiciones del objetivo no estén satisfechas
    while not all(clausula in clausulas for clausula in objetivo.precondiciones):
        # Agregar las cláusulas de las acciones al conjunto de cláusulas
        for accion in acciones:
            if all(clausula in clausulas for clausula in accion.efectos):
                clausulas.extend(accion.precondiciones)
    
    # Devolver el plan cuando todas las precondiciones estén satisfechas
    return clausulas

# Definición de las acciones para la planificación de la mudanza
acciones_mudanza = [
    Accion("PonerEnCaja", ["ObjetosEnLugarA"], ["ObjetosEnCaja"]),
    Accion("TransportarCaja", ["CajaEnLugarA"], ["CajaEnLugarB"]),
    Accion("SacarDeCaja", ["ObjetosEnCaja"], ["ObjetosEnLugarB"])
]

# Definición del objetivo de la mudanza
objetivo_mudanza = Accion("ObjetosEnLugarB", [], ["ObjetosEnLugarB"])

# Obtener el plan utilizando el algoritmo SATPLAN
plan = satplan(acciones_mudanza, objetivo_mudanza)

# Mostrar el plan generado
if plan:
    print("Plan para la mudanza:")
    print(plan)
else:
    print("No se pudo encontrar un plan para la mudanza.")
