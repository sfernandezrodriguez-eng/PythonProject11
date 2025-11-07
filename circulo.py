from objeto_metodo import Punto

class Circulo (Punto):
    def __init__(self, x, y, radio):
        super().__init__(x,y)
        self.radio = abs(radio)
    def obtenerDiametro(self):


        return self.radio*2
    def obtenerPerimetro(self):
        return 2*math.pi*self.radio
    def obtenerArea(self, radio):
        area = 3,14159*radio*radio
        return area
    def __str__(self):
        return self.toString()