#Letras en mayuscula
cadena_1 = 'Hola que paso'.upper()
print(cadena_1)

#Primera letra en mayuscula
palabra = 'nerf al minero'.capitalize()
print(palabra)

#Buscamos una cadena en una cadena
busqueda = palabra.find('minero')
print(busqueda)
busqueda2 = palabra.index('al')
print(busqueda2)

#¿Es un numero?
fuego = '32'
es_numerico = fuego.isnumeric()
print(es_numerico)

#Buscar la cantidad de repeticiones
contar_coincidencia = palabra.count('e')
print(contar_coincidencia)

#Remplaza un pedazo de cadena con otra
cadena_remplazada = palabra.replace('al','EL')
print(cadena_remplazada)

#Nos va a separar cadenas con las cadenas que le pasemos
cadena_separada = palabra.split(' ')
print(cadena_separada)
print(cadena_separada[0])