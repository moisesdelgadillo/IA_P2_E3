# ERICK MOISES DELGADILLO LARA
# R: 21310139 - 6E1

# Función para realizar inferencia lógica proposicional
def inferencia_logica(base_conocimiento, reglas):
    """Realiza inferencia lógica proposicional utilizando la base de conocimiento y reglas dadas."""
    nuevos_hechos = {}  # Diccionario para almacenar nuevos hechos inferidos
    
    # Iterar sobre cada regla
    for regla, conclusion in reglas.items():
        # Verificar si la premisa de la regla está en la base de conocimiento y su conclusión no
        if all(premisa in base_conocimiento and base_conocimiento[premisa] for premisa in regla) and conclusion not in base_conocimiento:
            nuevos_hechos[conclusion] = True  # Agregar la conclusión como nuevo hecho inferido
    
    return nuevos_hechos

# Función para pedir al usuario que ingrese la base de conocimiento
def obtener_base_conocimiento():
    """Solicita al usuario que ingrese la base de conocimiento."""
    base_conocimiento = {}
    print("Ingrese la base de conocimiento:")
    while True:
        hecho = input("Hecho (o presione Enter para terminar): ").strip().upper()
        if not hecho:
            break
        valor = input(f"Valor de verdad para '{hecho}' (True o False): ").strip().lower()
        if valor == 'true':
            base_conocimiento[hecho] = True
        elif valor == 'false':
            base_conocimiento[hecho] = False
        else:
            print("Valor no válido. Por favor ingrese 'True' o 'False'.")
    return base_conocimiento

# Función para pedir al usuario que ingrese las reglas de inferencia
def obtener_reglas_inferencia():
    """Solicita al usuario que ingrese las reglas de inferencia."""
    reglas_inferencia = {}
    print("\nIngrese las reglas de inferencia:")
    while True:
        premisa = input("Premisa (o presione Enter para terminar): ").strip().upper()
        if not premisa:
            break
        conclusion = input("Conclusión: ").strip().upper()
        reglas_inferencia[premisa] = conclusion
    return reglas_inferencia

# Obtener la base de conocimiento del usuario
base_conocimiento = obtener_base_conocimiento()

# Obtener las reglas de inferencia del usuario
reglas_inferencia = obtener_reglas_inferencia()

# Realizar inferencia lógica
nuevos_hechos = inferencia_logica(base_conocimiento, reglas_inferencia)

# Imprimir nuevos hechos inferidos
if nuevos_hechos:
    print("\nNuevos hechos inferidos:")
    for hecho, valor in nuevos_hechos.items():
        print(f"{hecho}: {valor}")
else:
    print("\nNo se han inferido nuevos hechos.")
