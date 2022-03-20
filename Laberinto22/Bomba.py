#Esta clase es un decorador para colocar bombas en elementos del mapa

from Decorator import Decorator

class Bomba(Decorator):
    def __init__(self):
        self.desc="soy una bomba"
        self.activa=False