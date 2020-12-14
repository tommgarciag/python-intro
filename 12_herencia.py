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

coco = Cocodrilo()
coco.nadar()
coco.caminar()