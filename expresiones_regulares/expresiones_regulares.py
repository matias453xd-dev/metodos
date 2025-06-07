import re
# import re = importar cadenas
texto = '''Hola maestro, esta es la cadena de texto 1 , como estas mi capitan 
Esta es la segunda linea 234 de texto 
Esta es la final definitiva3'''
#Encontrar texto
resultado = re.search("Hola",texto)
print(resultado)
#Encuentra todas las palabras repetidas
resultado = re.findall("esta", texto, flags=re.IGNORECASE) #Ignora las mayusculas
print(resultado)

#\d -> busca digitos numericos del 0 - 9
resultado = re.findall(r"\d",texto)
print(resultado)

#\D -> busca todo menos digitos numericos del 0 - 9
#resultado = re.findall(r"\D",texto)
#print(resultado)

#\w -> busca caracteres alfanumericos [a-z, A-Z, 0-9]
#resultado = re.findall(r"\w",texto)
#print(resultado)

#\W -> busca todo menos caracteres alfanumericos [a-z, A-Z, 0-9]
#resultado = re.findall(r"\W",texto)
#print(resultado)

#Armando una cadena que busque un numero, seguido de un punto y un espacio
#resultado = re.findall(f'\d, \s', texto)
#print(resultado)

#^ -> Busca el comienzo de una linea, dada una palabra
resultado = re.findall(f'^Hola', texto, flags=re.IGNORECASE)
print(resultado)

# {n} -> Busca n cantidad de veces el valor de la izquierda
resultado = re.findall(r'\d{1,4}', texto)#Tiene que haber numeros en ese rango
print(resultado)

#Dividir una cadena por uno o mas espacios en blanco
resultado = re.split(r'\s+', texto)
print(resultado)