import csv

with open("metodos\\archivos_csv\\archivos.csv", encoding='UTF-8') as archivo:
    reader = csv.reader(archivo)
    for row in reader:
        print(row)
