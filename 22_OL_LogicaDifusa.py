# ERICK MOISES DELGADILLO LARA
# R: 21310139 - 6E1

# Función de membresía para la velocidad del ventilador
def membresia_velocidad(velocidad):
    """Define las funciones de membresía para la velocidad del ventilador."""
    # Función de membresía para la velocidad baja
    if velocidad <= 20:
        return 1
    elif velocidad > 20 and velocidad < 50:
        return (50 - velocidad) / 30
    else:
        return 0

    # Función de membresía para la velocidad media
    if velocidad > 20 and velocidad <= 50:
        return (velocidad - 20) / 30
    elif velocidad > 50 and velocidad < 80:
        return 1
    elif velocidad >= 80 and velocidad < 100:
        return (100 - velocidad) / 20
    else:
        return 0

    # Función de membresía para la velocidad alta
    if velocidad >= 80 and velocidad <= 100:
        return (velocidad - 80) / 20
    elif velocidad > 100:
        return 1
    else:
        return 0

# Función para determinar la velocidad del ventilador
def velocidad_ventilador(velocidad):
    """Determina la velocidad del ventilador basada en la entrada de velocidad."""
    baja = membresia_velocidad(velocidad)
    media = membresia_velocidad(velocidad)
    alta = membresia_velocidad(velocidad)

    return baja, media, alta

# Ejemplo de uso
velocidad_actual = 65
print("Velocidad del ventilador (baja, media, alta):", velocidad_ventilador(velocidad_actual))
