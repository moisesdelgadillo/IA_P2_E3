# ERICK MOISES DELGADILLO LARA
# R: 21310139 - 6E1

# Definición de la clase Restaurante
class Restaurante:
    def __init__(self, nombre, tipo, precio, rating):
        self.nombre = nombre  # Nombre del restaurante
        self.tipo = tipo  # Tipo de cocina del restaurante
        self.precio = precio  # Rango de precios del restaurante
        self.rating = rating  # Rating del restaurante

# Definición de la clase Usuario
class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre  # Nombre del usuario
        self.preferencias = {}  # Preferencias del usuario

    def agregar_preferencia(self, tipo, rating_minimo):
        """Agrega una preferencia de tipo de restaurante con un rating mínimo."""
        self.preferencias[tipo] = rating_minimo

# Crear algunos restaurantes
restaurante1 = Restaurante("La Pizzería", "Italiana", "$$", 4.5)
restaurante2 = Restaurante("El Tenedor Feliz", "Mexicana", "$", 3.8)
restaurante3 = Restaurante("El Sabor Oriental", "Asiática", "$$", 4.0)

# Crear un usuario
usuario = Usuario("Ana")

# Agregar preferencias de usuario
usuario.agregar_preferencia("Italiana", 4.0)
usuario.agregar_preferencia("Mexicana", 3.5)

# Filtrar restaurantes según las preferencias del usuario
restaurantes_recomendados = []
for restaurante in [restaurante1, restaurante2, restaurante3]:
    if restaurante.tipo in usuario.preferencias and restaurante.rating >= usuario.preferencias[restaurante.tipo]:
        restaurantes_recomendados.append(restaurante)

# Mostrar los restaurantes recomendados
print(f"Restaurantes recomendados para {usuario.nombre}:")
for restaurante in restaurantes_recomendados:
    print(f"- {restaurante.nombre} ({restaurante.tipo}) - Rating: {restaurante.rating}")
