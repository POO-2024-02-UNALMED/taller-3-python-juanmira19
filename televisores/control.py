from __future__ import annotations
from televisores.tv import TV
class Control:

    def __init__(self):
        self.tv=None

        # Metodos canal
    def canalUp(self):
        self.tv.canalUp()
            
    def canalDown(self):
        self.tv.canalDown()
    def setCanal(self,canal):
        self.tv.setCanal(canal)
    

    # Metodos volumen

    def volumenUp(self):
        self.tv.volumenUp()
    def volumenDown(self):
        self.tv.volumenDown()
    def setVolumen(self,volumen):
        self.tv.setVolumen(volumen)
    def turnOff(self):
        self.tv.turnOff()
    def turnOn(self):
        self.tv.turnOn()

    def setTv(self,tv):
        self.tv=tv
    def getTv(self):
        return self.tv
        





    def enlazar(self,tv):
        self.tv=tv
        tv.control=self
