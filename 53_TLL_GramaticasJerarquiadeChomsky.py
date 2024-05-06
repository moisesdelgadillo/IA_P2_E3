# ERICK MOISES DELGADILLO LARA
# R: 21310139 - 6E1

# Definición de las gramáticas de la jerarquía de Chomsky
gramatica_tipo_0 = "S -> AB | a | b\nA -> a\nB -> b"
gramatica_tipo_1 = "S -> AB | a | b\nA -> a | aA\nB -> b"
gramatica_tipo_2 = "S -> AB | a\nA -> aA | a\nB -> b"
gramatica_tipo_3 = "S -> aA | b\nA -> aS | bS | ε"

# Función para imprimir el tipo de gramática
def imprimir_tipo_gramatica(gramatica):
    if "->" in gramatica:
        print("La gramática es de tipo 0.")
    elif "ε" in gramatica:
        print("La gramática es de tipo 3.")
    elif "S" in gramatica:
        if "A" in gramatica:
            print("La gramática es de tipo 2.")
        else:
            print("La gramática es de tipo 1.")
    else:
        print("La gramática no pertenece a la jerarquía de Chomsky.")

# Imprimir el tipo de gramática para cada una de las gramáticas definidas
print("Gramática 1:")
print(gramatica_tipo_0)
imprimir_tipo_gramatica(gramatica_tipo_0)

print("\nGramática 2:")
print(gramatica_tipo_1)
imprimir_tipo_gramatica(gramatica_tipo_1)

print("\nGramática 3:")
print(gramatica_tipo_2)
imprimir_tipo_gramatica(gramatica_tipo_2)

print("\nGramática 4:")
print(gramatica_tipo_3)
imprimir_tipo_gramatica(gramatica_tipo_3)
