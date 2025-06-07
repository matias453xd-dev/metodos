import time
import threading

# La programacion congruente consiste en ejecutar multiples tareas a la vez
# A diferencia de la programacion secuencial, en la que las tareas se ejecutan una tras otra, en orden
def codificar():
    time.sleep(2) #Se define un tiempo muerto de 2 segundos en todas las funciones

    print(f'Codificando')

def responder_correos():
    time.sleep(2)

    print(f'Respondiendo correos')

def realizar_calculos():
    time.sleep(2)

    print(f'Realizar los calculos')
# Se crean los hilos para cada funcion 
threading.Thread(target=codificar).start()
threading.Thread(target=responder_correos).start()
threading.Thread(target=realizar_calculos).start()
# Se ejecutan las funciones en paralelo tardando solo 2 segundos
# A diferencia de la programacion secuencial que tardaria 6 segundos
