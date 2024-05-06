# ERICK MOISES DELGADILLO LARA
# R: 21310139 - 6E1

# Definición de la clase Actividad
class Actividad:
    def __init__(self, nombre, clima_recomendado, nivel_riesgo):
        self.nombre = nombre  # Nombre de la actividad
        self.clima_recomendado = clima_recomendado  # Clima recomendado para la actividad
        self.nivel_riesgo = nivel_riesgo  # Nivel de riesgo de la actividad

# Definición de la clase RecomendadorActividades
class RecomendadorActividades:
    def __init__(self):
        self.actividades = []  # Lista de actividades disponibles

    def agregar_actividad(self, nombre, clima_recomendado, nivel_riesgo):
        """Agrega una nueva actividad a la lista."""
        actividad = Actividad(nombre, clima_recomendado, nivel_riesgo)
        self.actividades.append(actividad)

    def recomendar_actividades(self, clima_actual):
        """Recomienda actividades basadas en el clima actual."""
        actividades_recomendadas = []
        for actividad in self.actividades:
            if clima_actual == actividad.clima_recomendado:
                actividades_recomendadas.append(actividad)
        return actividades_recomendadas

# Crear un recomendador de actividades
recomendador = RecomendadorActividades()

# Agregar algunas actividades
recomendador.agregar_actividad("Caminata", "Soleado", "Bajo")
recomendador.agregar_actividad("Ver película", "Lluvioso", "N/A")
recomendador.agregar_actividad("Navegación", "Soleado", "Alto")

# Definir el clima actual
clima_actual = "Soleado"

# Recomendar actividades basadas en el clima actual
actividades_recomendadas = recomendador.recomendar_actividades(clima_actual)

# Mostrar las actividades recomendadas
print(f"Actividades recomendadas para un día {clima_actual}:")
for actividad in actividades_recomendadas:
    print(f"- {actividad.nombre} (Riesgo: {actividad.nivel_riesgo})")
