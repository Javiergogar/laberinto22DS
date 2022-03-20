#Esta clase es la interface que define los decoradores
from ElementoMapa import ElementoMapa
class Decorator(ElementoMapa):
    def __init__(self):
        self.desc="soy un decorator"
        self.component=any