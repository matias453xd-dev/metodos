#Si el modulo estuviera dentro de una carpeta en la misma ruta
#import funciones_buenas.saludar as m_saludar
import sys

print(sys.builtin_module_names)

#Como sber la ruta de los modulos
print(sys.path)

import modulo_saludar as saludar
print(saludar.saludar('Matias'))

