#Esta clase define la interface de los modos(agresivo y perezoso) del bicho

#Es donde implementamos el strategy

class Modo:
    def __init__(self):
        self.bicho=any
        self.desc="soy un modo"