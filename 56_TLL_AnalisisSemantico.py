# ERICK MOISES DELGADILLO LARA
# R: 21310139 - 6E1

# Función para realizar el análisis semántico
def analisis_semantico(frase):
    # Dividir la frase en palabras
    palabras = frase.split()

    # Verificar si la frase tiene al menos tres palabras
    if len(palabras) < 3:
        return False

    # Verificar la estructura "sujeto + verbo + objeto"
    sujeto = palabras[0]
    verbo = palabras[1]
    objeto = ' '.join(palabras[2:])

    # Verificar si el verbo es válido
    verbos_validos = ["come", "baila", "lee", "canta", "estudia"]
    if verbo.lower() not in verbos_validos:
        return False

    # Imprimir el resultado del análisis
    print("Sujeto:", sujeto)
    print("Verbo:", verbo)
    print("Objeto:", objeto)
    return True

# Ejemplo de uso
frase = "Juan come pizza"
print("Frase:", frase)
resultado = analisis_semantico(frase)
if resultado:
    print("La frase tiene una estructura gramatical válida.")
else:
    print("La frase no tiene una estructura gramatical válida.")
