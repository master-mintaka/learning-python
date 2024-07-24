first_name = 'John Wilhem'
last_name = 'Granados Alcala'

#Concatenar cadenas
print ( first_name + ' ' + last_name)

#Repetir cadenas
print(first_name * 5)

#Longitud de una cadena
print('Longitud de cadena: ' + str(len(first_name)))

#Pasar a minusculas y mayuscula
upper = 'TEXTO EN MAYUSCULA'
lower = 'texto en minuscula'

print(upper.lower())
print(lower.upper())

#Quitar espacios en blanco al principio y al final
cadena = '   | aqui la cadena |   '
print(cadena.strip())

## CLASE 5
#La coma dentro del print sirve para dar un espacio entre los elementos de la concatenación, el + para concatenar no pone espacios
frase = "Nunca pares de aprender"
author = "Platzi"
print("Frase:", frase, "Autor:", author)

#Otra forma es con print con formato
nombre = "Michael Dudykoff"
profesion = "Martial Arts Expert"
print("His name {}, and he is  {}".format(nombre, profesion))

#Operaciones Matemáticas
a = 10
b = 3
print("Suma:",  a + b)
print("Resta:",  a - b)
print("Multiplicacion:",  a * b)
print("División:",  a / b)
print("Parte entera:",  a // b)
print("Residuo:",  a % b)
