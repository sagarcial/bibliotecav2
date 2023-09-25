# sede.py

class Sede:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)
    def buscar_libro_por_codigo(self, codigo_libro):
        for libro in self.libros:
            if libro.codigo == codigo_libro:
                return libro
        return None
    def listar_libros(self):
        for libro in self.libros:
            estado = "Disponible" if libro.disponible else "No Disponible"
            print(f"{libro.titulo} - {libro.autor} ({libro.fecha}) - {estado} - {libro.codigo}")
