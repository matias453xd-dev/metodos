diccionario =dict(nombre= 'Matias', apellido= 'Llanos0')
print(diccionario)

#Las listas no pueden ser llaves pero las tuplas si, a menos que se use el frozenset
#diccionario = {['minero'], 'jijijaja'}
#print(diccionario)
diccionario = {('minero'), 'jijijaja'}
print(diccionario)
diccionario = {frozenset(['Dalto','rancio']): 'jajajaaj'}
print(diccionario)

#Creando diccionarios con fromkeys()
diccionario = dict.fromkeys(['telefono','calle'])
print(diccionario)
#Las listas son las llaves y pueden guardar el mismo valor
diccionario = dict.fromkeys(['telefono1', 'telefono2', 'telefono3'],'cualquiera')
print(diccionario)