#Esta clase es un lado de la habitacion que no se puede atravesar


from Hoja import Hoja
class Puerta(Hoja):
    def __init__(self,lado1,lado2):
        self.abierta=False
        self.lado1=lado1
        self.lado2=lado2
        self.desc="soy una puerta"