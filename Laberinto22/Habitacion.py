#Esta clase es un elemento del mapa con 4 lados y elementos
from ElementoMapa import ElementoMapa
class Habitacion(ElementoMapa):
    def __init__(self,num):
        self.norte=any
        self.sur=any
        self.este=any
        self.oeste=any
        self.num=num
        self.desc="soy la habitacion " + str(self.num)