# ERICK MOISES DELGADILLO LARA
# R: 21310139 - 6E1

def unificar(exp1, exp2):
    # Si las expresiones son idénticas, la unificación es exitosa y la sustitución es vacía
    if exp1 == exp2:
        return {}

    # Si una de las expresiones es una variable, la unificación es exitosa y la variable se sustituye por la otra expresión
    if es_variable(exp1):
        return {exp1: exp2}
    if es_variable(exp2):
        return {exp2: exp1}

    # Si ambas expresiones son funciones, las descomponemos en símbolo y argumentos
    if es_funcion(exp1) and es_funcion(exp2):
        simbolo1, args1 = descomponer_funcion(exp1)
        simbolo2, args2 = descomponer_funcion(exp2)
        # Si los símbolos son diferentes, la unificación falla
        if simbolo1 != simbolo2 or len(args1) != len(args2):
            return None
        # Realizamos la unificación recursiva de los argumentos
        sustituciones = {}
        for arg1, arg2 in zip(args1, args2):
            sust = unificar(arg1, arg2)
            if sust is None:
                return None
            sustituciones.update(sust)
        return sustituciones

    # Si ninguna de las condiciones anteriores se cumple, la unificación falla
    return None

# Funciones de ayuda para verificar si una expresión es una variable o una función
def es_variable(exp):
    return isinstance(exp, str) and exp.islower()

def es_funcion(exp):
    return isinstance(exp, tuple)

def descomponer_funcion(exp):
    return exp[0], exp[1:]

# Ejemplo de unificación
expresion1 = ('padre', 'Juan', 'Pedro')
expresion2 = ('padre', 'Juan', 'x')
sustitucion = unificar(expresion1, expresion2)
print("Sustitución:", sustitucion)
