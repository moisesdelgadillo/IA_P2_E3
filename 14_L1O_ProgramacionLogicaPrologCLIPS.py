# ERICK MOISES DELGADILLO LARA
# R: 21310139 - 6E1

# Base de conocimientos de las clases y horarios
base_conocimientos_clases = {
    'matematicas': {'lunes', 'miercoles'},
    'historia': {'martes', 'jueves'},
    'ciencias': {'miercoles', 'viernes'}
}

# Reglas de consulta
def consulta_horario_clase(materia, dia):
    """Consulta el horario de una clase en un día específico."""
    if materia in base_conocimientos_clases:
        return dia in base_conocimientos_clases[materia]
    else:
        return False

# Ejemplo de uso
print("Horario de clases:")
print("¿Matemáticas se imparte el lunes?", consulta_horario_clase('matematicas', 'lunes'))
print("¿Historia se imparte el viernes?", consulta_horario_clase('historia', 'viernes'))
print("¿Ciencias se imparte el jueves?", consulta_horario_clase('ciencias', 'jueves'))
