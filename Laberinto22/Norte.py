#Representa la orientacion Norte
from Orientacion import Orientacion


class Norte(Orientacion):
    def __init__(self):
        self.desc="soy el Norte"
        
        
    def ponerEmEn(self,unEm,unContenedor):
        unContenedor.norte=unEm