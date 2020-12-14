# Dado dos numeros, mostrar el mayor
'''
def mayor(a,b):
    if a==b:
        print("%d es igual que %d" %(a,b))
    elif a>b:
        print("%d es mayor que %d" %(a,b))
    else:
        print("%d es mayor que %d" %(b,a))

# Programa principal
num1 = int(input("Ingrese un numero:"))
num2 = int(input("Ingrese otro numero:"))
mayor(num1,num2) # llamado a la funcion
'''

# Funcion capitalizar una frase
'''
def capitalize(text):
    return text[0:1].upper() + text[1:len(text)]


frase = "hola mundo"
print(capitalize(frase))
print(frase)
'''

# Funcion para mostar arrays

'''
def ordenar(array):
    array.sort()

def mostar(array):
    ordenar(array)
    for i in array:
        print(i)

a1 = [12,2,33,4,512]
a2 = ["juan","tomas","ana","jesus"]

print(a1)

mostar(a1)

print(a1) # observo que un array una vez ordenado se modifica y queda asi siempre

'''

# Calcular la suma de n numero enteros
'''
def suma(n):
    a = 0
    for i in range(0,n,1):
        x = int(eval(input("Ingrese un numero: ")))
        a = a + x
    
    return print("La suma es %d" %a)

x = int(eval(input("Ingrese la cantidad de numeros que desea sumar: ")))
suma(x)
'''

# Escribir en dos columnas las potencias de 2 y 3 con exponeste 0 y 9

def potencia(m,n):
    p = 1
    for i in range(1,n,1):
        p = p * m
    return p

# Programa principal
'''
for i in range(0,10,1):
    if i==0:
        a=1
        b=1
    else:
        a=potencia(2,i)
        b=potencia(3,i)
    print("\t", i,a,b)
'''
# Funciones Recursivas

# factorial
'''
def factorial(n):
    fac=1
    for i in range(1,n+1,1):
        fac = fac*i
    return fac

print(factorial(5))

def factorialRecursivo(n):
    if n==1:
        return 1
    else:
        return n*(factorialRecursivo(n-1))

print(factorialRecursivo(5))
'''
# Hacer Ejercicio Fibonnaci

def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=" ")
        a,b = b, a+b
    print()

# fib(2000)

# Argumentos con valores por omision: 

def pedir_confirmacion(prompt, reintentos=4, queja="Si o no, por favor."):
    while True:
        ok = input(prompt)
        if ok in ("s","S","si","Si","SI"):
            return True
        if ok in ("n","N","no","No","NO"):
            return False
        reintentos = reintentos -1
        if reintentos < 0:
            raise OSError("Usuario duro")
        print(queja)

# Esta funcion puede ser llamada de distintas maneras

# pedir_confirmacion("Realmente quieres salir? ")
# pedir_confirmacion("¿Sobreescribir archivo? ", 2)
# pedir_confirmacion("¿Sobreescribir archivo?", 2, "Vamos, solo si o no.")