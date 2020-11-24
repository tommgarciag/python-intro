'''

a = 10
cad = 'hola'

nombre = input('Ingrese su nombre: ')


print(cad, nombre)

num = int(input('Ingrese un numero entero: '))

print('El numero ingrasado es %d'%(num))

if num==0:
    print('El numero ingrasado %d, es CERO'%(num))
elif num%2==0:
    print('El numero ingrasado %d, es PAR'%(num))
else:
    print('El numero ingrasado %d, es IMPAR'%(num))

'''

a='programacion'
print(a[:4]) #output= prog
print(a[6:]) #output= macion
print(len(a)) #output= 12
print(a.upper()) # =PROGRAMACION
print(a.lower()) # =programacion
print(a.capitalize()) # =Programacion
