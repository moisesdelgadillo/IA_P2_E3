# ERICK MOISES DELGADILLO LARA
# R: 21310139 - 6E1

# Base de conocimientos de las tareas y reglas de dependencia
base_conocimientos_tareas = [
    {'nombre': 'comprar_ingredientes', 'dependencias': []},
    {'nombre': 'preparar_comida', 'dependencias': ['comprar_ingredientes']},
    {'nombre': 'decorar_casa', 'dependencias': []},
    {'nombre': 'invitar_amigos', 'dependencias': []},
    {'nombre': 'organizar_juegos', 'dependencias': ['invitar_amigos', 'decorar_casa']}
]

# Función para resolver la planificación de tareas utilizando resolución con Skolem
def resolver_planificacion_tareas(tareas):
    """Resuelve la planificación de tareas utilizando resolución con Skolem."""
    while True:
        nuevas_clausulas = []
        for i in range(len(tareas)):
            for j in range(i + 1, len(tareas)):
                tarea1 = tareas[i]
                tarea2 = tareas[j]
                resolvente = resolver(tarea1, tarea2)
                if resolvente is not None:
                    if not resolvente:
                        return True  # Las tareas son consistentes
                    nuevas_clausulas.append(resolvente)
        if not nuevas_clausulas:
            return False  # No se pueden resolver más cláusulas

# Función para resolver dos tareas utilizando resolución con Skolem
def resolver(tarea1, tarea2):
    """Resuelve dos tareas utilizando resolución con Skolem."""
    for literal1 in tarea1['dependencias']:
        for literal2 in tarea2['dependencias']:
            if literal1 == 'no_' + literal2 or 'no_' + literal1 == literal2:
                return []  # Contradicción encontrada
    return None  # No se puede resolver

# Ejemplo de uso
if resolver_planificacion_tareas(base_conocimientos_tareas):
    print("Las tareas son consistentes. ¡La fiesta está planificada correctamente!")
else:
    print("Las tareas son inconsistentes. No se puede planificar la fiesta.")
