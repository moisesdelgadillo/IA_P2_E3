# ERICK MOISES DELGADILLO LARA
# R: 21310139 - 6E1

# Función para verificar la equivalencia entre dos expresiones lógicas
def verificar_equivalencia(expresion1, expresion2):
    """Verifica si dos expresiones lógicas son equivalentes."""
    return expresion1 == expresion2

# Función para verificar la validez de una expresión lógica
def verificar_validez(expresion):
    """Verifica si una expresión lógica es válida."""
    return all([eval(expresion, {}, asignacion) for asignacion in generar_asignaciones(expresion)])

# Función para verificar la satisfacibilidad de una expresión lógica
def verificar_satisfacibilidad(expresion):
    """Verifica si una expresión lógica es satisfacible."""
    return any([eval(expresion, {}, asignacion) for asignacion in generar_asignaciones(expresion)])

# Función para generar todas las asignaciones posibles de valores booleanos a las variables en una expresión
def generar_asignaciones(expresion):
    """Genera todas las asignaciones posibles de valores booleanos a las variables en una expresión."""
    variables = obtener_variables(expresion)
    if not variables:
        return [{}]
    resto = generar_asignaciones(expresion.replace(variables[0], ''))
    return [{variables[0]: valor, **resto_elemento} for valor in [True, False] for resto_elemento in resto]

# Función para obtener todas las variables en una expresión lógica
def obtener_variables(expresion):
    """Obtiene todas las variables en una expresión lógica."""
    return list(set([caracter for caracter in expresion if caracter.isalpha()]))

# Ejemplo de uso
expresion1 = "(p and q) or (not p and not q)"
expresion2 = "(not p) or (not q)"
print("Expresión 1:", expresion1)
print("Expresión 2:", expresion2)
print()

# Verificar equivalencia
if verificar_equivalencia(expresion1, expresion2):
    print("Las expresiones son equivalentes.")
else:
    print("Las expresiones no son equivalentes.")

# Verificar validez de la expresión 1
print("La expresión 1 es válida." if verificar_validez(expresion1) else "La expresión 1 no es válida.")

# Verificar satisfacibilidad de la expresión 2
print("La expresión 2 es satisfacible." if verificar_satisfacibilidad(expresion2) else "La expresión 2 no es satisfacible.")
