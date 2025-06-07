#Sucecion de figonacci
def figonacci(num):
    a,b = 0,1
    figonacci_lista = []
    for i in range(num):
        if a + b > num: return figonacci_lista
        else: 
            figonacci_lista.append(b)
            a,b = b,a+b  
resultado = figonacci(21)
print(resultado)