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
from Norte import Norte
from Sur import Sur
from Este import Este
from Oeste import Oeste

class Juego:
    def __init__(self):
        self.laberinto=Laberinto()
        self.bichos=[]
        self.desc="soy un juego"
        
    def agregarBichos(self,unBicho):
        self.bichos.append(unBicho)
        
    
    
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
    
    
    #  --CONSTRUCCIÓN DE LABERINTOS--
    
    def laberinto4habitacionesPr3(self):
        hab1=self.fabricarHabitacion(1)
        hab2=self.fabricarHabitacion(2)
        hab3=self.fabricarHabitacion(3)
        hab4=self.fabricarHabitacion(4)
        
        puerta1=self.fabricarPuerta(hab1,hab3)
        hab1.ponerEnEM(self.fabricarEste(),puerta1)
        hab3.ponerEnEM(self.fabricarOeste(),puerta1)
        
        puerta2=self.fabricarPuerta(hab3,hab4)
        hab3.ponerEnEM(self.fabricarSur(),puerta2)
        hab4.ponerEnEm(self.fabricarNorte(),puerta2)
        
        puerta3=self.fabricarPuerta(hab4,hab2)
        hab4.ponerEnEM(self.fabricarOeste(),puerta3)
        hab2.ponerEnEm(self.fabricarEste(),puerta3)
        
        puerta4=self.fabricarPuerta(hab2,hab1)
        hab2.ponerEnEM(self.fabricarNorte(),puerta4)
        hab1.ponerEnEM(self.fabricarSur(),puerta4)
        
        bicho1=self.fabricarBichoEn(self.fabricarAgresivo,hab1)
        bicho2=self.fabricarBichoEn(self.fabricarPerezoso,hab2)
        bicho3=self.fabricarBichoEn(self.fabricarAgresivo,hab3)
        bicho4=self.fabricarBichoEn(self.fabricarPerezoso,hab4)
        
        self.agregarBichos(bicho1)
        self.agregarBichos(bicho2)
        self.agregarBichos(bicho3)
        self.agregarBichos(bicho4)
        
        hab1.agregarHijo(self.fabricarBombaDecora())
        hab4.agregarHijo(self.fabricarBombaDecora())
        
        self.laberinto.agregarHabitaciones(hab1)
        self.laberinto.agregarHabitaciones(hab2)
        self.laberinto.agregarHabitaciones(hab3)
        self.laberinto.agregarHabitaciones(hab4)
        
        return self.laberinto
    
    
    #Estos ya no deberían de funcionar   
    """  def laberinto2habitacionesFM(self):
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
    
    def laberinto2habitaciones2BichosDec(self):
        pared=self.fabricarPared()
        bomba=self.fabricarBombaDecora(pared)
        hab1=self.fabricarHabitacion(pared,None, bomba, pared,1)
        hab2=self.fabricarHabitacion(None, pared, bomba, pared,2)
        puerta=self.fabricarPuerta(hab1,hab2)
        hab1.sur=puerta
        hab2.norte=puerta
        bichoAgr=self.fabricarBichoEn(self.fabricarAgresivo,hab1)
        bichoPer=self.fabricarBichoEn(self.fabricarPerezoso,hab2)
        self.agregarBichos(bichoAgr)
        self.agregarBichos(bichoPer)
        self.laberinto.habitaciones.append(hab1)
        self.laberinto.habitaciones.append(hab2)
        return self.laberinto
    """
    
    
    
        
        
        
        
        
        
        
        