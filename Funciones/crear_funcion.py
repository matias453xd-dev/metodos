#Creando una funcion simple
def saludar():
    print('Hola buenas tardes loco')
#Ejecutando la funcion simple
saludar()

def saludo(nombre, sexo):
    sexo = sexo.lower()
    if(sexo== 'mujer'):
        adjetivo = 'Reina'
    elif (sexo== 'hombre'):
        adjetivo = 'Titan'
    else:
        adjetivo ='amoor'
    print(f'Hola {nombre}, mi {adjetivo}, ¿Como andas?')

saludo('Matias', 'hombre')

def suma(*numeros):
    return sum(numeros)
resultado = suma(4,5,6,7)
print(resultado)


    
