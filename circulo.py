from objeto_metodo import Punto

class Circulo (Punto):
    def __init__(self, x, y, radio):
        super().__init__(x,y)
        self.radio = abs(radio)
    def obtenerDiametro(self,radio):
        diametro = 2*radio

        return diametro
    def obtenerPerimetro(self, radio):
        perimetro = 2*3,14159*radio
        return perimetro
    def obtenerArea(self, radio):
        area = 3,14159*radio*radio
        return area
    def __str__(self):
        return self.toString()