# Retornara una funcion la cual le hace falta un numero(num1), recibirá ese valor desde otra funcion
def Suma(num2):
    return lambda num1: num1 + num2
def Resta(num2):
    return lambda num1: num1 - num2
def Multiplicacion(num2):
    return lambda num1: num1 * num2
def Division(num2):
    if(num2 != 0):
        return lambda num1: num1 / num2
    else:
        return None

# Las siguientes funciones reciben otra funcion de parametro, si no la reciben solo retornan el numero
def Two(operation=None):
    if(operation==None):
        return 2
    else:
        # operation = lambda, se reemplaza la variable num1 con el parametro de operation()
        return operation(2)
def Seven(operation=None):
    if(operation==None):
        return 7
    else:
        return operation(7)
def Nine(operation=None):
    if(operation==None):
        return 9
    else:
        return operation(9)
    
print(Nine(Suma(Two()))) # 11
print(Seven(Multiplicacion(Nine()))) # 63
print(Two(Division(Seven()))) # 0.2857