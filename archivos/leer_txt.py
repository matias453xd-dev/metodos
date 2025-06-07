# Leer un archivo creado en bloc de notas
archivo = open("archivos\\Estoy_estudiando_python.txt",encoding="UTF-8")
print(archivo.read())


# Leer linea por linea
lineas = archivo.readline(4)
print(lineas)

