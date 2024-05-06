# ERICK MOISES DELGADILLO LARA
# R: 21310139 - 6E1

# Base de conocimientos de películas y sus géneros
base_conocimientos_peliculas = {
    'Avengers': {'acción', 'aventura', 'ciencia_ficción'},
    'Toy Story': {'animación', 'familia', 'comedia'},
    'Interestelar': {'ciencia_ficción', 'drama'}
}

# Reglas de recomendación de películas
reglas_recomendacion = {
    'A': {'Toy Story'},
    'B': {'Avengers', 'Interestelar'}
}

# Función para recomendar películas al usuario
def recomendar_peliculas(usuario):
    """Recomienda películas al usuario utilizando lógica no monótona."""
    peliculas_recomendadas = set()
    for regla, peliculas in reglas_recomendacion.items():
        if regla not in usuario:  # Verificar si el usuario no ha rechazado la regla
            peliculas_recomendadas.update(peliculas)
    return peliculas_recomendadas

# Ejemplo de uso
usuario = set()  # El usuario no ha rechazado ninguna regla aún
print("Películas recomendadas para el usuario:", recomendar_peliculas(usuario))
