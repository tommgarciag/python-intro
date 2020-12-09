# Ejercicios Adicionales Python Funciones.


# 1. Escribir una función que reciba dos números y devuelva su producto.


def multiplicar(n1,n2):
    return n1*n2

# print(multiplicar(2,3))

#2. Utilizando la función del ejercicio anterior, escribir un programa #(un archivo .py) que pida al usuario dos números, y luego muestre el producto.
'''
num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese un segundo numero: "))

print("%d x %d = %d"  %(num1,num2,multiplicar(num1,num2)))
'''
#3. Escribir funciones que permitan:


# a) Calcular el perímetro de un rectángulo dada su base y su altura.

def perimetroRectangulo(base,altura):
    return 2 * (altura+base)

# print(perimetroRectangulo(10,4))

# b) Calcular el área de un rectángulo dada su base y su altura.

def areaRectangulo(base,altura):
    return base * altura

# print(areaRectangulo(5,2))

# c) Calcular el perímetro de un círculo dado su radio.
import math
pi = math.pi
sqrt = math.sqrt

def perimetroCirculo(radio):    
    return round((2 * pi * radio), 2)

# print(perimetroCirculo(5))

# e) Calcular el área de un círculo dado su radio.

def areaCirculo(radio):
    return round((pi * radio**2),2)

# print(areaCirculo(5))

# f) Calcular el volumen de una esfera dado su radio.

def volumenEsfera(radio):
    return round((4/3 * pi) * (radio**3),2)

# print(volumenEsfera(5))


# g) Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.

def hipotenusa(a,b):
    return sqrt((a**2) + (b**2))

# print(hipotenusa(4,3))

# 4. Analizar los siguientes bloques de código. ¿Cuál será el resultado de ejecutarlos?

# Verificar la respuesta con el intérprete.
#for i in range(5):
#    print(i * i)

''' 
output: 

    0 * 0 = 0
    1 * 1 = 1  
    2 * 2 = 4
    3 * 3 = 9
    4 * 4 = 16
'''

#for i in range(2, 6):
#   print(i, 2 ** i)

'''
output:    
    2, 4
    3, 8
    4, 16
    5, 32    
'''


 

# 5. Escribir una función que, dado un número entero n, permita calcular su factorial

'''
def factorialRecursivo(n):
    if n==1:
        return 1
    else:
        return n*(factorialRecursivo(n-1))

factorial = int(input("Ingrese un numero entera para calcular su factorial: "))
print(factorialRecursivo(factorial))
'''

# 6. Escribir funciones que resuelvan los siguientes problemas:
#a) Dados dos números, imprimir la suma, resta, división y multiplicación de ambos.

def sumar(a,b):
    return a +b

# print(sumar(10,2))

def restar(a,b):
    return a -b

# print(restar(10,2))

# print(multiplicar(10,2))

def dividir(a,b):
    return a//b

# print(dividir(10,2))


#b) Dado un número entero n, imprimir su tabla de multiplicar.

def tablaMultiplicar(n):
    for i in range(1,11):
        print(i * n)

# tablaMultiplicar(5)

# 7. Escribir un programa que le pida una palabra al usuario, para luego imprimirla 1000 veces, en una única línea, con espacios intermedios.
#Ayuda: Investigar acerca del parámetro end de la función print.


def imprimirMilVeces(palabra):
    for i in range(1,1001):
        print(palabra, end=" ")

# palabra = input("Ingrese un palabra: ")
# imprimirMilVeces(palabra)


#8. a) Escribir una función que dado un número entero devuelva 1 si el mismo es impar y 0 si fuera par.

def parImpar(n):
    if n%2==0:
        print(0)
    else:
        print(1)

# parImpar(3)
# parImpar(6)

# b) Escribir una función que dado un número entero devuelva el dígito de las unidades. Por ejemplo, para 153 debe devolver 3.

def digitos(n):
    n = str(n)
    return len(n)

# print(digitos(311))


# c) Escribir una función que dado un número devuelva el primer número múltiplo de 10 inferior a él. Por ejemplo, para 153 debe devolver 150.

def multiploDiezInferior(n):
    for i in range(n,1,-1):
        if i%10==0:
            print(i)
            break

# multiploDiezInferior(153)


# 9. Escribir un programa que imprima todos los números pares entre dos números que se le pidan al usuario.

def pares(a,b):
    for i in range(a,b,1):
        if i%2==0:
            print(i)

# pares(3,15)


# 10. Escribir un programa que le pregunte al usuario un número n e imprima los primeros n números triangulares, junto con su índice. Los números triangulares se obtienen mediante la suma de los números naturales desde 1 hasta n. Es decir, si se piden los primeros 5 números triangulares, el programa debe imprimir:
'''
1 - 1
2 - 3
3 - 6
4 - 10
5 - 15
'''

def triangulares(n):
    triangular = 0
    for i in range(1,n+1):
        triangular += i
        print(i, triangular)

# triangulares(5)

# 11. Escribir un programa que tome una cantidad m de valores ingresados por el usuario, a cada uno le calcule el factorial (utilizando la función escrita en el ejercicio de factorial e imprima el resultado junto con el número de orden correspondiente.



# 12. Escribir un programa que imprima por pantalla todas las fichas de dominó, de una por línea y sin repetir.



# 13. Modificar el programa anterior para que pueda generar fichas de un juego que puede tener números de 0 a n.



# 14. Escribir dos funciones que permitan calcular:
#a) La duración en segundos de un intervalo dado en horas, minutos y segundos.


