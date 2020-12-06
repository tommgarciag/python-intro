# importo el metodo que permite extraer un atributo de una clase y utilizarlo como clave para ordenar: attrgetter

from operator import attrgetter 



# creo la clase alumno

class Alumno:
    nombre = ""
    apellido = ""
    legajo = 0
    edad = 0
    materias = 0

    def __init__(self, nombre, apellido, legajo, edad, materias):
        self.nombre = nombre
        self.apellido = apellido
        self.legajo = legajo
        self.edad = edad
        self.materias = materias

    def __str__(self):
        return ("%s %s %d %d %d") %(self.nombre, self.apellido, self.legajo, self.edad, self.materias)

# Programa principal

curso = []

for i in range(0,2):
    nombre = input("Nombre del alumno: ")
    apellido = input("Apellido del alumno: ")
    legajo = int(input("Legajo del alumno: "))
    edad = int(input("Edad del alumno: "))
    materias = int(input("Materias en curso del alumno: "))
    alumno = Alumno(nombre, apellido, legajo, edad, materias)
    curso.append(alumno)

    
for i in range(0,2):
    print(curso[i])

curso.sort(key=attrgetter("legajo"))
print()
for i in range(0,2):
    print(curso[i])

