# Filtrado de numeros pares
filtrado = [x for x in range(20) if x % 2 == 0 and x > 0]
print(filtrado)

# Metodo filter
miList = [1,2,3,4,5,6]
# filter(expresion, coleccion)
filtrado2 = filter(lambda x: x % 2 == 0, miList) # Toma cada valor de la lista y aplica la expresion lambda
print(list(filtrado2)) # filter() devuelve un objeto generador que se debe convertir para ser mostrado