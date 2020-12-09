# Cadenas de caracteres


# 30. Escribir funciones que dada una cadena de caracteres:

# a) Imprima los dos primeros caracteres.

# b) Imprima los tres últimos caracteres.

# c) Imprima dicha cadena cada dos caracteres. Ej.: 'recta' debería imprimir 'rca'

# d) Dicha cadena en sentido inverso. Ej.: 'hola mundo!' debe imprimir '!odnum aloh'

# e) Imprima la cadena en un sentido y en sentido inverso. Ej: 'reflejo' imprime 'reflejoojelfer'.


# 31. Escribir funciones que dada una cadena y un caracter:

# a) Inserte el caracter entre cada letra de la cadena. Ej: 'separar' y ',' debería devolver 's,e,p,a,r,a,r'

# b) Reemplace todos los espacios por el caracter. Ej: 'mi archivo de texto.txt' y '_' debería devolver 'mi_archivo_de_texto.txt'

# c) Reemplace todos los dígitos en la cadena por el caracter. Ej: 'su clave es: 1540' y 'X' debería devolver 'su clave es: XXXX'

# d) Inserte el caracter cada 3 dígitos en la cadena. Ej. '2552552550' y '.' debería devolver '255.255.255.0'


# 32. Modificar las funciones anteriores, para que reciban un parámetro que indique la cantidad máxima de reemplazos o inserciones a realizar.


# 33 Escribir una función que reciba una cadena que contiene un largo número entero y devuelva una cadena con el número y las separaciones de miles. Por ejemplo, si recibe '1234567890', debe devolver '1.234.567.890'.

# 34. Escribir una función que dada una cadena de caracteres, devuelva:

# a) La primera letra de cada palabra. Por ejemplo, si recibe 'Universal Serial Bus' debe devolver 'USB'.

# b) Dicha cadena con la primera letra de cada palabra en mayúsculas. Por ejemplo, si recibe 'república argentina' debe devolver 'República Argentina'.

# c) Las palabras que comiencen con la letra ‘A’. Por ejemplo, si recibe 'Antes de ayer' debe devolver 'Antes ayer'


# 35. Escribir funciones que dada una cadena de caracteres:

# a) Devuelva solamente las letras consonantes. Por ejemplo, si recibe 'algoritmos' o 'logaritmos' debe devolver 'lgrtms'.

# b) Devuelva solamente las letras vocales. Por ejemplo, si recibe 'sin consonantes' debe devolver 'i ooae'.

# c) Reemplace cada vocal por su siguiente vocal. Por ejemplo, si recibe 'vestuario' debe devolver 'vistaerou'.

# d) Indique si se trata de un palíndromo. Por ejemplo, 'anita lava la tina' es un palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda).


# 36. Escribir funciones que dadas dos cadenas de caracteres:

# a) Indique si la segunda cadena es una subcadena de la primera. Por ejemplo, 'cadena' es una subcadena de 'subcadena'.

# b) Devuelva la que sea anterior en orden alfábetico. Por ejemplo, si recibe 'kde' y 'gnome' debe devolver 'gnome'.


# 37. Escribir una función que reciba una cadena de unos y ceros (es decir, un número en representación binaria) y devuelva el valor decimal correspondiente.


# 38. Implementar la función pedir_entero(mensaje, min, max), que debe imprimir el mensaje y luego esperar a que el usuario ingrese un valor. Si el valor ingresado no es un número entero, o no es un número entre min y max (inclusive), se le debe avisar al usuario y pedir el ingreso de otro valor. Una vez que el usuario ingresa un valor válido, la función lo debe devolver.

'''
Ejemplo:
>>> z = pedir_entero("¿Cuál es tu número favorito?", -50, 50)
¿Cuál es tu número favorito? [-50..50]:
10
Por favor ingresa un número entre -50 y 50.
¿Cuál es tu número favorito? [-50..50]: hola
Por favor ingresa un número entre -50 y 50.
¿Cuál es tu número favorito? [-50..50]: -60
Por favor ingresa un número entre -50 y 50.
¿Cuál es tu número favorito? [-50..50]: 51
Por favor ingresa un número entre -50 y 50.
¿Cuál es tu número favorito? [-50..50]: -16
>>> z
-16
'''