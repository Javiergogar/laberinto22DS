#Esta clase representa una pared con una bomba
from Pared import Pared

class ParedBomba(Pared):
    def __init__(self):
        self.desc="soy una pared bomba"
        self.activa=False