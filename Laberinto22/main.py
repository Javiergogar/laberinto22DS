from Juego import *
from Laberinto import *
from Pared import *
from Puerta import *
from ParedBomba import *
from Habitacion import *
from ElementoMapa import *

#Genera un laberinto con dos habitaciones con una puerta al sur de una habitacion y al norte de la otra y en el resto de las orientaciones paredes
juegoSinBombas=Juego()
juegoSinBombas.laberinto=juegoSinBombas.laberinto2habitacionesFM()  #Aqui se usa el factory method
"print(juegoSinBombas.laberinto.habitaciones)"
hab1=juegoSinBombas.laberinto.habitaciones.pop(0)
hab2=juegoSinBombas.laberinto.habitaciones.pop(0)
print(juegoSinBombas.laberinto.habitaciones)
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

#Idem que el anterior pero colocando una pared bomba al este de las dos habitaciones
juegoBombasEste=Juego()
juegoBombasEste.laberinto=juegoBombasEste.laberinto2habitacionesFMBombasEste() #Aqui se usa el factory method
"print(juegoBombasEste.laberinto.habitaciones)"
hab1=juegoBombasEste.laberinto.habitaciones.pop(0)
hab2=juegoBombasEste.laberinto.habitaciones.pop(0)
print("Laberinto con bombas al este")
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


#He añadido a todas las clases un atributo desc para comprobar que esta bien, aunque debuggeando también se puede

print("prueba para git")



















