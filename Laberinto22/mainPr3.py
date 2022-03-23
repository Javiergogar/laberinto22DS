from Juego import *
from Laberinto import *
from Pared import *
from Puerta import *
from ParedBomba import *
from Habitacion import *
from ElementoMapa import *
from Contenedor import *


#main para la prueba de la entrega de la practica 2

#NOTA: no he podido hacer bien las comprobaciones porque no me entere que la entrega era para este fin de semana y lo he tenido que hacer deprisa y corriendo
#En caso de que me lo digas hago las comprobaciones mejor, porque si no no me da tiempo a entregarlo a la hora
#Lo mismo pasa con el UML que esta sin actualizar
juegoPr3=Juego()
juegoPr3.laberinto=juegoPr3.laberinto4habitacionesPr3()

hab1=juegoPr3.laberinto.habitaciones.pop(0)
hab2=juegoPr3.laberinto.habitaciones.pop(0)
hab3=juegoPr3.laberinto.habitaciones.pop(0)
hab4=juegoPr3.laberinto.habitaciones.pop(0)
print(juegoPr3.laberinto.habitaciones)
print("Laberinto Pr3")
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

print("Tercera habitación: "+hab3.desc)
print("Al sur hay: "+hab3.sur.desc)
print("Al norte hay: "+hab3.norte.desc)
print("Al este hay: "+hab3.este.desc)
print("Al oeste hay: "+hab3.oeste.desc)

print("Cuarta habitación: "+hab3.desc)
print("Al sur hay: "+hab3.sur.desc)
print("Al norte hay: "+hab3.norte.desc)
print("Al este hay: "+hab3.este.desc)
print("Al oeste hay: "+hab3.oeste.desc)





