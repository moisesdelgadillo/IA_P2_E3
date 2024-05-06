# ERICK MOISES DELGADILLO LARA
# R: 21310139 - 6E1

# Base de conocimiento: reglas y hechos
base_conocimiento = {
    'sintoma1': {
        'causa': 'enfermedad1',
        'regla': lambda x: x['sintoma1'] == 'si'
    },
    'sintoma2': {
        'causa': 'enfermedad2',
        'regla': lambda x: x['sintoma2'] == 'si'
    },
    'sintoma3': {
        'causa': 'enfermedad3',
        'regla': lambda x: x['sintoma3'] == 'si'
    }
}

# Función para realizar el diagnóstico
def diagnosticar(sintomas):
    enfermedades = []
    for sintoma, info in base_conocimiento.items():
        if info['regla'](sintomas):
            enfermedades.append(info['causa'])
    return enfermedades

# Ejemplo de uso del sistema experto
sintomas_paciente = {
    'sintoma1': 'no',
    'sintoma2': 'si',
    'sintoma3': 'si'
}
enfermedades_diagnosticadas = diagnosticar(sintomas_paciente)
print("El paciente puede tener las siguientes enfermedades:", enfermedades_diagnosticadas)
