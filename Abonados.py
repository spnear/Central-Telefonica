import random
class Abonados:
    def __init__(self,prefijo):
        self.prefijo = prefijo
        self.lista = []
        self.listaOcupados = []
        self.listaFueraServicio = []
        self.total = 0


    def generarListaAbonados(self,cantidad):
        for i in range(0,cantidad):
             self.lista.append(self.prefijo*1000+i)
        self.total = len(self.lista)
        print("Total abonados:",self.total)
        return self.lista
    def generarEstadosAbonados(self,porcentajeOcupados,porcentajeFueraServicio):
        #Para ocupados
        for i in range(0,int(round(self.total*porcentajeOcupados))):
            muestra = random.choice(self.lista)
            self.listaOcupados.append(muestra)
            self.lista.remove(muestra)
            del muestra
        print("Total ocupados:",len(self.listaOcupados))
        #Para Fuera de servicio:
        for i in range(0,int(round(self.total * porcentajeFueraServicio))):
            muestra = random.choice(self.lista)
            self.listaFueraServicio.append(muestra)
            self.lista.remove(muestra)
            del muestra
        print("Total Fuera de servicio",len(self.listaFueraServicio))
        return (self.listaOcupados,self.listaFueraServicio)

a = Abonados(318)
a.generarListaAbonados(900)
a.generarEstadosAbonados(0.3,0.15)
disponible = a.lista

