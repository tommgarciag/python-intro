# 1. Escribe un programa que muestra por pantalla "Hello World".
#print('"Hello World"')

# 2. Escribe un programa que escriba en pantalla el resultado de 3 + 5.
#print(3+5)

# 3. Escribe un programa que pida por pantalla el nombre del usuario y lo salude.
'''
nombreUsuario = input("Ingrese su nombre: ")
print("Hola",nombreUsuario)
'''
# 4.  Escribe un programa que pida un número, pida otro número y escriba el resultado de sumar estos dos números.
'''
num1 = int(input("Ingrese un primer numero: "))
num2 = int(input("Ingrese un segundo numero: "))
suma = num1 + num2
print("La suma entre %d y %d es igual a %d." %(num1,num2,suma))
'''
# 5. Escribe un programa que pida dos números y escriba en la pantalla cual es el mayor.
'''
num1 = int(input("Ingrese un primer numero: "))
num2 = int(input("Ingrese un segundo numero: "))
if num1==num2:
    print("%d es igual que %d" %(num1,num2))
elif num1>num2:
    print("%d es mayor que %d" %(num1,num2))
else:
    print("%d es mayor que %d" %(num2,num1)) 
'''
# 6. Escribe un programa que pida 3 números y escriba en la pantalla el mayor de los tres.
'''
# con if

num1 = int(input("Ingrese un primer numero: "))
num2 = int(input("Ingrese un segundo numero: "))
num3 = int(input("Ingrese un tercer numero: "))
if num1>num2:
    if num1>num3:
        print("%d es mayor que %d y %d" %(num1,num2,num3))
    else:
        print("%d es mayor que %d y %d" %(num3,num1,num2))
else:
    if num2>num3:
        print("%d es mayor que %d y %d" %(num2,num1,num3))
    else:
        print("%d es mayor que %d y %d" %(num3,num1,num2))
'''

'''

# con for

num = int(input("Ingrese un número: "))
maximo = num
for i in range(2):
    num = int(input("Ingrese otro número: "))
    if num>maximo:
        maximo=num
print("El mayor de los numero ingresado es ", maximo)
'''
# 7. Escribe un programa que pida un número y diga si es divisible por 2
'''
num1 = int(input("Ingrese un numero: "))
if num1%2==0: 
    print("%d es divisible por 2" %num1)
else:
    print("%d NO es divisible por 2" %num1)
'''
# 8. Escribe un programa que pida una frase y escriba cuantas veces aparece la letra a
'''
frase = input("Escriba una frase: ")
frase = frase.lower()
contador = 0
for i in frase:
    if i=="a":
        contador += 1
print("En la frase ingreasada hay %d letras a" %contador)
'''
# 9. Escribe un programa que pida una frase y escriba las vocales que aparecen
'''
frase = input("Escriba una frase: ")
frase = frase.lower()
vocales = ["a","e","i","o","u"]
for i in frase:
    for x in vocales:
        if i==x:
            print(i)
'''

# 10. Escribe un programa que pida una frase y escriba cuántas de las letras que tiene son vocales
'''
frase = input("Escriba una frase: ")
frase = frase.lower()
contador = 0
vocales = ["a","e","i","o","u"]
for i in frase:
    for x in vocales:
        if i==x:
            contador += 1
print("La frase ingrasada contiene %d vocales" %contador)
'''

# 11. Escribe un programa que pida una frase y escriba cuántas veces aparecen cada una de las vocales
'''
frase = input("Escriba una frase: ")
frase = frase.lower()
vocales = ["a","e","i","o","u"]
contadorA = 0
contadorE = 0
contadorI = 0
contadorO = 0
contadorU = 0
for i in frase:
    for x in vocales:
        if i==x and i=="a":
            contadorA += 1
        elif i==x and i=="e":
            contadorE += 1
        elif i==x and i=="i":
            contadorI += 1
        elif i==x and i=="o":
            contadorO += 1
        elif i==x and i=="u":
            contadorU += 1

print("La frase ingrasada contiene: \n %d vocales 'A' \n %d vocales 'E' \n %d vocales 'I' \n %d vocales 'O' \n %d vocales 'U'" %(contadorA,contadorE,contadorI,contadorO,contadorU))
'''
# 12. Escribe un programa que pida un número y nos diga si es divisible por 2, 3, 5 o 7 (sólo hay que comprobar si lo es por uno de los cuatro)
'''
num = int(input("Ingrese un numero: "))
if num%2==0:
    print("%d es divisible por 2" %num)
elif num%3==0:
    print("%d es divisible por 3" %num)
elif num%5==0:
    print("%d es divisible por 5" %num)
elif num%7==0:
    print("%d es divisible por 7" %num)
else:
    print("%d no es divisible por 2,3,5,o 7" %num)
'''

# 13. Añadir al ejercicio anterior que nos diga por cual de los cuatro es divisible (hay que decir todos por los que es divisible)

num = int(input("Ingrese un numero: "))
divisores = [2,3,5,7]
cantDivisores = 0
for i in divisores:
    if num==0:
        print("El numero ingrasado es %d" %num)
        break
    elif num%i==0:
        print("%d es divisibles por %d" %(num,i))
        cantDivisores += 1
if cantDivisores==0:
    print("%d no es divisible por 2,3,5 o 7" %num)
  

# 14. Escribir un programa que escriba en pantalla los divisores de un número dado

# 15. Escribir un programa que escriba en pantalla los divisores comunes de dos números dados