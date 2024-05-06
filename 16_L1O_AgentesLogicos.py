# ERICK MOISES DELGADILLO LARA
# R: 21310139 - 6E1

# Base de conocimientos de reglas lógicas para la toma de decisiones
base_conocimientos_decisiones = {
    'temperatura': {'alta', 'baja', 'media'},
    'hora_del_dia': {'mañana', 'tarde', 'noche'},
    'ocupacion': {'ocupado', 'desocupado'},
    'actividades': {'trabajar', 'descansar', 'cocinar', 'ver_tv'}
}

# Función para que el agente lógico tome una decisión basada en las reglas
def tomar_decision(temperatura, hora_del_dia, ocupacion, actividades):
    """El agente lógico toma una decisión basada en las reglas lógicas."""
    # Si hace calor y es tarde, y no hay ocupación, se decide ver televisión
    if temperatura == 'alta' and hora_del_dia == 'tarde' and ocupacion == 'desocupado':
        return 'ver_tv'
    # Si hace frío y es noche, y la persona está ocupada, se decide cocinar
    elif temperatura == 'baja' and hora_del_dia == 'noche' and ocupacion == 'ocupado':
        return 'cocinar'
    # Si no se cumple ninguna regla específica, se decide descansar
    else:
        return 'descansar'

# Ejemplo de uso
decision = tomar_decision('alta', 'tarde', 'desocupado', {'trabajar', 'descansar'})
print("El agente lógico decide:", decision)
