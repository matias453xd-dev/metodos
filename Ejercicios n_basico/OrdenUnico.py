def unique_in_order(sequence):
    newlist = []
    palabraActual = ""
    SeqList = list(sequence)
    for i in  range((int)(len(SeqList))):
        if(palabraActual == SeqList[i]):
            continue
        newlist.append(SeqList[i])
        palabraActual = SeqList[i]
    return newlist

li = unique_in_order("AAAABBBBCCCDSSDEWWSS")
print(li)