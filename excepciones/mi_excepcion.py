#Creando mi propia excepcion
class MiExcepcion(Exception):
    def __init__(self,err):
        print(f"Impresionante, cometiste el siguiente error: {err}")
#Lanzando mi propia excepcion
try:
  raise MiExcepcion("Que bobo, dividiste por cero")
except:
    print("Como vas a cometer ese error")