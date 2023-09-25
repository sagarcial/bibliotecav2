# main.py
from libro import Libro
from sede import Sede
from biblioteca import Biblioteca
from usuario import Usuario, cargar_usuarios_desde_archivo
from csv_parser import cargar_libros_desde_archivo

# Crear una instancia de la biblioteca
biblioteca = Biblioteca("Biblioteca Universitaria")

# Cargar sedes y libros desde un archivo CSV
biblioteca.biblioteca = cargar_libros_desde_archivo('libros.csv')
usuarios = cargar_usuarios_desde_archivo('usuarios.csv') 

# Listar sedes disponibles al usuario
print("Sedes disponibles:")
biblioteca.listar_sedes()

# Solicitar al usuario la sede donde desea buscar libros
nombre_sede = input("Ingresa el nombre de la sede donde deseas buscar libros: ")

# Buscar la sede
sede = biblioteca.buscar_sede(nombre_sede)

# Solicitar al usuario su código
codigo_usuario = input("Ingresa tu código de usuario: ")

# Buscar el usuario por código
usuario = None
for u in usuarios:
    if u.codigo == codigo_usuario:
        usuario = u
        break

if usuario:
    # Mostrar información del usuario
    print(f"Información del usuario:")
    print(f"Nombre: {usuario.nombre}")
    print(f"Edad: {usuario.edad}")
    print(f"Correo: {usuario.correo}")
    print(f"Tipo de usuario: {usuario.tipo_usuario}")
    print(f"Proyecto Curricular: {usuario.proyecto_curricular}")
    print(f"Facultad: {usuario.facultad}")

    if sede:
        # Listar libros disponibles en la sede seleccionada
        print(f"Libros disponibles en la sede '{nombre_sede}':")
        sede.listar_libros()

        # Solicitar al usuario el título del libro que desea alquilar
        codigo_libro = input("Ingresa el código del libro que deseas alquilar: ")


        # Alquilar el libro en la sede seleccionada
        biblioteca.alquilar_libro(usuario, codigo_libro, nombre_sede)
    else:
        print(f"No existe la sede '{nombre_sede}' en la biblioteca.")
else:
    print(f"No existe un usuario con el código '{codigo_usuario}'.")
