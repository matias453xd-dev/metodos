# Verificar si la palabra se lee igual al derecho y al revez
palindromo = input("Ingrese una palabra: ")
Validez = True
j = -1

for i in range(len(palindromo)//2):
    if(palindromo[i] != palindromo[j]):
        Validez = False
        break
    j -= 1
    
if(Validez):
    print(f"La palabra {palindromo} si es un palindromo")
else:
    print(f"La palabra {palindromo} NO es un palindromo")