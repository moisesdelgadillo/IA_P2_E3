# ERICK MOISES DELGADILLO LARA
# R: 21310139 - 6E1

# Base de conocimientos de restaurantes y sus características
base_conocimientos_restaurantes = {
    'restaurante_a': {'ambiente_acogedor', 'buena_comida', 'precios_moderados'},
    'restaurante_b': {'buena_comida', 'precios_elevados'},
    'restaurante_c': {'buena_comida', 'precios_moderados', 'terraza'},
    'restaurante_d': {'buena_comida', 'precios_moderados'}
}

# Reglas de recomendación de restaurantes
reglas_recomendacion = {
    'A': {'restaurante_a', 'restaurante_b'},
    'B': {'restaurante_c', 'restaurante_d'}
}

# Función para recomendar un restaurante al usuario
def recomendar_restaurante(preferencias_usuario):
    """Recomienda un restaurante al usuario utilizando lógica por defecto."""
    restaurantes_recomendados = set()
    for regla, restaurantes in reglas_recomendacion.items():
        if regla in preferencias_usuario:
            restaurantes_recomendados.update(restaurantes)
    return restaurantes_recomendados

# Ejemplo de uso
preferencias_usuario = {'A'}  # El usuario prefiere precios moderados
print("Restaurantes recomendados para el usuario:", recomendar_restaurante(preferencias_usuario))
