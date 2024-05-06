# ERICK MOISES DELGADILLO LARA
# R: 21310139 - 6E1

# Definición de la clase Fruta para representar una fruta con sus características
class Fruta:
    def __init__(self, nombre, color, forma):
        self.nombre = nombre  # Nombre de la fruta
        self.color = color    # Color de la fruta
        self.forma = forma    # Forma de la fruta

# Función para aprender las características comunes de un conjunto de frutas
def aprender_caracteristicas(frutas):
    caracteristicas_comunes = {}  # Diccionario para almacenar las características comunes

    for fruta in frutas:
        if fruta.color not in caracteristicas_comunes:
            caracteristicas_comunes[fruta.color] = set()  # Crear un conjunto para cada color
        caracteristicas_comunes[fruta.color].add(fruta.forma)  # Agregar la forma al conjunto del color

    return caracteristicas_comunes

# Lista de frutas para el aprendizaje inductivo
frutas_ejemplo = [
    Fruta("Manzana", "Rojo", "Redonda"),
    Fruta("Naranja", "Naranja", "Redonda"),
    Fruta("Plátano", "Amarillo", "Alargada"),
    Fruta("Limon", "Amarillo", "Redonda")
]

# Aprender las características comunes de las frutas
caracteristicas_aprendidas = aprender_caracteristicas(frutas_ejemplo)

# Imprimir las características comunes aprendidas
print("Características comunes aprendidas:")
for color, formas in caracteristicas_aprendidas.items():
    git statprint(f"Color: {color}, Formas: {', '.join(formas)}")
    
