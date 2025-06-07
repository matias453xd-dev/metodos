# Un modulo es como una carpeta, desde un modulo puedo llamar a otro modulo, usando sus funciones
import modulo_saludar
# La funcion 'as' permite renombrar modulos
saludo = modulo_saludar.saludar('Matias')
print(saludo)
print(type(modulo_saludar))

#Importamos 2 funciones y les cambiamos el nombre a una
from modulo_saludar import saludar,saludar_raro as saludar_como_chileno
saludo = saludar('Matias')
saludo_raro = saludar_como_chileno('Fran')
print(saludo)
print(saludo_raro)
# Con 'import *' se importa todo lo del modulo

print(modulo_saludar,__name__) #'modulo_saludar' es el modulo principal

