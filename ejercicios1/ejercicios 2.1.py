#Creando una funcion que nos devuelvo numeros primos
def numeros_primos(num):
    for i in range(2,num*1):
        if num%i==0: return False  # i va tomando valores desde uno hasta infinito
    return True
resultado = numeros_primos(13)
print(resultado)

def primos_hasta(num):
    primos = []
    for i in range(1, num):
        resultado = numeros_primos(i) 
        if resultado == True: primos.append(i)
    return primos
resultado = primos_hasta(18)
print(resultado)


