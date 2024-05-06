# ERICK MOISES DELGADILLO LARA
# R: 21310139 - 6E1

def encontrar_explicaciones(datos_entrenamiento):
    explicaciones = []
    
    # Iteramos sobre cada instancia en los datos de entrenamiento
    for instancia in datos_entrenamiento:
        # Si la clase es positiva, consideramos la instancia como relevante
        if instancia[-1] == 'positiva':
            # Agregamos la instancia como explicación
            explicaciones.append(instancia[:-1])
    
    # Devolvemos las explicaciones encontradas
    return explicaciones

def mostrar_explicaciones(explicaciones):
    print("Explicaciones relevantes encontradas:")
    for idx, explicacion in enumerate(explicaciones, start=1):
        print(f"Explicación {idx}: {explicacion}")

# Ejemplo de datos de entrenamiento
datos_entrenamiento = [
    ['sí', 'sol', 'calor', 'alta', 'debil', 'positiva'],
    ['no', 'nublado', 'calor', 'alta', 'fuerte', 'negativa'],
    ['no', 'lluvia', 'templado', 'alta', 'debil', 'positiva'],
    ['sí', 'lluvia', 'frio', 'normal', 'debil', 'positiva'],
    ['no', 'sol', 'calor', 'alta', 'fuerte', 'negativa']
]

# Encontrar las explicaciones relevantes en los datos de entrenamiento
explicaciones_encontradas = encontrar_explicaciones(datos_entrenamiento)

# Mostrar las explicaciones encontradas
mostrar_explicaciones(explicaciones_encontradas)
