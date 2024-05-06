# ERICK MOISES DELGADILLO LARA
# R: 21310139 - 6E1

# Definición de la clase Pelicula
class Pelicula:
    def __init__(self, titulo, genero, duracion, rating):
        self.titulo = titulo  # Título de la película
        self.genero = genero  # Género de la película
        self.duracion = duracion  # Duración de la película en minutos
        self.rating = rating  # Rating de la película

# Definición de la clase Usuario
class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre  # Nombre del usuario
        self.preferencias = []  # Lista de películas que le gustan al usuario

    def agregar_preferencia(self, pelicula):
        """Agrega una película a las preferencias del usuario."""
        self.preferencias.append(pelicula)

# Crear algunas películas
pelicula1 = Pelicula("El padrino", "Drama", 175, 9.2)
pelicula2 = Pelicula("Toy Story", "Animación", 81, 8.3)
pelicula3 = Pelicula("Titanic", "Romance", 195, 7.8)

# Crear un usuario
usuario = Usuario("Juan")

# Agregar algunas películas a las preferencias del usuario
usuario.agregar_preferencia(pelicula1)
usuario.agregar_preferencia(pelicula3)

# Mostrar las preferencias del usuario
print(f"Preferencias de {usuario.nombre}:")
for pelicula in usuario.preferencias:
    print(f"- {pelicula.titulo} ({pelicula.genero}) - Rating: {pelicula.rating}")
