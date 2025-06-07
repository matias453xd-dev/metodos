#Edad de los compañeros y ordenarlos de mayor a menor
def obtener_compañeros(cantidad_de_compañeros):
  compañeros = []
  for i in range(cantidad_de_compañeros):
    nombre = input('Ingrese el nombre del compañero: ')
    edad = int(input('Ingrese la edad del compañero: '))
    compañero = (nombre,edad)
    compañeros.append(compañero)
  compañeros.sort(key=lambda x: x[1]) #sort es una funcion que ordena un conjunto segun un parametro
  asistente = compañeros[0][0] #El asistente es el primero de la lista, el menor
  profesor = compañeros[-1][0] #El profesor es el ultimo de la lista, el mayor
  return asistente,profesor
asistente,profesor = obtener_compañeros(5)
print(f'El asistente es: {asistente}')
print(f'El profesor es: {profesor}')
 