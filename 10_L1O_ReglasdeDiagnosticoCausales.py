# ERICK MOISES DELGADILLO LARA
# R: 21310139 - 6E1

# Base de conocimientos de síntomas y enfermedades
base_conocimientos = {
    'fiebre': {'resfriado', 'gripe', 'malaria'},
    'tos': {'resfriado', 'gripe', 'bronquitis'},
    'dolor_de_garganta': {'resfriado', 'gripe', 'amigdalitis'},
    'fatiga': {'gripe', 'malaria'},
    'dolor_de_cabeza': {'resfriado', 'gripe', 'malaria'},
    'dolor_muscular': {'gripe', 'malaria'},
    'escalofríos': {'gripe', 'malaria'},
    'dolor_de_pecho': {'bronquitis', 'amigdalitis'}
}

# Función para diagnosticar una enfermedad a partir de los síntomas
def diagnosticar_enfermedad(sintomas):
    """Diagnostica una enfermedad a partir de los síntomas proporcionados."""
    enfermedades_posibles = set()
    for sintoma in sintomas:
        if sintoma in base_conocimientos:
            enfermedades_posibles.update(base_conocimientos[sintoma])
    return enfermedades_posibles

# Síntomas proporcionados por el paciente
sintomas_paciente = ['fiebre', 'tos', 'dolor_de_cabeza']

# Diagnosticar la enfermedad del paciente
enfermedad_diagnosticada = diagnosticar_enfermedad(sintomas_paciente)

# Mostrar el resultado del diagnóstico
print("Síntomas del paciente:", sintomas_paciente)
print("Posibles enfermedades diagnosticadas:", enfermedad_diagnosticada)
