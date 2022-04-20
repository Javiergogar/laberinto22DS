#Esta clase representa un enemigo del juego
#Template aqui con actua, delego en modo
class Bicho:
    def __init__(self):
        self.modo=any
        self.posicion=any
        self.desc="soy un bicho"
        
        
    def actua(self):
        self.modo.actua()