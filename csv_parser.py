# csv_parser.py
import csv
from libro import Libro
from sede import Sede

def cargar_libros_desde_archivo(archivo):
    biblioteca = {}

    with open(archivo, mode='r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            sede_nombre = row['Sede']
            codigo = row['Codigo']  # Agregamos la columna 'Codigo' al archivo CSV
            titulo = row['Titulo']
            autor = row['Autor']
            fecha = row['Fecha']

            # Verificar si la sede ya existe en la biblioteca
            if sede_nombre not in biblioteca:
                sede = Sede(sede_nombre)
                biblioteca[sede_nombre] = sede
            else:
                sede = biblioteca[sede_nombre]

            disponible = True  # Por defecto, los libros están disponibles al cargarlos
            libro = Libro(codigo, titulo, autor, fecha, sede, disponible)
            sede.agregar_libro(libro)

    return biblioteca

