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

# Función para imprimir los tokens
def imprimir_tokens(tokens):
    for token in tokens:
        print(token)

# Ejemplo de uso
expresion = "3 + 4 * (10 - 2)"
print("Expresión:", expresion)
tokens = analizador_lexico(expresion)
print("Tokens:")
imprimir_tokens(tokens)
