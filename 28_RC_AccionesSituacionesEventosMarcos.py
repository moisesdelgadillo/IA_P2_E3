# ERICK MOISES DELGADILLO LARA
# R: 21310139 - 6E1

# Definición de la clase Evento
class Evento:
    def __init__(self, nombre, fecha, hora, lugar):
        self.nombre = nombre  # Nombre del evento
        self.fecha = fecha  # Fecha del evento
        self.hora = hora  # Hora del evento
        self.lugar = lugar  # Lugar del evento

# Definición de la clase PlanificadorEventos
class PlanificadorEventos:
    def __init__(self):
        self.eventos = []  # Lista de eventos planificados

    def planificar_evento(self, nombre, fecha, hora, lugar):
        """Planifica un nuevo evento."""
        evento = Evento(nombre, fecha, hora, lugar)
        self.eventos.append(evento)

    def buscar_evento_por_fecha(self, fecha):
        """Busca eventos planificados para una fecha específica."""
        eventos_encontrados = []
        for evento in self.eventos:
            if evento.fecha == fecha:
                eventos_encontrados.append(evento)
        return eventos_encontrados

# Crear un planificador de eventos
planificador_eventos = PlanificadorEventos()

# Planificar algunos eventos
planificador_eventos.planificar_evento("Fiesta de cumpleaños", "2024-05-20", "19:00", "Casa de Juan")
planificador_eventos.planificar_evento("Reunión de trabajo", "2024-05-25", "09:00", "Oficina")
planificador_eventos.planificar_evento("Concierto en el parque", "2024-05-30", "20:00", "Parque Central")

# Buscar eventos por fecha
fecha_busqueda = "2024-05-25"
eventos_encontrados = planificador_eventos.buscar_evento_por_fecha(fecha_busqueda)

# Mostrar los eventos encontrados
print(f"Eventos para la fecha '{fecha_busqueda}':")
for evento in eventos_encontrados:
    print(f"Nombre: {evento.nombre}, Hora: {evento.hora}, Lugar: {evento.lugar}")
