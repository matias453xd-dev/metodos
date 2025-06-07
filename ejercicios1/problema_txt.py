#2 listas con nombres, otra con apellidos
nombres = ["Lucas", "Matias", "Camila", "Joaquin", "Andres"]
apellidos = ["Dalto", "Zing", "Robetix", "Albarado", "Brereton"]
# Asignando a cada nombre un apellido
with open("nombre_y_apellidos.txt","w") as arch:
    arch.writelines("Los datos son:\n")
    [arch.writelines(f"Nombre: {n}\nApellido: {a}\n----\n") for n,a in zip(nombres,apellidos)]
    