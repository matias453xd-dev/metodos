from functools import reduce
# La programacion funcional se centra en trabajar
# con funciones puras, inmutabilidad, evitando efectos
# secundarios, etc. Utiliza lambdas(funciones anonimas)
# que son mas cortas, lambda <argumento>: expresion

# Herramientas
numeros = [1,2,3,4,5]
cuadrados = map(lambda x: x**2, numeros) #map() modifica una coleccion y devuelve una lista
print(list(cuadrados)) # [1,4,5,16,25]

pares = filter(lambda x: x%2==0,numeros) # Aplica un filtro y devuelve una lista
print(list(pares)) # [2,4]

producto = reduce(lambda x,y: x*y, numeros) # Aqui se van tomando numeros de a 2
print(producto) # 1*2= 2 -> 2*3= 6 -> 6*4 = 24 -> 24*5 = 120

# Comprension de colecciones de datos
cubo = [x**3 for x in numeros] #[1,8,27,64,125]
print(cubo)

impares = [x for x in numeros if x % 2 != 0] # Definiendo la variable x, por cada x(elemento) en "numeros", si cumple la condicion guardalo
print(impares)

# Una utilidad importante de las lambda en la P.Funcional
# es que se puede pasar de parametro a otras funciones
print("----------0----------")
def aplicar_operacion(funcion, numeros):
    return [funcion(n) for n in numeros]

numeros = [1, 2, 3, 4]
resultado = aplicar_operacion(lambda x: x**2, numeros)
print(resultado)  # Salida: [1, 4, 9, 16]

# Verificaciones
numbs = [2,4,6,8]
print(all(x % 2 == 0 for x in numbs)) # True, son todos pares
print(any(x % 2 == 0 for x in numbs)) # True, al menos uno es par