class Persoa:
    def __init__(self,nome,edade,dni,direccion,nacionalidade):
        self.nome = nome
        if self.comprobarEdade(edade):
           self.edade = edade
        else:
            edade = 0

        if self.comprobarDNI(dni):
           self.dni = dni
        else:
            self.dni="00000000X"
        self.direccion = direccion
        self.nacionalidade = nacionalidade
    def __str__(self):
        comprobacionPersoa= ("Tus datos son: \n\t Tu nombre es: "+str(self.nome)+"\n\t Tu edad es: "+ str(self.edade)+
                             "\n\t Tu DNI es: "+ (self.dni)+ "\n\t Tu direccion es: "+ str(self.direccion)+
                             "\n\t Tu nacionalidad es: "+ str(self.nacionalidade))
        return comprobacionPersoa
    def comprobarEdade(self, edade):
        if edade>=0 and edade < 150:
            return True
        else:
            return False
    def comprobarDNI(self,dni):
        if len(dni) == 9 and int(dni[:-1].isdigit()) and dni[-1:].isalpha() :
            letraDni = 'TRWAGMYFPDXBNJZSQVHLCKE'
            resto = int(dni[:-1]) % 23
            if letraDni[resto]== dni[-1:].upper():
                return True
        else:
            return False

        def __eq__(self, other):
            return self.dni == other.dni


