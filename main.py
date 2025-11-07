
from circulo import Circulo
from objeto_metodo import Punto
from metodo_persoa import Persoa
from cilindro import Cilindro

p1 = Punto(2,3)
p2 = Punto(9,1)
p3 = Punto(5,10)
p4 = Punto(7,6)

print(p1.toString(),p2.toString(),p3.toString())

manuel= Persoa("manuel",dni="00000000X", edade=19,direccion="Garcia Barbon",nacionalidade="española" )
Pablo= Persoa("Pablo",  dni="00000000X", edade=19,direccion="hi",nacionalidade="española" )
print(manuel == Pablo)


circulo= Circulo( 3,4,5)
print(circulo.aCadea())

cilindro = Cilindro(2,3,4,6)
print(cilindro.aCadea(),"area : ",cilindro.obtenerArea(5),"volumen : ",cilindro.obtenerVolumen(9))