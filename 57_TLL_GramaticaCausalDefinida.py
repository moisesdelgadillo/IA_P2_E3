# ERICK MOISES DELGADILLO LARA
# R: 21310139 - 6E1

# Función para realizar el análisis gramatical causal
def analizar_gramatica_causal(frase):
    # Dividir la frase en palabras
    palabras = frase.split()

    # Verificar si la frase tiene al menos tres palabras
    if len(palabras) < 3:
        print("La frase es demasiado corta para un análisis causal.")
        return

    # Identificar el sujeto, el verbo y el objeto de la primera oración
    sujeto1 = palabras[0]
    verbo1 = palabras[1]
    objeto1 = ' '.join(palabras[2:])

    # Verificar si la segunda oración empieza con una conjunción causal
    conjunciones_causales = ["porque", "ya que", "debido a que", "puesto que"]
    if palabras[-1].lower() not in conjunciones_causales:
        print("La segunda oración no empieza con una conjunción causal.")
        return

    # Identificar el sujeto, el verbo y el objeto de la segunda oración
    sujeto2 = palabras[-1]
    verbo2 = palabras[-2]
    objeto2 = ' '.join(palabras[-3:-1])

    # Imprimir el análisis causal
    print("Oración 1:")
    print("Sujeto:", sujeto1)
    print("Verbo:", verbo1)
    print("Objeto:", objeto1)
    print("\nOración 2:")
    print("Sujeto:", sujeto2)
    print("Verbo:", verbo2)
    print("Objeto:", objeto2)

# Ejemplo de uso
frase = "Juan estudia mucho porque quiere aprobar el examen"
print("Frase:", frase)
print("\nAnálisis gramatical causal:")
analizar_gramatica_causal(frase)