# b) La duración en horas, minutos y segundos de un intervalo dado en segundos.


# 15. Usando las funciones del ejercicio anterior, escribir un programa que pida al usuario dos intervalos expresados en horas, minutos y segundos, sume sus duraciones, y muestre por pantalla la duración total en horas, minutos y segundos.

# 16. Escribir una función que reciba por parámetro una dimensión n, e imprima la matriz identidad correspondiente a esa dimensión.


# 17. Escribir funciones que resuelvan los siguientes problemas:

#a) Dado un año indicar si es bisiesto.

#Nota: un año es bisiesto si es un número divisible por 4, pero no si es divisible por 100, excepto que también sea divisible por 400.

# b) Dado un mes y un año, devolver la cantidad de días correspondientes.
# c) Dada una fecha (día, mes, año), indicar si es válida o no.
# d) Dada una fecha, indicar los días que faltan hasta fin de mes.
# e) Dada una fecha, indicar los días que faltan hasta fin de año.
# f) Dada una fecha, indicar la cantidad de días transcurridos en ese año hasta esa fecha.
# g) Dadas dos fechas (día1, mes1, año1, día2, mes2, año2), indicar el tiempo transcurrido entre ambas, en años, meses y días.

# Nota: en todos los casos, invocar las funciones escritas previamente cuando sea posible.


# 18. Suponiendo que el primer día del año fue lunes, escribir una función que reciba un número con el día del año (de 1 a 366) y devuelva el día de la semana que le toca. Por ejemplo: si recibe '3' debe devolver 'miércoles', si recibe '9' debe devolver 'martes'.


# 19. Escribir un programa que reciba como entrada un entero representando un año (por ejemplo 751, 1999, o 2158), y muestre por pantalla el mismo año escrito en números romanos.


# 20. Programa de astrología: el usuario debe ingresar el día y mes de su cumpleaños y el programa le debe decir a qué signo corresponde.
'''
Acuario: 21 de enero al 20 de febrero.
Piscis: 21 de febrero al 20 de marzo.
Aries: 21 de marzo al 20 de abril.
Tauro: 21 de abril al 20 de mayo.
Geminis: 21 de mayo al 20 de junio.
Cancer: 21 de junio al 20 de julio.
Leo: 21 de julio al 20 de agosto.
Virgo: 21 de agosto al 20 de septiembre.
Libra: 21 de septiembre al 20 de octubre.
Escorpio: 21 de octubre al 20 de noviembre.
Sagitario: 21 de noviembre al 20 de diciembre.
Capricornio: 21 de diciembre al 20 de enero.
'''


# 21. Escribir un programa que permita al usuario ingresar un conjunto de notas, preguntando a cada paso si desea ingresar más notas, e imprimiendo el promedio correspondiente.


# 22. Escribir una función que reciba un número entero k e imprima su descomposición en factores primos.

# 23. Manejo de contraseñas

# a) Escribir un programa que contenga una contraseña inventada, que le pregunte al usuario la contraseña, y no le permita continuar hasta que la haya ingresado correctamente.

# b) Modificar el programa anterior para que solamente permita una cantidad fija de intentos.

# c) Modificar el programa anterior para que después de cada intento agregue una pausa cada vez mayor, utilizando la función sleep del módulo time.

# d) Modificar el programa anterior para que sea una función que devuelva si el usuario ingresó o no la contraseña correctamente, mediante un valor booleano (True o False).


# 24. Números perfectos y números amigos

# a) Escribir una función que devuelva la suma de todos los divisores de un número n, sin incluirlo.

# b) Usando la función anterior, escribir una función que imprima los primeros m números tales que la suma de sus divisores sea igual a sí mismo (es decir los primeros m números perfectos).

# c) Usando la primera función, escribir una función que imprima las primeras m parejas de números (a, b), tales que la suma de los divisores de a es igual a b y la suma de los divisores de b es igual a a (es decir las primeras m parejas de números amigos).

# d) Proponer optimizaciones a las funciones anteriores para disminuir el tiempo de ejecución.

# 25. Escribir un programa que le pida al usuario que ingrese una sucesión de números naturales (primero uno, luego otro, y así hasta que el usuario ingrese ’-1’ como condición de salida). Al final, el programa debe imprimir cuántos números fueron ingresados, la suma total de los valores y el promedio.


# 26. Escribir una función que reciba dos números como parámetros, y devuelva cuántos múltiplos del primero hay, que sean menores que el segundo.

# a) Implementarla utilizando un ciclo for, desde el primer número hasta el segundo.

# b) Implementarla utilizando un ciclo while, que multiplique el primer número hasta que sea mayor que el segundo.

# c) Comparar ambas implementaciones: ¿Cuál es más clara? ¿Cuál realiza menos operaciones?

# 27. Escribir una función que reciba un número natural e imprima todos los números primos que hay hasta ese número.

# 28. Escribir una función que reciba un dígito y un número natural, y decida numéricamente si el dígito se encuentra en la notación decimal del segundo.


# 29. Escribir una función que dada la cantidad de ejercicios de un examen, y el porcentaje necesario de ejercicios bien resueltos necesario para aprobar dicho examen, revise un grupo de examenes. Para ello, en cada paso debe preguntar la cantidad de ejercicios resueltos por el alumno, indicando con un valor centinela que no hay más examenes a revisar. Debe mostrar por pantalla el porcentaje correspondiente a la cantidad de ejercicios resueltos respecto a la cantidad de ejercicios del examen y una leyenda que indique si aprobó o no.