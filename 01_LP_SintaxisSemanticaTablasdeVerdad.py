# ERICK MOISES DELGADILLO LARA
# R: 21310139 - 6E1

# Función para generar las combinaciones de valores booleanos para las variables
def generar_combinaciones(variables):
    """Genera todas las combinaciones posibles de valores booleanos para las variables dadas."""
    if not variables:
        return [[]]
    resto = generar_combinaciones(variables[1:])
    return [[valor] + resto_elemento for valor in [True, False] for resto_elemento in resto]

# Función para evaluar una expresión lógica dada una asignación de valores a las variables
def evaluar_expresion(expresion, asignacion):
    """Evalúa una expresión lógica dada una asignación de valores a las variables."""
    return eval(expresion, asignacion)

# Función para generar y mostrar la tabla de verdad de una expresión lógica
def tabla_verdad(expresion, variables):
    """Genera y muestra la tabla de verdad de la expresión lógica."""
    # Generar todas las combinaciones de valores booleanos para las variables
    combinaciones = generar_combinaciones(variables)
    
    # Encabezado de la tabla
    encabezado = " | ".join(variables + [expresion])
    print(encabezado)
    print("-" * len(encabezado))
    
    # Filas de la tabla
    for asignacion in combinaciones:
        valores = [str(valor) for valor in asignacion]
        valores.append(str(evaluar_expresion(expresion, dict(zip(variables, asignacion)))))
        fila = " | ".join(valores)
        print(fila)

# Ejemplo de uso
expresion_logica = "(p and q) or (not p and not q)"
variables = ["p", "q"]
tabla_verdad(expresion_logica, variables)
