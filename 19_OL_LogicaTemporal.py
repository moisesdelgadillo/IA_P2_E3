# ERICK MOISES DELGADILLO LARA
# R: 21310139 - 6E1

# Base de conocimientos de tareas y sus horarios
base_conocimientos_tareas = {
    'lavar_platos': 'mañana',
    'ir_al_supermercado': 'tarde',
    'hacer_ejercicio': 'tarde',
    'preparar_cena': 'noche'
}

# Función para verificar si una tarea está programada para un momento específico
def tarea_programada(tarea, momento):
    """Verifica si una tarea está programada para un momento específico."""
    if tarea in base_conocimientos_tareas:
        return base_conocimientos_tareas[tarea] == momento
    else:
        return False

# Función para encontrar tareas programadas en un momento específico
def encontrar_tareas_en_momento(momento):
    """Encuentra las tareas programadas en un momento específico."""
    tareas_en_momento = []
    for tarea, momento_tarea in base_conocimientos_tareas.items():
        if momento_tarea == momento:
            tareas_en_momento.append(tarea)
    return tareas_en_momento

# Ejemplo de uso
momento_evaluar = 'tarde'
print(f"¿Hay alguna tarea programada para la {momento_evaluar}?", encontrar_tareas_en_momento(momento_evaluar))
