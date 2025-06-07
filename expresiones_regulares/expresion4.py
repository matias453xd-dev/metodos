import re
#Verificar si una cadena es una fecha en formato YYYY-MM-DD
date_pattern = r'^\d{4}-\d{2}-\d{2}$'
print("Ingrese una fecha en formato YYYY-MM-DD")
date = input()
if re.match(date_pattern, date):
    print("Fecha válida")
else:
    print("Fecha no válida")
