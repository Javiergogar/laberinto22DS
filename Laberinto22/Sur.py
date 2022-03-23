#Representa la orientacion Sur
from Orientacion import Orientacion


class Sur(Orientacion):
    def __init__(self):
        self.desc="soy el Sur"
        
    def ponerEmEn(self,unEm,unContenedor):
        unContenedor.sur=unEm