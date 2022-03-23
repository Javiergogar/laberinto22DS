#Es un clase que representa un conjunto de habitaciones

class Laberinto:
    def __init__(self):
        self.habitaciones=[]
        self.desc="soy un laberinto"
        
    def agregarHabitaciones(self,unaHab):
        self.habitaciones.append(unaHab)