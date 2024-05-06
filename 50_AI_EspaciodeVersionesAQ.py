# ERICK MOISES DELGADILLO LARA
# R: 21310139 - 6E1

def espacio_versiones(datos_entrenamiento):
    # Inicializamos el espacio de versiones con la primera instancia
    espacio = [datos_entrenamiento[0][:-1]]
    
    # Recorremos cada instancia en los datos de entrenamiento
    for instancia in datos_entrenamiento:
        # Si la clase de la instancia es positiva, actualizamos el espacio de versiones
        if instancia[-1] == 'si':
            # Creamos una copia del espacio de versiones actual
            nuevo_espacio = espacio[:]
            # Recorremos cada hipótesis en el espacio de versiones
            for hipotesis in espacio:
                # Verificamos si la hipótesis es consistente con la instancia
                if not es_consistente(hipotesis, instancia[:-1]):
                    # Si no es consistente, la eliminamos del nuevo espacio de versiones
                    nuevo_espacio.remove(hipotesis)
            # Actualizamos el espacio de versiones con el nuevo espacio
            espacio = nuevo_espacio
    
    # Devolvemos el espacio de versiones final
    return espacio

def es_consistente(hipotesis, instancia):
    # Verificamos si la hipótesis es consistente con la instancia
    for i in range(len(hipotesis)):
        # Si la hipótesis es específica (no es '?') y no coincide con la instancia, no es consistente
        if hipotesis[i] != '?' and hipotesis[i] != instancia[i]:
            return False
    # Si la hipótesis es consistente con la instancia, devolvemos True
    return True

# Ejemplo de datos de entrenamiento
datos_entrenamiento = [
    ['sol', 'calor', 'alta', 'debil', 'si'],
    ['sol', 'calor', 'alta', 'fuerte', 'no'],
    ['nublado', 'calor', 'alta', 'debil', 'si'],
    ['lluvia', 'templado', 'alta', 'debil', 'si'],
    ['lluvia', 'frio', 'normal', 'debil', 'si']
]

# Obtenemos el espacio de versiones
espacio_versiones = espacio_versiones(datos_entrenamiento)

# Imprimimos el espacio de versiones
print("Espacio de Versiones:")
for hipotesis in espacio_versiones:
    print(hipotesis)
