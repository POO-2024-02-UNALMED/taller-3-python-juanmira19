from control import Control

class Tv:
    control=control.Control
    canal=1
    volumen=1
    precio=500
    numTv=0

    def __init__(self,marca,estado):
        self.marca=marca
        self.estado=estado
        Tv.numTv+=1

    # Metodos control
    def getControl(self):
        return self.control
    def setControl(self,control):
        self.control=control

    # Metodos canal
    def getCanal(self):
        return self.canal
    def setCanal(self,canal):
        if self.estado:
            if canal>=1 and canal <=120:
                self.canal=canal
    def canalUp(self):
        if self.estado: 
            if self.canal >= 1 and self.canal <= 119:
                self.canal+=1
    def canalDown(self):
        if self.estado:
            if self.canal >= 2 and self.canal <= 120:
                self.canal-=1
    

    # Metodos volumen
    def getVolumen(self):
        return self.volumen
    def setVolumen(self,volumen):
        if self.estado:
            if volumen <= 7 and volumen >=0:
                self.volumen=volumen
    def volumenUp(self):
        if self.estado:
            if self.volumen >= 0 and self.volumen <= 6:
                self.volumen+=1
    def volumenDown(self):
        if self.estado:
            if self.volumen >= 1 and self.volumen <= 7:
                self.volumen-=1
        

    # Metodos precio
    def getPrecio(self):
        return self.precio
    def setPrecio(self,precio):
        self.precio=precio

    # Metodos marca
    def getMarca(self):
        return self.marca
    def setMarca(self,marca):
        self.marca=marca
        
    # Metodos de entado
    def turnOn(self):
        self.estado=True 
    def turnOff(self):
        self.estado=False



    @classmethod
    def getNumTv():
        return Tv.numTv
    def setNumTv(numTv):
        Tv.numTv=numTv
    def getEstado(self):
        return self.estado
        
    
    