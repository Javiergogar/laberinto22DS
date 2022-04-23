#Esta clase define la interface de los modos(agresivo y perezoso) del bicho

#Es donde implementamos el strategy
#También implementamos template, con actua

class Modo:
    def __init__(self):
        self.bicho=any
        self.desc="soy un modo"
    #template    
    def actua(self):
        self.dormir()
        self.atacar()    #implementados como prints, menos dormir que si espera
        self.moverme()
        