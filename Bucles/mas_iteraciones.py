frutas = ['platano', 'naranja', 'manzana', 'pera', 'mandarina']
cadena = 'perro gato'
numeros = [2,5,90,10]

#Continue = saltar valores en una iteración
#Si la fruta es igual a manzana saltala y continua
for fruta in frutas:
    if fruta == 'manzana':
        continue
    print(f'Me voy a comer una {fruta}')
print('')

#Evitando que la iteracion/bucle continue, break = termina    
for fruta in frutas:
    if fruta == 'pera':
        break
    print(f'Me voy a comer una {fruta}')
print('')

for letra in cadena:
    print(letra)
    
#For en una sola linea de codigo
numeros_duplicados = list()
for numero in numeros:
        numeros_duplicados.append(numero*2)
print(numeros_duplicados)

#Lo mismo pero en una sola linea de codigo
numero_duplicado = [x*2 for x in numeros]
print(numero_duplicado)