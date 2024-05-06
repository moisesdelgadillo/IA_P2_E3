# ERICK MOISES DELGADILLO LARA
# R: 21310139 - 6E1

# Definición de la clase Libro
class Libro:
    def __init__(self, titulo, autor, categoria):
        self.titulo = titulo  # Título del libro
        self.autor = autor  # Autor del libro
        self.categoria = categoria  # Categoría del libro

# Definición de la clase Biblioteca
class Biblioteca:
    def __init__(self):
        self.libros = []  # Lista de libros en la biblioteca

    def agregar_libro(self, titulo, autor, categoria):
        """Agrega un nuevo libro a la biblioteca."""
        libro = Libro(titulo, autor, categoria)
        self.libros.append(libro)

    def buscar_libros_por_categoria(self, categoria):
        """Busca libros en la biblioteca por categoría."""
        libros_encontrados = []
        for libro in self.libros:
            if libro.categoria == categoria:
                libros_encontrados.append(libro)
        return libros_encontrados

# Crear una biblioteca
biblioteca = Biblioteca()

# Agregar algunos libros a la biblioteca
biblioteca.agregar_libro("Cien años de soledad", "Gabriel García Márquez", "Ficción")
biblioteca.agregar_libro("El señor de los anillos", "J.R.R. Tolkien", "Ficción")
biblioteca.agregar_libro("Breve historia del tiempo", "Stephen Hawking", "No ficción")
biblioteca.agregar_libro("La metamorfosis", "Franz Kafka", "Ficción")

# Buscar libros por categoría
categoria_busqueda = "Ficción"
libros_encontrados = biblioteca.buscar_libros_por_categoria(categoria_busqueda)

# Mostrar los libros encontrados
print(f"Libros en la categoría '{categoria_busqueda}':")
for libro in libros_encontrados:
    print(f"Título: {libro.titulo}, Autor: {libro.autor}")
