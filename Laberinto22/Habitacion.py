#Esta clase es un elemento del mapa con 4 lados y elementos
from Contenedor import Contenedor

class Habitacion(Contenedor):
    def __init__(self):
        Contenedor.__init__(self)    
        self.desc="soy la habitacion"
        
    def esHabitacion(self):
        return True
    
    #Para probar iteraror   
    def imprimirInfo(self):
        print("Soy la hab-",self.num)
        
    def recorrer(self,unBloque):
        print("Soy la hab-",self.num)
        for i in self.hijos:
            i.recorrer(unBloque)