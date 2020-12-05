class Alumno:
    legajo=0
    nombre=""
    apellido=""
    dni=0

    def __init__(self, legajo, nombre, apellido, dni):
        self.legajo = legajo
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni

    def __str__(self):
        return ("Nro de legajo: %d Nombre: %s %s DNI: %d") %(self.legajo,self.nombre,self.apellido,self.dni)



miAlumno = Alumno(1,"Tomas", "Garcia", 36181853) # 1er instancia 

print(miAlumno.legajo)
print(miAlumno.nombre)
print(miAlumno.apellido)
print(miAlumno.dni)
print(miAlumno.__str__())

legajo=int(input("Ingrese nro de legajo: "))
nombre=input("Ingrese el nombre: ")
apellido=input("Ingrese el apellido: ")
dni=int(input("Ingrese el DNI: "))

miAlumno2 = Alumno(legajo,nombre,apellido,dni)
print(miAlumno2.__str__())