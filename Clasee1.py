# Ejercicio 1
sueldo = int((input("Ingrese su sueldo: ")))
aumento = 0

if sueldo < 150000:
    print("El sueldo es menor a 150000")
    aumento = 0.25
elif 150000 <= sueldo <= 350000:
    print("El sueldo es mayor a 150000 y menor a 350000")
    aumento = 0.20
else:
    print("El sueldo es mayor a 350000")
    aumento = 0.17
    
sueldototal = sueldo + (sueldo * aumento)
print(f"Su sueldo con el aumento es: {sueldototal}")
