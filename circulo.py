from objeto_metodo import Punto
import math
class Circulo (Punto):
    def __init__(self, x, y, radio):
        super().__init__(x,y)
        self.radio = abs(radio)
    def obtenerDiametro(self):
        return self.radio*2
    def obtenerPerimetro(self):
        return 2* math.pi *self.radio
    def obtenerArea(self):
        return math.pi*self.radio*self.radio
    def aCadea(self):
        cadea = super().toString() + "\n\t Radio : " + str(self.radio)
        return cadea