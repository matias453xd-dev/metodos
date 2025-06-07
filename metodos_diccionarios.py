libros = {
    'nombre': 'Matias',
    'apellido': 'Llanos',
    'dinero': 10000,
    'libros': 6
}
claves = libros.keys()
print(claves)

#Obteniendo un elemento 
claves = libros.get('dinero')
print(claves)

#Eliminando 1 o mas elementos
print(libros)
libros.pop('dinero','libros')
print(libros)

#Clear lo elemina todo
#libros.clear()
#print(libros)

#Obteniendo un elemento
diccionario = libros.items()
print(diccionario)