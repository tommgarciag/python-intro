# Ejercicios Adicionales Python.


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
'''
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
'''

# 14. Escribir un programa que escriba en pantalla los divisores de un número dado
'''
num = int(input("Ingrese un numero entero: "))
for i in range(1,num+1,1):    
    if num%i==0:
        print(i)
'''
# 15. Escribir un programa que escriba en pantalla los divisores comunes de dos números dados
'''
num1 = int(input("Ingrese un numero entero: "))
num2 = int(input("Ingrese un segundo numero entero: "))
divisoresNum1 = []
divisoresNum2 = []
divisoresComunes = []

for i in range(1,num1+1,1):
    if num1%i==0:
        divisoresNum1.append(i)

for i in range(1,num2+1,1):
    if num2%i==0:
        divisoresNum2.append(i)

for i in divisoresNum1:
    for x in divisoresNum2:
        if i==x:
            divisoresComunes.append(i)


print(divisoresNum1)
print(divisoresNum2)

print("Los divisores comunes entre", num1, "y", num2, "son", divisoresComunes)
'''
# 16. Escribir un programa que nos diga si un número dado es primo (no es divisible por ninguno otro número que no sea él mismo o la unidad)
'''
def esPrimo(num):    
    if num<2:        
        return False
        

    for i in range(2,num):
        if num%i==0:            
            return False

    return True


numero = int(input("Ingrese un numero entero: "))
if esPrimo(numero)==True:
    print("%d ES un numero primo" %numero)
else:
    print("%d NO ES un numero primo" %numero)
'''
# 17. Pide la edad y si es mayor de 18 años indica que ya puede conducir
'''
edad = int(input("Que edad tenes? "))
if edad>=18:
    print("Ya puede conducir.")
else:
    print("No puede conducir. Debes ser mayor de 18 años.")
'''
# 18. Pide una nota (número). Muestra la calificación según la nota:
'''
• 0-3: Muy deficiente
• 3-5: Insuficiente
• 5-6: Suficiente
• 6-7: Bien
• 7-9: Notable
• 9-10: Sobresaliente
'''

'''
nota = float(input("Ingrese la nota: "))
if nota>0 and nota<=3:
    print("Muy deficiente")
elif nota>3 and nota<=5:
    print("Insuficiente")
elif nota>5 and nota<=6:
    print("Suficiente")
elif nota>6 and nota<=7:
    print("Bien")
elif nota>7 and nota<=9:
    print("Notable")
elif nota>9 and nota<10:
    print("Sobresaliente")
'''

# 20. Realiza un script que pida cadenas de texto hasta que se pulse “cancelar”. Al salir con “cancelar” deben mostrarse todas las cadenas concatenadas con un guión

'''
arr = []
texto = ""

while texto!="cancelar":
    texto = input("Ingrese una cadena de texto: ")
    arr.append(texto)

for i in arr:   
    print(i, end="-")

'''

# 21. Realiza un script que pida números hasta que se pulse “cancelar”. Si no es un número deberá indicarse con un «alert» y seguir pidiendo. Al salir con “cancelar” deberá indicarse la suma total de los números introducidos.


# 22. Realizar una página con un script que calcule el valor de la letra de un número de DNI (Documento nacional de indentidad).
'''
El algoritmo para calcular la letra del dni es el siguiente :
• El número debe ser entre 0 y 99999999
• Debemos calcular el resto de la división entera entre el número y el número 23.
• Según el resultado, de 0 a 22, le corresponderá una letra de las siguientes: (T, R, W, A, G,
M, Y, F, P, D, X, B, N, J, Z, S, Q, V, H, L, C, K, E)
• Si lo introducido no es un número deberá indicarse con un alert y volver a preguntar.
• Deberá de repetirse el proceso hasta que el usuario pulse «cancelar».
'''

# 23. Realiza un script que escriba una pirámide del 1 al 30 de la siguiente forma :
'''
1
22
333
4444
55555
666666
…….
'''
# 24) Haz un script que escriba una pirámide inversa de los números del 1 al número que indique el usuario de la siguiente forma : (suponiendo que indica 6).
'''
666666
55555
4444
333
22
1
'''
# 25. Crea script para generar pirámide siguiente con los números del 1 al número que indique el usuario (no mayor de 50) :

## 26. Un script que escriba los números del 1 al 500, que indique cuales son múltiplos de 4 y de 9 y que cada 5 líneas muestre una línea horizontal. Por ejemplo :
'''
1
2
3
4 (Múltiplo de 4)
5-
————————————————————-
6
7
8 (Múltiplo de 4)
9 (Múltiplo de 9)
10
'''
