from collections import defaultdict
# defaultdict se utiliza para inicializar un diccionario con valores por defecto
# En caso de que sean enteros -> 0; listas -> []; string -> "" 

# Crear un defaultdict con list como valor predeterminado
agrupador = defaultdict(list)

# Agrupar elementos
datos = [('a', 1), ('b', 2), ('a', 3), ('b', 4), ('c', 5)]
for clave, valor in datos:
    agrupador[clave].append(valor)

print(agrupador)

cont = defaultdict(int)
print(cont["Lol"]) # Llave inexistente, da como valor: 0
cont["Lol"] = 4
print(cont["Lol"]) # 4

letras = defaultdict(str)
print(letras["Matias"]) # " "
letras["Matias"] = "|"
print(letras["Matias"]) # "|"

Alumnos = ["Matias","Juan","Alberto","Juan","Nicolas"]
for i in Alumnos: # Por cada vez que se repitan los nombres, se agregará "|"
    letras[i] += "|"
print(letras)