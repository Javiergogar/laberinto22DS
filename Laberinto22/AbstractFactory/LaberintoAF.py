#Esta clase es la utilizada para implementar el patrón abstract factory
from Pared import Pared
from Puerta import Puerta
from ParedBomba import ParedBomba
from Habitacion import Habitacion
from Laberinto import Laberinto
from Bomba import Bomba
from Bicho import Bicho
from Agresivo import Agresivo
from Perezoso import Perezoso
from Norte import Norte
from Sur import Sur
from Este import Este
from Oeste import Oeste

class LaberintoAF:
    def __init__(self) -> None:
        pass
    
        # --FACTORYS--
        
    def fabricarPared(self):
        pared= Pared()
        return pared
    
    def fabricarPuerta(self,lado1,lado2):
        puerta= Puerta(lado1,lado2)
        puerta.lado1=lado1
        puerta.lado2=lado2
        return puerta
    
   
    def fabricarHabitacion(self,num):
        habitacion=Habitacion()
        habitacion.num=num
        habitacion.ponerEnEM(self.fabricarNorte(),self.fabricarPared())
        habitacion.ponerEnEM(self.fabricarSur(),self.fabricarPared())
        habitacion.ponerEnEM(self.fabricarEste(),self.fabricarPared())
        habitacion.ponerEnEM(self.fabricarOeste(),self.fabricarPared())
        habitacion.agregarOrientacion(self.fabricarNorte())
        habitacion.agregarOrientacion(self.fabricarSur())
        habitacion.agregarOrientacion(self.fabricarEste())
        habitacion.agregarOrientacion(self.fabricarOeste())
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
    
    def fabricarNorte(self):
        norte=Norte()
        return norte
    
    def fabricarEste(self):
        este=Este()
        return este
    
    def fabricarOeste(self):
        oeste=Oeste()
        return oeste
    
    def fabricarSur(self):
        sur=Sur()
        return sur  