#Representa la orientacion Norte
from Orientacion import Orientacion


class Oeste(Orientacion):
    def __init__(self):
        self.desc="soy el Oeste"
        
        
        
    def ponerEmEn(self,unEm,unContenedor):
        unContenedor.oeste=unEm