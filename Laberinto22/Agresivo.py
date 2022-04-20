#Esta clase define el comportamiento agresivo del bicho
import time
from Modo import Modo
class Agresivo(Modo):
    def __init__(self):
        self.desc="soy un agresivo"
        
        
    def dormir(self):
        time.sleep(3)
        print("he esperado 3 segundos")