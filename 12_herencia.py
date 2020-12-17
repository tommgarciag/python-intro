# heredar de una clase también se le llama a menudo “extender una clase”, extender de una clase "padre" (superclase) sus atributos y metodos a otra clase "hija" (subclase).

# Para indicar que una clase hereda de otra se coloca el nombre de la clase de la que se hereda entre paréntesis después del nombre de la clase.

# Ej: modelar los instrumentos musicales de una banda

class Instrumento:
    def __init__(self,precio):
        self.precio = precio

    def tocar(self):
        print("Estamos tocando música...")

    def romper(self):
        print("Ups, el que lo rompe la paga...")
        print("Son $%d ." %self.precio)


class Bateria(Instrumento):
    pass

class Guitarra(Instrumento):
    pass

# Como Bateria y Guitarra heredan de Instrumento, ambos tienen un método tocar() y un método romper(), y se inicializan pasando un parámetro precio.


# Herencia múltiple: una clase puede heredar de varias clases a la vez. Basta con enumerar las clases de las que se hereda separándolas por comas.

class Terrestre:
    def caminar(self):
        print("Caminando...")

class Acuatico:    
    def nadar(self):
        print("Nadando...") 

class Cocodrilo(Terrestre, Acuatico):
    pass

# coco = Cocodrilo()
# coco.nadar()
# coco.caminar()


class Vehiculo:
    marca=""
    modelo=""
    anio=0

    def __init__(self, marca, modelo, anio):
        self.marca=marca
        self.modelo=modelo
        self.anio=anio

    def __str__(self):
        return ("Marca: %s \t Modelo: %s \t Año: %s" %(self.marca, self.modelo, self.anio))

    def arrancar(self):
        return "Run run..."


class Auto(Vehiculo): # Auto herada de Vehiculo sus atributos y metodos
    cantPuertas=0
    
    def __init__(self, marca, modelo, anio, cantPuertas):
        super().__init__(marca, modelo, anio)
        self.cantPuertas=cantPuertas

    def __str__(self):
        return super().__str__() + (" \t Cant. de puertas: %d" %self.cantPuertas)



auto1 = Auto("Ford","Ranger", 2019, 4)
# print(auto1)

class Barco: 
    eslora=0
    manga=0
    calado=0

    def __init__(self, eslora, manga, calado):
        self.eslora=eslora
        self.manga=manga
        self.calado=calado

    def __str__(self):
        return ("Eslora: %d \t Manga: %d \t Calado: %d" %(self.eslora, self.manga, self.calado))

    def amarrar(self):
        return "Amarrando..."

    def setCalado(self,calado):
        self.calado=calado

    def getCalado(self):
        return ("Calado: %d" %self.calado)

'''
barco1=Barco(20,2,0)
print(barco1)
barco1.setCalado(2)
print(barco1)
print(barco1.getCalado())
'''

class Anfibio(Auto, Barco):
    def __init__(self, marca, modelo, anio, cantPuertas, eslora, manga, calado):
        Auto.__init__(self, marca, modelo, anio, cantPuertas)
        Barco.__init__(self, eslora, manga, calado)

    def __str__(self):
        return Auto.__str__(self) + "\t" + Barco.__str__(self)

anfibio1 = Anfibio("Yamaha", "ANF1", 2020, 4, 20, 3, 1)
print(anfibio1)
anfibio1.setCalado(5)
print(anfibio1.getCalado())