from Juego import *
from Laberinto import *
from Pared import *
from Puerta import *
from ParedBomba import *
from Habitacion import *
from ElementoMapa import *
from Contenedor import *


#main para la prueba de la entrega de la practica 4
juegoPr4=Juego()
juegoPr4.laberinto=juegoPr4.laberinto4habitacionesPr3()

print("Laberinto Práctica 4")

#Template implementado con el metodo actua en bichos que delega en modo y con dormir, atacar y moverme en agresivo y perezoso
print("Prueba para template")    #debe imprimir cosas distintas para los metodos dormir,atacar y moverme, en función de si es agresivo o perezoso
for i in juegoPr4.bichos:
    i.actua()

#Iterator implementado con los distintos metodos recorrer en las clases: ElementoMapa, Laberinto, Contenedor y Habitación
print("Prueba para iterator")    
juegoPr4.laberinto.recorrer(juegoPr4.laberinto)  #recorre todos los contenedores del laberinto y en las habitaciones imprime un mensaje según la habitación que sea


    