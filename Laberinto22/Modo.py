#Esta clase define la interface de los modos(agresivo y perezoso) del bicho

#Es donde implementamos el strategy
#También implementamos template, con actua

class Modo:
    def __init__(self):
        self.bicho=any
        self.desc="soy un modo"
        
    def actua(self):
        self.dormir()
        "self.atacar"    #de momento solo implementado dormir, el template funciona
        "self.moverme()"
        