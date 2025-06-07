#Creando una funcion con 3 parametros

#def frase(nombre,apellido,adjetivo):
#    return f'Hola {nombre} {apellido}, soy muy {adjetivo}'
#frase_resultante = frase(adjetivo = 'capo', nombre = 'Matias', apellido ='Llanos')
#print(frase_resultante)

#Utilizando keyword arguments
def frase(nombre,apellido,adjetivo = 'tonto'): #Por defecto pone el adjetivo tonto
    return f'Hola {nombre} {apellido} soy muy {adjetivo}' 
frase_resultante = frase('Matias','Llanos', adjetivo= 'inteligente') #Pero se puede modificar
print(frase_resultante)
