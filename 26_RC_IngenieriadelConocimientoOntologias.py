# ERICK MOISES DELGADILLO LARA
# R: 21310139 - 6E1

# Definición de la clase Animal
class Animal:
    def __init__(self, nombre, especie, tipo_alimentacion):
        self.nombre = nombre  # Nombre del animal
        self.especie = especie  # Especie del animal
        self.tipo_alimentacion = tipo_alimentacion  # Tipo de alimentación del animal

# Definición de la clase Ontología
class Ontologia:
    def __init__(self):
        self.animales = []  # Lista de animales en la ontología

    def agregar_animal(self, nombre, especie, tipo_alimentacion):
        """Agrega un nuevo animal a la ontología."""
        animal = Animal(nombre, especie, tipo_alimentacion)
        self.animales.append(animal)

    def buscar_animal_por_nombre(self, nombre):
        """Busca un animal en la ontología por su nombre."""
        for animal in self.animales:
            if animal.nombre == nombre:
                return animal
        return None

# Crear una ontología de animales
ontologia_animales = Ontologia()

# Agregar algunos animales a la ontología
ontologia_animales.agregar_animal("León", "Felino", "Carnívoro")
ontologia_animales.agregar_animal("Elefante", "Proboscidea", "Herbívoro")
ontologia_animales.agregar_animal("Tigre", "Felino", "Carnívoro")

# Buscar un animal por su nombre
nombre_animal = "León"
animal_buscado = ontologia_animales.buscar_animal_por_nombre(nombre_animal)
if animal_buscado:
    print("Información sobre el animal:", animal_buscado.nombre)
    print("Especie:", animal_buscado.especie)
    print("Tipo de alimentación:", animal_buscado.tipo_alimentacion)
else:
    print("El animal no se encuentra en la ontología.")
