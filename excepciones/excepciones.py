#Creando funcion suma numeros
def sum_dos():
    while True: 
      #Pidiendo numeros
      a = input("Numero 1: ")
      b = input("Numero 2: ")
      try:
        resultado = int(a) + int(b)
        #Si lanzo una excepcion, pedir que reingrese los datos
      except Exception as e:
          print("Te pedi un numero" )
          #Cual es el error
          print(f"ERROR: {e}")
      else:
        break
      finally:
        print("Esto se ejecuta siempre")
    #Mostrar resultado
    return resultado
print(sum_dos())