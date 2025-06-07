# Abriendo un archivo con with open
with open("archivos\\promedio.java", encoding='UTF-8') as archivo:
    print('Hola')
    print(archivo.read())
print('')
with open("Modulos\\modulo_saludar.py", encoding='UTF-8') as archivo:
    print(archivo.read())
# encoding='UTF-8' asegura que Python interprete correctamente los caracteres del archivo como texto Unicode

# Sobreescribiendo un archivo de texto
with open("archivos\\Estoy_estudiando_python.txt", 'w', encoding='UTF-8') as archivo:
    archivo.write('El madrid no llega a la final, ')
    archivo.write('mañana hay que comprar pan')
    

# Se pueden crear archivos de texto, imagen, sonido, etc a partir del with open (aunque algunos no funcionan)
with open("archivos\\Saludos profesor.txt", 'w', encoding='UTF-8') as archivo:
    archivo.writelines(['Hola profesor, como esta ', 'me saque un 7'])
    archivo.writelines(['A que hora es la prueba'])
with open("archivos\\Video musical.mp4", 'w', encoding='UTF-8') as archivo:
    print(archivo)
    
    