#Representa la orientacion Este
from Orientacion import Orientacion


class Este(Orientacion):
    def __init__(self):
        self.desc="soy el Este"
        
        
        
    def ponerEmEn(self,unEm,unContenedor):
        unContenedor.este=unEm