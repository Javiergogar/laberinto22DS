#Representa la orientacion Norte
#En este clase he implementado Singleton
from Orientacion import Orientacion


class Oeste(Orientacion):
    
    #Para el singleton
    unicaInstancia=None
    def __new__(cls):
        if Oeste.unicaInstancia is None:
            Oeste.unicaInstancia = object.__new__(cls)
        else:
            print("Error, Oeste solo se puede instanciar una vez, devolviendo la instancia existente")
            
        return Oeste.unicaInstancia
    
    def __init__(self):
        self.desc="soy el Oeste"
        
        
        
    def ponerEmEn(self,unEm,unContenedor):
        unContenedor.oeste=unEm