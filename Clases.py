class Personaje():
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, suerte):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa 
        self.vida = vida
        self.suerte = suerte
    
    def atributos(self):
        print(self.nombre,":", sep="")
        print("-Fuerza: ",self.fuerza)
        print("-Inteligencia: ",self.inteligencia)
        print("-Defensa: ",self.defensa)
        print("-Vida: ",self.vida)
        print("-Suerte: ",self.suerte)
    
    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.fuerza += fuerza
        self.inteligencia += inteligencia
        self.defensa += defensa
    
    def esta_vivo(self):
        return self.vida > 0
    
    def morir(self):
        self.vida = 0
        print(self.nombre, "ha muerto")
        
    def daño(self, enemigo):
        return self.fuerza - enemigo.defensa
    
    def atacar(self, enemigo):
        daño = self.daño(enemigo)
        enemigo.vida -= daño
        print(self.nombre, "ha realizado", daño, "puntos de daño a", enemigo.nombre)
        if enemigo.esta_vivo():
             print("La vida de", enemigo.nombre, "es", enemigo.vida)
        else:
            enemigo.morir()

class Guerrero(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, suerte, espada=0):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida, suerte)
        self.espada = espada
    
    def cambiar_arma(self):
        opcion = int(input("Elige un arma: 1) Espada de acero, 2) Matadragones "))
        if opcion == 1:
            self.espada = 8
        elif opcion == 2:
            self.espada = 10
        else:
            print("La opción no está disponible")
    
    def atributos(self):
        super().atributos()
        print("Espada: ", self.espada)
    
    def daño(self, enemigo):
        return self.fuerza * self.espada - enemigo.defensa

class Mago(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, suerte, libro=0):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida, suerte)
        self.libro = libro
    
    def cambiar_arma(self):
        opcion = int(input("Elige un arma: 1) Favonius, 2) Sacrificio "))
        if opcion == 1:
            self.libro = 6
        elif opcion == 2:
            self.libro = 10
        else:
            print("La opción no está disponible")
    
    def atributos(self):
        super().atributos()
        print("Libro: ", self.libro)
    
    def daño(self, enemigo):
        return self.inteligencia * self.libro - enemigo.defensa

# Creación de personajes
Asta = Guerrero("Asta", 5, 1, 4, 120, 2)
Asta.cambiar_arma()
Asta.atributos()

Vanessa = Mago("Vanessa", 3, 5, 2, 110, 3)
Vanessa.cambiar_arma()
Vanessa.atributos()

# Bucle de combate
print("Empieza la pelea:")
while Asta.esta_vivo() and Vanessa.esta_vivo():
    Asta.atacar(Vanessa)
    if Vanessa.esta_vivo():
        Vanessa.atacar(Asta)
    Asta.atributos()
    Vanessa.atributos()
    if Vanessa.vida <= 0:
        print("Asta ha ganado")
    elif Asta.vida <= 0:
        print("Vanessa ha ganado")
    else:
        print("Siguiente turno:")



    


