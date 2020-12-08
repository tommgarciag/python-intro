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