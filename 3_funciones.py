# Funcion capitalizar una frase

def capitalize(text):
    return text[0:1].upper() + text[1:len(text)]


frase = "hola mundo"
print(capitalize(frase))
print(frase)


# Funcion para mostar arrays
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


# Funciones Recursivas

# factorial

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

# Hacer Ejercicio Fibonnaci