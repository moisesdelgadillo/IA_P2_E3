# ERICK MOISES DELGADILLO LARA
# R: 21310139 - 6E1

#Hacia adelante
# Base de conocimiento (reglas)
reglas = {
    'regla1': (('p', 'q'), 'r'),
    'regla2': ('s', 'p'),
    'regla3': ('t', 's')
}

# Hechos conocidos
hechos = {'t'}

# Encadenamiento hacia adelante
nuevos_hechos = set()
while True:
    se_encontro_nueva_conclusion = False
    for cuerpo, conclusion in reglas.values():
        if set(cuerpo).issubset(hechos) and conclusion not in hechos:
            nuevos_hechos.add(conclusion)
            se_encontro_nueva_conclusion = True
    if not se_encontro_nueva_conclusion:
        break
    hechos.update(nuevos_hechos)

print("Hechos derivados:", hechos)


#Hacia atras
# Base de conocimiento (reglas)
reglas = {
    'regla1': ('p', ('q', 'r')),
    'regla2': ('s', 'p'),
    'regla3': ('t', 's')
}

# Meta que se desea probar
meta = 't'

# Encadenamiento hacia atrás
def encadenamiento_hacia_atras(meta, reglas, hechos):
    if meta in hechos:
        return True
    for regla, cuerpo in reglas.items():
        if cuerpo[0] == meta:
            submetas = cuerpo[1] if isinstance(cuerpo[1], tuple) else (cuerpo[1],)
            if all(encadenamiento_hacia_atras(submeta, reglas, hechos) for submeta in submetas):
                hechos.add(meta)
                return True
    return False

hechos = set()
if encadenamiento_hacia_atras(meta, reglas, hechos):
    print("La meta", meta, "se puede probar.")
    print("Hechos derivados:", hechos)
else:
    print("La meta", meta, "no se puede probar.")
