# ERICK MOISES DELGADILLO LARA
# R: 21310139 - 6E1

# Función para resolver un rompecabezas de Sudoku utilizando backtracking
def resolver_sudoku(tablero):
    """Resuelve un rompecabezas de Sudoku utilizando backtracking."""
    # Busca una celda vacía en el tablero
    celda_vacia = encontrar_celda_vacia(tablero)
    # Si no hay celdas vacías, el Sudoku está resuelto
    if not celda_vacia:
        return True
    fila, columna = celda_vacia
    # Intenta colocar un número del 1 al 9 en la celda vacía
    for numero in range(1, 10):
        if es_numero_valido(tablero, fila, columna, numero):
            tablero[fila][columna] = numero
            # Realiza una llamada recursiva para resolver el Sudoku
            if resolver_sudoku(tablero):
                return True
            # Si no se puede resolver con este número, retrocede y prueba otro
            tablero[fila][columna] = 0
    # Si ningún número es válido, la solución no es posible
    return False

# Función para encontrar una celda vacía en el tablero de Sudoku
def encontrar_celda_vacia(tablero):
    """Encuentra una celda vacía en el tablero de Sudoku."""
    for fila in range(9):
        for columna in range(9):
            if tablero[fila][columna] == 0:
                return (fila, columna)
    return None

# Función para verificar si un número dado es válido en una celda específica
def es_numero_valido(tablero, fila, columna, numero):
    """Verifica si un número dado es válido en una celda específica."""
    # Verifica si el número ya está en la fila
    if numero in tablero[fila]:
        return False
    # Verifica si el número ya está en la columna
    for i in range(9):
        if tablero[i][columna] == numero:
            return False
    # Verifica si el número ya está en el cuadrante 3x3
    fila_inicio, columna_inicio = 3 * (fila // 3), 3 * (columna // 3)
    for i in range(fila_inicio, fila_inicio + 3):
        for j in range(columna_inicio, columna_inicio + 3):
            if tablero[i][j] == numero:
                return False
    return True

# Ejemplo de uso
tablero_sudoku = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

print("Tablero de Sudoku sin resolver:")
for fila in tablero_sudoku:
    print(fila)

if resolver_sudoku(tablero_sudoku):
    print("\nTablero de Sudoku resuelto:")
    for fila in tablero_sudoku:
        print(fila)
else:
    print("\nNo se pudo resolver el Sudoku.")
