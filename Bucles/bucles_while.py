#Creando un contador que va a ir sumando hasta un cierto valor
contador = 0
while contador <27:
    print(contador)
    contador +=1
print('El contador llego a su fin')

#Ejercicio de calcular votos
votosa = 0
votosb = 0
votosc = 0
votosnulos = 0
n = 0
cantidadvotos = int(input('Ingrese la cantidad de votantes: '))
while n < cantidadvotos:
    candidato = int(input('Ingrese el voto. 1.-Candidato A, 2.-Candidato B, 3.-Candidato C, cualquier otro voto será invalido '))
    if candidato == 1:
        votosa = votosa + 1
    elif candidato == 2: 
        votosb = votosb + 1
    elif candidato == 3:
        votosc = votosc + 1
    elif candidato != 1 and candidato != 2 and candidato != 3:
        votosnulos = votosnulos + 1
    n += 1
    
print(f'La cantidad de votos para A es {votosa}, para B son {votosb}, para c son {votosc} y los votos nulos son {votosnulos}')
if votosa > votosb and votosa > votosc:
    print('Ganó el candidato A')
elif votosb > votosa and votosb > votosc:
    print('Ganó el candidato B')
elif votosc > votosa and votosc > votosb:
    print('Ganó el candidato C')
else:
    print('Hubo un empate')
    