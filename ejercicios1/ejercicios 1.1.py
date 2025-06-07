otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio = 4
dalto_curso = 1.5

#Duracion real total

crudo_promedio = 5
crudo_dalto = 3.5

#Diferencias de duracion

diferencia_con_min = 100 - dalto_curso / otros_cursos_min *100
print(f'El curso de dalto dura un {diferencia_con_min}% menos que el mas rapido')

tiempo_vacio_promedio = 100 - otros_cursos_promedio *100 // crudo_promedio 
print(f'El curso promedio elimino un {tiempo_vacio_promedio}% de tiempo vacio')

#Ver 10 horas de este curso a cuanto equivaldria con los cursos promedio
print(f'Ver 10 horas de este curso equivalen a ver {otros_cursos_promedio*100 // dalto_curso/10} horas de otros cursos')

#Ejercicio 2
#Tiempo_estimado = int(input('Introduce el tiempo estimado: '))
#palabras = Tiempo_estimado*2
#if Tiempo_estimado > 60:
#    print('Para flaco no te pedí un testamento')
#else:
#    print(f'La cantidad de palabras fueron: {palabras}')

frase = input('Dime una frase: ')
palabras_separadas = frase.split(' ')
cantidad_de_palabras = len(palabras_separadas)
print(f'Dijiste {cantidad_de_palabras} palabras, y tardarias {cantidad_de_palabras/2} segundos en decirla')
print(f'Dalto lo diria en {cantidad_de_palabras/2*1.3} segundos')