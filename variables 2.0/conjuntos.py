#Creando un conjunto con 'set', set= Conjunto
conjunto =set(['Hola','que tal'])
print(conjunto)

#Metiendo un conjunto dentro de otro conjunto
conjunto1 = frozenset(['dato1','dato2'])
conjunto2 = {conjunto1,'dato3'}
print(conjunto2)

#Subconjunto de un conjunto, ussubset = 'Es un subconjunto'
conjunto3 = {1,3,5,7}
subconjunto = {1,3,7}
resultado = subconjunto.issubset(conjunto3)
print(resultado)
#Verificando si es un subconjunto, el subconjunto debe ser menor
resultado = subconjunto <= conjunto3
print(resultado)
#Verificando si es un superconjunto
resultado = subconjunto.issuperset(conjunto3)
print(resultado)
resultado = conjunto3.issuperset(subconjunto)
print(resultado)



