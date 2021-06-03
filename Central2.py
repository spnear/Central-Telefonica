from Abonados import Abonados
class Central:
    numeroLocal = 0
    estado = 1
    def __init__(self,listaDisp,listaOcup,listaFs):
        self.listaDisp = listaDisp
        self.listaOcup = listaOcup
        self.listaFs = listaFs

    def buscarAbonado(self,numero):
        if numero in self.listaDisp:
            Central.estado = 1
        elif numero in self.listaOcup:
            Central.estado = 2
        elif numero in self.listaFs:
            Central.estado = 3
        else:
            Central.estado = 4
        return Central.estado
