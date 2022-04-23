#Esta clase define el comportamiento mas tranquilo y dormilon del bicho
import time
from Modo import Modo
class Perezoso(Modo):
    def __init__(self):
        self.desc="soy un perezoso"
        
    #template    
    def dormir(self):
        time.sleep(5)
        print("he esperado 5 segundos")
        
    def atacar(self):
        print("Soy un bicho perezoso ataca tu")
        
    def moverme(self):
        print("Soy un bicho perezoso no se yo si me voy a mover")