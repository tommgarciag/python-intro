# Polimorfismo se refiere a la habilidad de objetos de distintas clases de responder al mismo mensaje.

# Encapsulación La encapsulación se refiere a impedir el acceso a determinados métodos y atributos de los objetos estableciendo así qué puede utilizarse desde fuera de la clase.  Si el nombre comienza con dos guiones bajos (y no termina también con dos guiones bajos) se trata de una variable o función privada, en caso contrario es pública. Los métodos cuyo nombre comienza y termina con dos guiones bajos son métodos especiales que Python llama automáticamente bajo ciertas circunstancias.

class Ejemplo:
    def publico(self):
        print ("Publico") 

    def __privado(self):
        print ("Privado")

 

ej = Ejemplo()

ej.publico()

# ej.privado() # error
ej._Ejemplo__privado() # trampa


