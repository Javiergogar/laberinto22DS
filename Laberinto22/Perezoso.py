#Esta clase define el comportamiento mas tranquilo y dormilon del bicho
import time
from Modo import Modo
class Perezoso(Modo):
    def __init__(self):
        self.desc="soy un perezoso"
        
        
    def dormir(self):
        time.sleep(3)
        print("he esperado 3 segundos")