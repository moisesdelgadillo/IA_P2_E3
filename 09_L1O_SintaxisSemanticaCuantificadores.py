# ERICK MOISES DELGADILLO LARA
# R: 21310139 - 6E1

# Definición de la base de datos de personas
base_de_datos_personas = [
    {'nombre': 'Juan', 'edad': 25, 'ciudad': 'Ciudad A'},
    {'nombre': 'María', 'edad': 30, 'ciudad': 'Ciudad B'},
    {'nombre': 'Pedro', 'edad': 28, 'ciudad': 'Ciudad A'},
    {'nombre': 'Ana', 'edad': 35, 'ciudad': 'Ciudad C'}
]

# Función para buscar personas que cumplen con un predicado
def buscar_personas(predicado):
    """Busca personas que cumplen con un predicado en la base de datos."""
    personas_encontradas = []
    for persona in base_de_datos_personas:
        if predicado(persona):
            personas_encontradas.append(persona['nombre'])
    return personas_encontradas

# Predicado para encontrar personas mayores de una cierta edad
def personas_mayores_que(persona):
    """Predicado para encontrar personas mayores que una cierta edad."""
    return persona['edad'] > 28

# Predicado para encontrar personas que viven en una ciudad específica
def personas_en_ciudad(persona, ciudad):
    """Predicado para encontrar personas que viven en una ciudad específica."""
    return persona['ciudad'] == ciudad

# Ejemplo de uso
print("Personas mayores de 28 años:")
print(buscar_personas(personas_mayores_que))

print("\nPersonas que viven en Ciudad A:")
print(buscar_personas(lambda persona: personas_en_ciudad(persona, 'Ciudad A')))
