#Encontrando el numero mayor de una lista
numeros = [2,6,43,21,39]

numero_mas_alto = max(numeros)
print(numero_mas_alto)

#Encontrando el numero menor
numero_mas_bajo = min(numeros)
print(numero_mas_bajo)

#Redondeando a con 3 digitos
numero = round(12.345,3)
print(numero)

#Retorna falso cuando = 0, False, None\ Retorna verdad cuando es distinto de 0.
resultado = bool()
resultado2 = bool(2)
print(resultado)
print(resultado2)
print('~~~~~~o~~~~~~~')
#Retorna true si todos los valores son verdaderos
resultado_all = all([234, 'true', [344,23]])
print(resultado_all)
resultado_all = all([0])
print(resultado_all)

#Suma todos los valores
suma_total = sum(numeros)
print(suma_total)