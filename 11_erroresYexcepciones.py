def division(a, b):
    return a / b
 
def calcular():
    division(1, 0)
 
# calcular() # ZeroDivisionError: divison by zero

# En Python se utiliza una construcción try-except para capturar y tratar las excepciones. El bloque try (intentar) define el fragmento de código en el que creemos que podría producirse una excepción. El bloque except (excepción) permite indicar el tratamiento que se llevará a cabo de producirse dicha excepción. 

try:
    f = file("archivo.txt")

except:
    print ("El archivo no existe")


# Python permite utilizar varios except para un solo bloque try, de forma que podamos dar un tratamiento distinto a la excepción dependiendo del tipo de excepción de la que se trate. Cuando se lanza una excepción en el bloque try, se busca en cada una de las clausulas except un manejador adecuado para el tipo de error que se produjo. En caso de que no se encuentre, se propaga la excepción.

try:
    num = int("3a")
    print ("no_existe")

except NameError:
    print ("La variable no existe")

except ValueError:
    print ("El valor no es un numero")


# Además podemos hacer que un mismo except sirva para tratar más de una excepción usando una tupla para listar los tipos de error que queremos que trate el bloque:

try:
    num = int("3a")
    print ("no_existe")

except (NameError, ValueError):
    print ("Ocurrio un error")


# La construcción try-except puede contar además con una clausula else, que define un fragmento de código a ejecutar sólo si no se ha producido ninguna excepción en el try.

try:
    num = 33

except:
    print("Hubo un error!")

else:
    print ("Todo esta bien")


# También existe una clausula finally que se ejecuta siempre, se produzca o no una excepción. Esta clausula se suele utilizar, entre otras cosas, para tareas de limpieza.

try:
    z = 7 / 0

except ZeroDivisionError:
    print ("Division por cero")

finally:
    print ("Limpiando")

# También podemos crear y lanzar nuestras propias excepciones. Basta crear una clase que herede de Exception o cualquiera de sus hijas y lanzarla con raise.


# VER

