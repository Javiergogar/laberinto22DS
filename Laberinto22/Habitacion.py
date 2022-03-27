#Esta clase es un elemento del mapa con 4 lados y elementos
from Contenedor import Contenedor

class Habitacion(Contenedor):
    def __init__(self):
        Contenedor.__init__(self)    
        self.desc="soy la habitacion"
       
        