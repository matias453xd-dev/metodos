multiplicar_por_dos = lambda x : x*2 #Lambda crea funciones vacias
print(multiplicar_por_dos(5))

#Creando funcion si es o no par
numeros = [1,2,3,4,5,6,7,8]
def es_par(num): #Si el numero es impar retorna el numero
    if (num%2==0):
        return True
numeros_pares = filter(es_par, numeros) #Asignando los valores de la variable 'numeros' al parametro 'num'
print(list(numeros_pares))

numeros_pares = filter(lambda numero:numero%2 == 0, numeros) #Lo mismo pero con lambda, parametro 'numero', en donde 'numero' es divisible por dos en la variable 'numeros'
print(list(numeros_pares))

def es_impar(lol): # Numeros impares
    if (lol%2!=0):
        return True
numeros_impares = filter(es_impar, numeros)
print(list(numeros_impares))