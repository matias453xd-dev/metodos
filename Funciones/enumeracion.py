# Usando la funcion enumerate
series = {"breakin_bad", "Loki", "Un_show_mas", "Hora_de_aventura"}
print(series)
for i in enumerate(series):
    print(i)
# Asignandolo a una variable y convirtiendolo en una lista
seriesenum = enumerate(series)
serieslist = list(seriesenum)
print(serieslist)

# En las tuplas si se pueden llamar elementos por el indice
pizzas = ('jamon', 'cuatroquesos', 'napolitana', 'española')
print(pizzas[1])
for a in enumerate(pizzas):
    print(a)