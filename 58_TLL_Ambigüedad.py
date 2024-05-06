# ERICK MOISES DELGADILLO LARA
# R: 21310139 - 6E1

# Función para analizar la ambigüedad en una frase
def analizar_ambiguedad(frase):
    # Dividir la frase en palabras
    palabras = frase.split()

    # Contar el número de posibles interpretaciones ambiguas
    num_interpretaciones = 1
    for palabra in palabras:
        # Si la palabra tiene múltiples significados, se considera ambigua
        if tiene_multiples_significados(palabra):
            num_interpretaciones *= contar_significados(palabra)

    # Imprimir el resultado
    print("La frase '{}' tiene {} posibles interpretaciones ambiguas.".format(frase, num_interpretaciones))

# Función para determinar si una palabra tiene múltiples significados
def tiene_multiples_significados(palabra):
    # Simplemente se asume que cualquier palabra tiene múltiples significados para este ejemplo
    return True

# Función para contar el número de significados de una palabra
def contar_significados(palabra):
    # Simulamos contar los significados de la palabra
    # En un caso real, esto implicaría consultar una base de datos o algún recurso lingüístico
    return 2  # Por ejemplo, podríamos decir que la palabra 'banco' tiene 2 significados: banco de sentarse y banco financiero

# Ejemplo de uso
frase = "El banco estaba cerrado"
analizar_ambiguedad(frase)
