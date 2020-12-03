# Inicializar un arreglo de 5 elementos en cero y mostrarlo
'''
a = [0,0,0,0,0]
for i in a:
    print("\t", a[i], end="")
'''
# Operacion con arreglos

# Cargar elementos
'''
a = []
n = int(input("Ingrese la cantidad de elementos del vector: "))
for i in range(0,n,1):
    a.append(int(input("Ingrese el valor de cada elemento \t")))

print(a)
'''

# Recorrer un arreglo

# Sumar los elemento del arreglo
'''
n = [2,4,55,6,8]
sum = 0
for i in range(0,len(n),1):
    sum = sum + n[i]
print(sum)
'''

# Mostrar un arreglo
'''
n = [2,4,55,6,8]
for i in range(0,len(n)):
    print("Elemento %d: %d" %(i,n[i]))
'''

# Buscar un elemento en un arreglo
'''
a = []
n = int(input("Ingrese la cantidad de elemento del vector: "))
for i in range(0,n):
    a.append(int(input("Ingrese el valor de cada elemento: ")))
for i in range(0,n):
    print("Elemento %d: %d" %(i,a[i]))

i=0
while (i<n and a[i]%3!=0):
    i = i+1
if i==n:
    print("El vector no tiene ningun elemento multiplo de 3")
else:
    print("El primer multiplo de 3 esta en la posicion %d y es %d" %(i,a[i]))
'''    

# Intercambiar dos elementos del arreglo
'''
a = [1,2]
aux = a[1]
print(a)
a[1] = a[0]
a[0] = aux
print(a)
'''

# Otras operacion con arreglos

# Insert: permite insertar un valor en una posicion determinada, desplazando los elementos que estan a la derecha del mismo

# Ej 1
'''
a = [2,23,4,5]
print(a)
a.insert(2,44)
print(a)
'''

# Ej 2

'''
a = []
n = int(input("Ingrese la cantidad de elemento del vector: "))
for i in range(0,n):
    a.append(int(input("Ingrese el valor de cada elemento: ")))

print(a)
m = int(input("Ingrese el valor a ingresar: "))
pos = int(input("Ingrese la posicion donde va a insertar en nuevo elemento: "))

a.insert(pos,m)
print(a)

for i in range(0,len(a)):
    print(a[i])
'''
# Reverse: permite invertir los elementos del arreglo
'''
a = [1,2,3,4,5]
print(a)
a.reverse()
print(a)
'''

# Sort: permite ordenar un arreglo en forma creciente

'''
a = []
n = int(input("Ingrese la cantidad de elemento del vector: "))
for i in range(0,n):
    a.append(int(input("Ingrese el valor a ingresar: ")))
print(a)
a.sort()
print(a)

# NOTA: para ordenar un arreglo de forma decreciente podemos utilizar sort() y luego reverse()

a.reverse()
print(a)
'''

# Remove: permite eliminar un elemento determinado del arreglo 
# array.remove(valor)
'''
a = [2,5,66,7,8,13]
print(a)
a.remove(66)
print(a)
'''
# Pop: permite eliminar el elemento de un arreglo por su posicion y devuelve el elemento eliminado
# array.pop(pos)
'''
a = [2,5,66,74,12,77765,8,15]
print(a)
a.pop(3)
print(a)
'''

# Como pasar arreglos como argumento en funciones

'''
def sumar(n,arr):
    suma = 0
    for i in range(0,len(arr)):
        suma = suma + arr[i]
    return suma

# Programa principal

arr = [4,5,2,15]
suma = sumar(len(arr),arr)
print("La suma de los elementos del vector es: %d" %suma)
'''