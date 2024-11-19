
from televisores.tv import Tv

class Control:

    tv=tv.Tv





        # Metodos canal
    def canalUp(self):
        if self.tv.estado:
            if self.tv.canal >= 1 and self.tv.canal <= 119:
                self.tv.canal+=1
    def canalDown(self):
        if self.tv.estado:
            if self.tv.canal >= 2 and self.tv.canal <= 120:
                self.tv.canal-=1  
    def setCanal(self,canal):
        if self.tv.estado:
            if canal>=1 and canal <=120:
                self.tv.canal=canal
    

    # Metodos volumen

    def volumenUp(self):
        if self.tv.estado:
            if self.tv.volumen >= 0 and self.tv.volumen <= 6:
                self.tv.volumen+=1
    def volumenDown(self):
        if self.tv.estado:
            if self.tv.volumen >= 1 and self.tv.volumen <= 7:
                self.tv.volumen-=1
    def setVolumen(self,volumen):
        if self.tv.estado:
            if volumen <= 7 and volumen >=0:
                self.volumen=volumen



    def enlazar(self,tv):
        self.tv=tv
        tv.control=self
