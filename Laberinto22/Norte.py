#Representa la orientacion Norte
#En este clase he implementado Singleton
from Orientacion import Orientacion


class Norte(Orientacion):
    
    #Para el singleton
    unicaInstancia=None
    def __new__(cls):
        if Norte.unicaInstancia is None:
            Norte.unicaInstancia = object.__new__(cls)
        else:
            print("Error, Norte solo se puede instanciar una vez, devolviendo la instancia existente")
            
        return Norte.unicaInstancia
            
    def __init__(self):
        self.desc="soy el Norte"
        
        
    def ponerEmEn(self,unEm,unContenedor):
        unContenedor.norte=unEm