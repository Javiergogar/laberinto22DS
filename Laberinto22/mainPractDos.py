from Juego import *
from Laberinto import *
from Pared import *
from Puerta import *
from ParedBomba import *
from Habitacion import *
from ElementoMapa import *

juegoBichos=Juego()
juegoBichos.laberinto=juegoBichos.laberinto2habitaciones2BichosDec()

hab1=juegoBichos.laberinto.habitaciones.pop(0)
hab2=juegoBichos.laberinto.habitaciones.pop(0)
print(juegoBichos.laberinto.habitaciones)
print("Laberinto sin bombas")
print("Primera habitación: "+hab1.desc)
print("Al sur hay: "+hab1.sur.desc)
print("Al norte hay: "+hab1.norte.desc)
print("Al este hay: "+hab1.este.desc)
print("Al oeste hay: "+hab1.oeste.desc)

print("Segunda habitación: "+hab2.desc)
print("Al sur hay: "+hab2.sur.desc)
print("Al norte hay: "+hab2.norte.desc)
print("Al este hay: "+hab2.este.desc)
print("Al oeste hay: "+hab2.oeste.desc)