#Esta clase es la interface que define los decoradores

from Hoja import Hoja
class Decorator(Hoja):
    def __init__(self):
        self.desc="soy un decorator"
        self.component=any