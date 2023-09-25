# biblioteca.py
class Biblioteca:
    def __init__(self, nombre):
        self.nombre = nombre
        self.biblioteca = {}

    def agregar_sede(self, sede):
        self.biblioteca[sede.nombre] = sede

    def listar_sedes(self):
        for nombre_sede in self.biblioteca.keys():
            print(nombre_sede)

    def buscar_sede(self, nombre_sede):
        return self.biblioteca.get(nombre_sede)

    def alquilar_libro(self, usuario, codigo_libro, nombre_sede):
        sede = self.buscar_sede(nombre_sede)
        if sede:
            libro = sede.buscar_libro_por_codigo(codigo_libro)
            if libro:
                if libro.disponible:
                    libro.disponible = False
                    print(f"{usuario.nombre} ha alquilado '{libro.titulo}' en la sede '{nombre_sede}'")
                else:
                    print(f"'{libro.titulo}' no está disponible actualmente en la sede '{nombre_sede}'.")
            else:
                print(f"No existe un libro con el código '{codigo_libro}' en la sede '{nombre_sede}'.")
        else:
            print(f"No existe la sede '{nombre_sede}' en la biblioteca.")