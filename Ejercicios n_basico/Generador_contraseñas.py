import secrets
import string
# La libreria secrets es parecido a random pero mas seguro
# Puedes personalizar los caracteres que quieres usar
caracteres = string.ascii_letters + string.digits + string.punctuation  # todo el alfabeto, números y símbolos

longitud = int(input("Ingrese el largo de la contraseña: "))
# La contraseña queda como String, se usa join en ves de append o insert que son para listas
contraseña = ''.join(secrets.choice(caracteres) for _ in range(longitud))

print(f"La contraseña generada es: {contraseña}")



