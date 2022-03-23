#Define la interface de los objetos de orientacion(Patron Strategy)
import abc


class Orientacion:
    __metaclass__ = abc.ABCMeta
     
    def __init__(self):
        self.desc="soy una orientacion"
        
    @abc.abstractmethod   
    def ponerEmEn(self,unEm,unContenedor):
        pass