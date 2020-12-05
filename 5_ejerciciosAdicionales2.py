# 1. Escribir una función que reciba dos números y devuelva su producto.

'''
def multiplicar(n1,n2):
    return n1*n2

print(multiplicar(2,3))
'''
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

print(perimetroRectangulo(10,4))

# b) Calcular el área de un rectángulo dada su base y su altura.

def areaRectangulo(base,altura):
    return base * altura

print(areaRectangulo(5,2))
# c) Calcular el perímetro de un círculo dado su radio.
# e) Calcular el área de un círculo dado su radio.
# f) Calcular el volumen de una esfera dado su radio.
# g) Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.
# 4. Analizar los siguientes bloques de código. ¿Cuál será el resultado de ejecutarlos?
# Verificar la respuesta con el intérprete.
# a) for i in range(5):
#  print(i * i)
# b) for i in range(2, 6):
#  print(i, 2 ** i)
 

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