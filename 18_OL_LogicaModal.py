# ERICK MOISES DELGADILLO LARA
# R: 21310139 - 6E1

class Mundo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.relaciones = {}

    def agregar_relacion(self, agente, propiedad):
        if agente not in self.relaciones:
            self.relaciones[agente] = set()
        self.relaciones[agente].add(propiedad)

    def obtener_propiedades(self, agente):
        return self.relaciones.get(agente, set())

# Ejemplo de mundos y relaciones
mundo1 = Mundo("Mundo1")
mundo1.agregar_relacion("Alice", "es_rico")
mundo1.agregar_relacion("Bob", "es_inteligente")

mundo2 = Mundo("Mundo2")
mundo2.agregar_relacion("Alice", "es_inteligente")
mundo2.agregar_relacion("Bob", "es_rico")

# Funciones para evaluar modalidades
def necesidad(mundo, agente, propiedad):
    return propiedad in mundo.obtener_propiedades(agente)

def posibilidad(mundo, agente, propiedad):
    return any(propiedad in mundo.obtener_propiedades(agente) for mundo in [mundo1, mundo2])

# Verificar necesidades y posibilidades
print("En Mundo1, es necesario que Alice sea rico:", necesidad(mundo1, "Alice", "es_rico"))
print("En Mundo2, es posible que Alice sea rico:", posibilidad(mundo2, "Alice", "es_rico"))
