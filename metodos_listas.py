lista =list(['Hola','Dalto',54])
print(lista)

lista.append('brawl_stars')
print(lista)
print(len(lista))

lista.insert(2,'clash royale')
print(lista)

lista.extend([False, 2030])
print(lista)

#pop elimina el primer elemento
#lista.pop(0)
print(lista)
print(len(lista))
#lista.pop(-1)
print(lista)
print(len(lista))

lista.remove('Dalto')
print(lista)

#elimina todos los elementos
#lista.clear()

#No puede ordenar str
#lista.sort()
#print(lista)

#invierte los elementos de una lista
lista.reverse()
print(lista)
print(lista.index('Hola'))

