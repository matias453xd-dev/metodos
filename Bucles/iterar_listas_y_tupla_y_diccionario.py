animales = ['perro', 'gato', 'loro', 'tigre', 'pez']
numeros = [53, 15, 63, 38, 0]
pais = []
#Por cada animal en animales imprima los animales en lista
for animal in animales:
    print(f'El siguiente animal es un: {animal}')

#Recorriendo la lista y multiplicando cada valor por 10    
for numero in numeros:
    resultado = numero * 10
    print(resultado)

#Iterando dos elementos en un mismo for, (pueden ser mas)    
for numero,animal in zip(animales,numeros):
    print(f'Recorriendo lista2: {animal}')
    print(f'recorriendo la lista1: {numero}')
#Iterando en cierto rango, Iterar= Repetir
for i in range(5, 12):
    print(i)
print('')
#Recorre la lista por el indice, (Forma no optima)
for num in range(len(numeros)):
    print(numeros[num])
print('')

#Forma correcta de recorrer una lista con su indice
for num in enumerate(numeros): # enumerate le asigna a cada elemento un numero de indice
    print(num)
    indice = num[0]
    valor = num[1]
    print(f'El indice es: {indice} y el valor es {valor}')
print('') 
#Usando el for/else
for numero in numeros:
    print(f'Ejecutando el ultimo bucle, valor actual: {numero}')
    
else:
    print('El bucle termino')
print('')    
diccionario = {
    'nombre': 'Matias',
    'apellido': 'Llanos',
    'dinero': '50000'
    
}
#Itera las llaves del diccionario
for lol in diccionario:
    print(lol)
print('')

#Recorrer diccionario con items() para obtener la clave y el valor
for datos in diccionario.items():
    key = datos[0]
    value = datos[1]
    print(f'La clave es {key} y el valor es {value}')
