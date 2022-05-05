#Representa la orientacion Este
#En este clase he implementado Singleton
from Orientacion import Orientacion


class Este(Orientacion):
    
    #Para el singleton
    unicaInstancia=None
    def __new__(cls):
        if Este.unicaInstancia is None:
            Este.unicaInstancia = object.__new__(cls)
        else:
            print("Error, Este solo se puede instanciar una vez, devolviendo la instancia existente")
            
        return Este.unicaInstancia
    
    def __init__(self):
        self.desc="soy el Este"
        
        
        
    def ponerEmEn(self,unEm,unContenedor):
        unContenedor.este=unEm