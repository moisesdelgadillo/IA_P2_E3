# ERICK MOISES DELGADILLO LARA
# R: 21310139 - 6E1

# Definición de la base de conocimiento como un diccionario de hechos
base_conocimiento = {
    "A": True,
    "B": False,
    "C": True,
    "D": False
}

# Función para consultar la base de conocimiento y determinar la verdad de una expresión
def consultar_hecho(base_conocimiento, expresion):
    """Consulta la base de conocimiento para determinar la verdad de una expresión."""
    # Verificar si la expresión es un hecho conocido
    if expresion in base_conocimiento:
        return base_conocimiento[expresion]
    else:
        print(f"Hecho '{expresion}' desconocido en la base de conocimiento.")
        return None

# Ejemplo de consultas a la base de conocimiento
expresiones = ["A", "B", "C", "D", "E"]

# Consultar cada expresión en la base de conocimiento
for expresion in expresiones:
    valor_verdad = consultar_hecho(base_conocimiento, expresion)
    if valor_verdad is not None:
        print(f"El valor de verdad de '{expresion}' es: {valor_verdad}")
