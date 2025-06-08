# Calcular el factorial de un numero entero
num = int(input("Ingrese un numero: "))
def factorial(num):
    resultado = num
    for i in range(1, num):
        resultado = resultado*(num-i)
    print(resultado)
factorial(num)