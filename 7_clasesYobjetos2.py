num=5
print("Tipo num: ",type(num)) # muestra el tipo de dato
print("Metodos del tipo de dato int son: ",dir(num))
print(num.__abs__()) # metodo valor absoluto
print(abs(num)) # lo mismo que num.__abs__()

print(num.__add__(4)) # metodo sumar

print(num.__mod__(2)) # metodo modulo == num%2
print(num%2)

print(num.__str__()) # cambia el tipo de dato a string
print(str(num))

real = 3.4
print(type(real))
print("Los metodos del tipo de dato float son: ", dir(real))

print(real.__round__(0)) # metodo redondeo
print(round(real,0))

frase = "Hello world"
print(type(frase))
print("Los metodos del tipo de dato str son: ", dir(frase))

booleano = True
print(type(booleano))
print("Los metodos del tipo de dato bool son: ", dir(booleano))

# Resumiendo, para python todos los tipos de datos son una clase y tienen sus metodos 