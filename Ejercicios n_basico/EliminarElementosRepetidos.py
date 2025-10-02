def delete_nth(order,max_e):
    # Dada una lista y un numero maximo de repeticiones
    # se debe eliminar los elementos que se repitan mas de "max_e"
    newlist = []
    counts = {}
    for item in order: # ([1,1,1,2,3,3,4],2), solo se puede repetir 2 veces
        if item not in counts:
            counts[item] = 0 #Primer ciclo: counts[1] = 0
        if counts[item] < max_e: # True
            newlist.append(item) # newlist = [1]
            counts[item] += 1 #count[1] = 1
    newlist.sort()
    return newlist

print(delete_nth([1,1,2,1,3,4,3,244,4,4,3],3))