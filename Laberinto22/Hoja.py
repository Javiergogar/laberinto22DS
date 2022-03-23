#Una hoja es el componente simple del composite
from ElementoMapa import ElementoMapa


class Hoja(ElementoMapa):
    def __init__(self):
        self.desc="Soy una hoja"
        pass
        