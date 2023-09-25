# usuario.py
import csv

class Usuario:
    def __init__(self, nombre, edad, correo, tipo_usuario, proyecto_curricular, facultad, codigo):
        self.nombre = nombre
        self.edad = edad
        self.correo = correo
        self.tipo_usuario = tipo_usuario
        self.proyecto_curricular = proyecto_curricular
        self.facultad = facultad
        self.codigo = codigo

class Admin(Usuario):
    def __init__(self, nombre, edad, correo, proyecto_curricular, facultad, codigo):
        super().__init__(nombre, edad, correo, "Admin", proyecto_curricular, facultad, codigo)

class Estudiante(Usuario):
    def __init__(self, nombre, edad, correo, proyecto_curricular, facultad, codigo):
        super().__init__(nombre, edad, correo, "Estudiante", proyecto_curricular, facultad, codigo)

class Profesor(Usuario):
    def __init__(self, nombre, edad, correo, proyecto_curricular, facultad, codigo):
        super().__init__(nombre, edad, correo, "Profesor", proyecto_curricular, facultad, codigo)

# Función para cargar usuarios desde un archivo CSV
def cargar_usuarios_desde_archivo(archivo):
    usuarios = []

    with open(archivo, mode='r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            tipo_usuario = row['TipoUsuario']
            nombre = row['Nombre']
            edad = row['Edad']
            correo = row['Correo']
            proyecto_curricular = row['ProyectoCurricular']
            facultad = row['Facultad']
            codigo = row['Codigo']

            if tipo_usuario == "Admin":
                usuario = Admin(nombre, edad, correo, proyecto_curricular, facultad, codigo)
            elif tipo_usuario == "Estudiante":
                usuario = Estudiante(nombre, edad, correo, proyecto_curricular, facultad, codigo)
            elif tipo_usuario == "Profesor":
                usuario = Profesor(nombre, edad, correo, proyecto_curricular, facultad, codigo)
            else:
                usuario = Usuario(nombre, edad, correo, tipo_usuario, proyecto_curricular, facultad, codigo)

            usuarios.append(usuario)

    return usuarios
