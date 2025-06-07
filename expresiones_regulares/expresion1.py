import re
#Verificar si una cadena es un correo electronico valido
email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
email = "example@example.com"
if re.match(email_pattern, email):
    print("Correo electrónico válido")
else:
    print("Correo electrónico no válido")
    