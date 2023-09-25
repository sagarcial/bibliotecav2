# libro.py
class Libro:
    def __init__(self, codigo, titulo, autor, fecha, sede, disponible=True):
        self.codigo = codigo
        self.titulo = titulo
        self.autor = autor
        self.fecha = fecha
        self.sede = sede
        self.disponible = disponible
