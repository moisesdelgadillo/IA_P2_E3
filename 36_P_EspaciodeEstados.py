# ERICK MOISES DELGADILLO LARA
# R: 21310139 - 6E1

# Definición de la clase Estado para representar un estado en el espacio de estados
class Estado:
    def __init__(self, ubicacion, combustible, destino_alcanzado):
        self.ubicacion = ubicacion  # Ubicación actual del viajero
        self.combustible = combustible  # Nivel de combustible del vehículo
        self.destino_alcanzado = destino_alcanzado  # Booleano indicando si se ha alcanzado el destino

# Función para generar los posibles estados sucesores a partir de un estado dado
def generar_sucesores(estado_actual):
    sucesores = []
    # Posibles ubicaciones siguientes
    posibles_ubicaciones = ["Ciudad A", "Ciudad B", "Ciudad C"]
    # Posibles niveles de combustible siguientes
    posibles_combustibles = [100, 50, 20]
    # Generar todos los posibles estados sucesores
    for ubicacion in posibles_ubicaciones:
        for combustible in posibles_combustibles:
            # Verificar si el estado siguiente alcanza el destino
            destino_alcanzado = ubicacion == "Ciudad C" and combustible >= 20
            sucesores.append(Estado(ubicacion, combustible, destino_alcanzado))
    return sucesores

# Función principal para encontrar el camino hacia el destino
def encontrar_camino_inicial(estado_inicial, objetivo):
    frontera = [estado_inicial]  # Lista para almacenar los estados frontera
    visitados = set()  # Conjunto para almacenar los estados visitados
    while frontera:
        estado_actual = frontera.pop(0)  # Obtener el primer estado de la frontera
        visitados.add(estado_actual)  # Agregar el estado actual a los visitados
        if estado_actual.destino_alcanzado:  # Verificar si se ha alcanzado el destino
            return estado_actual
        # Generar los sucesores del estado actual y agregarlos a la frontera si no han sido visitados
        for sucesor in generar_sucesores(estado_actual):
            if sucesor not in visitados and sucesor not in frontera:
                frontera.append(sucesor)
    return None

# Definición del estado inicial del viaje
estado_inicial = Estado("Ciudad A", 100, False)
# Definición del objetivo del viaje
objetivo = Estado("Ciudad C", None, True)

# Encontrar el camino hacia el destino
estado_final = encontrar_camino_inicial(estado_inicial, objetivo)

# Mostrar el resultado
if estado_final:
    print(f"El viajero ha llegado a su destino en {estado_final.ubicacion} con {estado_final.combustible}% de combustible.")
else:
    print("El viajero no ha logrado llegar a su destino.")
