#Representa la orientacion Sur
#En este clase he implementado Singleton
from Orientacion import Orientacion


class Sur(Orientacion):
    
    #Para el singleton
    unicaInstancia=None
    def __new__(cls):
        if Sur.unicaInstancia is None:
            Sur.unicaInstancia = object.__new__(cls)
        else:
            print("Error, Sur solo se puede instanciar una vez, devolviendo la instancia existente")
            
        return Sur.unicaInstancia
    
    def __init__(self):
        self.desc="soy el Sur"
        
    def ponerEmEn(self,unEm,unContenedor):
        unContenedor.sur=unEm