# Cuantas vocales hay en la palabra ingresada
palabra = input("Ingrese una palabra: ")
cont_vocales = 0

for i in palabra:
    if(i == "a" or i == "e" or i == "i" or i == "o" or i == "u"):
        cont_vocales +=1
        
print(f"{palabra} tiene {cont_vocales} vocales")