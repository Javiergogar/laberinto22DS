#Esta clase es un Elemento Mapa que tiene hijos, es el composite del patron
from ElementoMapa import ElementoMapa


class Contenedor(ElementoMapa):
    def __init__(self):
        self.hijos=[]
        self.orientaciones=[]
        self.num=any
        self.este=any
        self.oeste=any
        self.norte=any
        self.sur=any
        self.desc="soy un Contenedor"
        
        
    def agregarHijo(self,unEM):
        self.hijos.append(unEM)
        unEM.padre=self
        
        
    def eliminarHijo(self,unEM):
        if unEM in self.hijos:
            self.hijos.remove(unEM)
        else:
            pass  
        
    def ponerEnEM(self,unaOr,unEM):
        unaOr.ponerEmEn(unEM,self)  
        
    def agregarOrientacion(self,unaOr):
        self.orientaciones.append(unaOr)
        
    def obtenerOrientaciones(self):
        return self.orientaciones
    
        