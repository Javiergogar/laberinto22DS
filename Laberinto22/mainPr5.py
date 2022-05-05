from Juego import *
from Laberinto import *
from Pared import *
from Puerta import *
from ParedBomba import *
from Habitacion import *
from ElementoMapa import *
from Contenedor import *
from Orientacion import *
from AbstractFactory.LaberintoAF import *


#main para la prueba de la entrega de la practica 5
#En este caso el UML ha sido el mismo
#Utilizamos Abstract factory, implementado con la clase LaberintoAF en el paquete de nombre AbstractFactory y con el metodo laberinto4habitacionesAF en la clase Juego
af=LaberintoAF()
juegoPr5=Juego()
juegoPr5.laberinto=juegoPr5.laberinto4habitacionesAF(af)

print("Laberinto Práctica 5")

#Template para comprobar que se ha creado bien
print("Prueba para template")    #debe imprimir cosas distintas para los metodos dormir,atacar y moverme, en función de si es agresivo o perezoso
for i in juegoPr5.bichos:
    i.actua()

#Iterator para comprobar que se ha creado bien
print("Prueba para iterator")    
juegoPr5.laberinto.recorrer(juegoPr5.laberinto)  #recorre todos los contenedores del laberinto y en las habitaciones imprime un mensaje según la habitación que sea


#Singleton implementado en clases Nort,Sur,Este y Oeste
#Solo se puede crear una instancia de estas, en caso de ya existir saltara un mensaje de error y devuelve la misma instancia
print("Prueba para singleton")
norte=Norte()
sur=Sur()
este=Este()
oeste=Oeste()

