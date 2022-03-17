#Esta clase es el lado de una habitacion que no se puede atravesar
from ElementoMapa import ElementoMapa
class Pared(ElementoMapa):
    def __init__(self):
        self.desc="soy una pared"
       