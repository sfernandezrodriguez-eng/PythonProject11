
class Data:
    def __init__(self,dia,mes,ano):
        self.__dia = self.set(dd)
        self.__mes = self.set(mm)
        self.__ano = self.set(aaaa)

    def setAno(self,ano):
        if type(ano) == int:
            if ano > 0:
                self.__ano = ano
                return self.__ano
            else:
                self.ano = 0
                return self.__ano

    def eBisiesto(self,ano):
        if (ano % 4 == 0 and ano % 100 != 0) or ano %400 == 0:
            return True
        else:
            return False

    def setMes(self,mes):
        if type(mes) == int:
            if mes > 0 and mes< 13:
                self.__mes = mes
                return self.__mes
            else:

                self.mes = 0
                return self.__mes


    def setDia(self, dia):
           diaMes =  {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30, 10:31, 11:30, 12:31}
           if self.__mes is not None:
               if dia>0 and dia<=diaMes[self.__mes]:
                      self.__dia= dia


               else:
                if self.__mes == 2 and self.eBisiesto():
                        if dia>0 and dia<29:
                            self.__dia = dia

                        else:
                            self.__dia = None
                            self.__mes = None
                            self.__ano = None

    def getAno(self):
        return self.__ano

    def getMes(self):
        return self.__mes

    def getDia(self):
        return self.__dia

    def __str__(self):

        return f"Tus data es:{self.__dia}/{self.__mes}/{self.__ano} "

    dia = property(getDia,setDia)
    mes = property(getMes,setMes)
    ano = property(getAno,setAno)

data = Data(31,2,2025)
print(data)

