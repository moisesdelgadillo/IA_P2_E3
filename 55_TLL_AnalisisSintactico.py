# ERICK MOISES DELGADILLO LARA
# R: 21310139 - 6E1

# Definición de tokens para el análisis léxico
TOKEN_ENTERO = 'ENTERO'
TOKEN_SUMA = 'SUMA'
TOKEN_RESTA = 'RESTA'
TOKEN_MULTIPLICACION = 'MULTIPLICACION'
TOKEN_DIVISION = 'DIVISION'
TOKEN_PARENTESIS_IZQ = 'PARENTESIS_IZQ'
TOKEN_PARENTESIS_DER = 'PARENTESIS_DER'
TOKEN_FIN_DE_EXPRESION = 'FIN_DE_EXPRESION'

# Función para tokenizar la entrada
def analizador_lexico(expresion):
    tokens = []
    i = 0
    while i < len(expresion):
        char = expresion[i]
        if char.isdigit():
            num = char
            while i + 1 < len(expresion) and expresion[i + 1].isdigit():
                num += expresion[i + 1]
                i += 1
            tokens.append((TOKEN_ENTERO, int(num)))
        elif char == '+':
            tokens.append((TOKEN_SUMA, char))
        elif char == '-':
            tokens.append((TOKEN_RESTA, char))
        elif char == '*':
            tokens.append((TOKEN_MULTIPLICACION, char))
        elif char == '/':
            tokens.append((TOKEN_DIVISION, char))
        elif char == '(':
            tokens.append((TOKEN_PARENTESIS_IZQ, char))
        elif char == ')':
            tokens.append((TOKEN_PARENTESIS_DER, char))
        elif char.isspace():
            pass  # Ignorar los espacios en blanco
        else:
            raise ValueError("Carácter no reconocido: {}".format(char))
        i += 1
    tokens.append((TOKEN_FIN_DE_EXPRESION, None))
    return tokens

# Función para el análisis sintáctico
def analizador_sintactico(tokens):
    token_actual = 0

    # Funciones para cada regla gramatical
    def expresion():
        resultado = termino()
        while tokens[token_actual][0] in (TOKEN_SUMA, TOKEN_RESTA):
            if tokens[token_actual][0] == TOKEN_SUMA:
                match(TOKEN_SUMA)
                resultado += termino()
            elif tokens[token_actual][0] == TOKEN_RESTA:
                match(TOKEN_RESTA)
                resultado -= termino()
        return resultado

    def termino():
        resultado = factor()
        while tokens[token_actual][0] in (TOKEN_MULTIPLICACION, TOKEN_DIVISION):
            if tokens[token_actual][0] == TOKEN_MULTIPLICACION:
                match(TOKEN_MULTIPLICACION)
                resultado *= factor()
            elif tokens[token_actual][0] == TOKEN_DIVISION:
                match(TOKEN_DIVISION)
                resultado /= factor()
        return resultado

    def factor():
        token = tokens[token_actual]
        if token[0] == TOKEN_ENTERO:
            match(TOKEN_ENTERO)
            return token[1]
        elif token[0] == TOKEN_PARENTESIS_IZQ:
            match(TOKEN_PARENTESIS_IZQ)
            resultado = expresion()
            match(TOKEN_PARENTESIS_DER)
            return resultado
        else:
            raise SyntaxError("Factor inválido")

    # Función para emparejar el token actual con el tipo esperado
    def match(tipo):
        nonlocal token_actual
        if tokens[token_actual][0] == tipo:
            token_actual += 1
        else:
            raise SyntaxError("Se esperaba {}".format(tipo))

    # Llamar a la función de inicio y devolver el resultado del análisis
    return expresion()

# Ejemplo de uso
expresion = "3 + 4 * (10 - 2)"
print("Expresión:", expresion)
tokens = analizador_lexico(expresion)
print("Tokens:", tokens)
resultado = analizador_sintactico(tokens)
print("Resultado del análisis sintáctico:", resultado)
