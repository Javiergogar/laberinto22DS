#Es un clase que representa un conjunto de habitaciones
#Aqui implementamos el iterator para recorrer todo el laberinto

class Laberinto:
    
    def __init__(self):
        self.habitaciones=[]
        self.desc="soy un laberinto"
        
    def agregarHabitaciones(self,unaHab):
        self.habitaciones.append(unaHab)
     
    #iterator   
    def recorrer(self,unBloque):
        print("Recorrer el laberinto")
        for i in self.habitaciones:
            i.recorrer(unBloque)
