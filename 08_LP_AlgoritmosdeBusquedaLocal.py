# ERICK MOISES DELGADILLO LARA
# R: 21310139 - 6E1

import random

# Función para el algoritmo de búsqueda local
def busqueda_local(ruta_actual, distancias):
    """Optimiza una ruta de entrega utilizando el algoritmo de búsqueda local."""
    mejor_ruta = ruta_actual
    distancia_mejor_ruta = calcular_distancia(mejor_ruta, distancias)
    
    # Bucle de mejora iterativa
    for _ in range(1000):
        ruta_vecina = generar_ruta_vecina(mejor_ruta)
        distancia_ruta_vecina = calcular_distancia(ruta_vecina, distancias)
        if distancia_ruta_vecina < distancia_mejor_ruta:
            mejor_ruta = ruta_vecina
            distancia_mejor_ruta = distancia_ruta_vecina
            
    return mejor_ruta

# Función para calcular la distancia total de una ruta
def calcular_distancia(ruta, distancias):
    """Calcula la distancia total de una ruta de entrega."""
    distancia_total = 0
    for i in range(len(ruta) - 1):
        ciudad_actual = ruta[i]
        siguiente_ciudad = ruta[i + 1]
        distancia_total += distancias[ciudad_actual][siguiente_ciudad]
    return distancia_total

# Función para generar una ruta vecina intercambiando dos ciudades aleatorias
def generar_ruta_vecina(ruta):
    """Genera una ruta vecina intercambiando dos ciudades aleatorias."""
    ruta_vecina = ruta[:]
    ciudad1, ciudad2 = random.sample(range(len(ruta)), 2)
    ruta_vecina[ciudad1], ruta_vecina[ciudad2] = ruta_vecina[ciudad2], ruta_vecina[ciudad1]
    return ruta_vecina

# Ejemplo de uso
distancias_entrega = {
    'A': {'B': 10, 'C': 15, 'D': 20},
    'B': {'A': 10, 'C': 35, 'D': 25},
    'C': {'A': 15, 'B': 35, 'D': 30},
    'D': {'A': 20, 'B': 25, 'C': 30}
}

ruta_inicial = ['A', 'B', 'C', 'D']
print("Ruta de entrega inicial:", ruta_inicial)

ruta_optimizada = busqueda_local(ruta_inicial, distancias_entrega)
print("Ruta de entrega optimizada:", ruta_optimizada)
