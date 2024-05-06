# ERICK MOISES DELGADILLO LARA
# R: 21310139 - 6E1

# Definición de la clase Destino
class Destino:
    def __init__(self, nombre, clima, costo, popularidad):
        self.nombre = nombre  # Nombre del destino
        self.clima = clima  # Clima típico del destino
        self.costo = costo  # Costo promedio del viaje al destino
        self.popularidad = popularidad  # Nivel de popularidad del destino

# Definición de la clase Usuario
class Usuario:
    def __init__(self, nombre, presupuesto, flexibilidad):
        self.nombre = nombre  # Nombre del usuario
        self.presupuesto = presupuesto  # Presupuesto disponible para el viaje
        self.flexibilidad = flexibilidad  # Flexibilidad del usuario para adaptarse a diferentes condiciones

# Función para recomendar destinos
def recomendar_destinos(usuario, destinos):
    destinos_recomendados = []
    for destino in destinos:
        # Calcular el factor de certeza para cada destino basado en la disponibilidad de recursos y preferencias del usuario
        factor_certeza = min(usuario.presupuesto / destino.costo, usuario.flexibilidad)
        # Agregar el destino a la lista de recomendaciones solo si el factor de certeza es mayor que un umbral
        umbral_certeza = 0.5  # Umbral de certeza
        if factor_certeza > umbral_certeza:
            destinos_recomendados.append((destino, factor_certeza))
    return destinos_recomendados

# Crear algunos destinos
destino1 = Destino("Playa del Carmen", "Tropical", 1000, 0.8)
destino2 = Destino("Nueva York", "Templado", 2000, 0.9)
destino3 = Destino("Tokio", "Templado", 1500, 0.7)

# Crear un usuario
usuario = Usuario("Ana", 1500, 0.6)

# Lista de destinos disponibles
destinos_disponibles = [destino1, destino2, destino3]

# Recomendar destinos al usuario
destinos_recomendados = recomendar_destinos(usuario, destinos_disponibles)

# Mostrar destinos recomendados
print(f"Destinos recomendados para {usuario.nombre}:")
for destino, factor_certeza in destinos_recomendados:
    print(f"- {destino.nombre} (Factor de certeza: {factor_certeza})")
