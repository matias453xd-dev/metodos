
def FuncionExterior(num):
    return lambda x: x + num # La funcion va a devolver otra funcion

resultado = FuncionExterior(10) #resultado = lambda x: x + 10
print(resultado(5)) # Ahora se reemplaza x con 5 -> 15

valores = [1,2,4,5,13]

def filtrar(x):
    return x > 4

valores_filtrados = filter(filtrar, valores) # Va a aplicar un filtro en la lista de valores
                                             # segun la expresion que devuelve filtrar()
print(list(valores_filtrados))

# Modificando los valores de una lista
# map(expresion, coleccion de datos)
valores_mapeados = map(lambda x: x * 2, valores)
print(list(valores_mapeados))