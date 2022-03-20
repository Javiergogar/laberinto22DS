#Esta es la clase principal de la solucion


from Pared import Pared
from Puerta import Puerta
from ParedBomba import ParedBomba
from Habitacion import Habitacion
from Laberinto import Laberinto
from Bomba import Bomba
from Bicho import Bicho
from Agresivo import Agresivo
from Perezoso import Perezoso

class Juego:
    def __init__(self):
        self.laberinto=Laberinto()
        self.desc="soy un juego"
        
        
    def fabricarPared(self):
        pared= Pared()
        return pared
    
    def fabricarPuerta(self,lado1,lado2):
        puerta= Puerta(lado1,lado2)
        puerta.lado1=lado1
        puerta.lado2=lado2
        return puerta
    
   
    
    def fabricarHabitacion(self,norte,sur,este,oeste,num):
        habitacion=Habitacion(num)
        habitacion.num=num
        habitacion.norte=norte
        habitacion.sur=sur
        habitacion.este=este
        habitacion.oeste=oeste
        return habitacion
    
    def fabricarParedBomba(self):
        paredBomba=ParedBomba()
        paredBomba.activa=True
        return paredBomba
    
    def fabricarBombaDecora(self,unEm):
        bomba=Bomba()
        bomba.component=unEm
        return bomba
    
    def fabricarBichoEn(self,unModo,unaPosicion):
        bicho=Bicho()
        bicho.modo=unModo
        bicho.posicion=unaPosicion
        return bicho
    
    def fabricarAgresivo(self):
        agresivo=Agresivo()
        return agresivo
    
    def fabricarPerezoso(self):
        perezoso=Perezoso()
        return perezoso
        
        
    def laberinto2habitacionesFM(self):
        pared=self.fabricarPared()
        hab1=self.fabricarHabitacion(pared,None,pared, pared,1)
        hab2=self.fabricarHabitacion(None, pared, pared, pared,2)
        puerta=self.fabricarPuerta(hab1,hab2)
        hab1.sur=puerta
        hab2.norte=puerta
        self.laberinto.habitaciones.append(hab1)
        self.laberinto.habitaciones.append(hab2)
        return self.laberinto
    
    def laberinto2habitacionesFMBombasEste(self):
        pared=self.fabricarPared()
        paredBomba=self.fabricarParedBomba()
        hab1=self.fabricarHabitacion(pared,None,paredBomba, pared,1)
        hab2=self.fabricarHabitacion(None, pared, paredBomba, pared,2)
        puerta=self.fabricarPuerta(hab1,hab2)
        hab1.sur=puerta
        hab2.norte=puerta
        self.laberinto.habitaciones.append(hab1)
        self.laberinto.habitaciones.append(hab2)
        return self.laberinto
        
        
        
        
        
        
        
        