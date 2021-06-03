class Central():
    def __init__(self):
        self.num = b
        self.primerNum=False

    def abon(self):
        self.abonados = list(range(8380000,8380900))
        self.disponibles = random.sample(self.abonados, 585)
        self.abonados = set(self.abonados) - set(self.disponibles)
        self.ocupados = random.sample(self.abonados, 225)
        self.abonados = set(self.abonados) - set(self.ocupados)
        self.outser = random.sample(self.abonados, 90)
        return ("Los abonados",self.disponibles)
    def numero(self):
        print('El numero marcado es:', self.num)
        print("El estado disponible es: ", a.estadoDis())
        print("El estado ocupado es: ", a.estadoOc())
        print("El estado fuera de servicio es: ", a.estadoFue())
        x = a.estadoDis()
        y = a.estadoOc()
        z = a.estadoFue()
        if self.num < [8380001] or self.num > [8380900]:
            winsound.PlaySound("errada", winsound.SND_FILENAME)
        else:
            if x == True:
                print("Establaciendo llamada")
                winsound.PlaySound("tono", winsound.SND_FILENAME)
            if y == True:
                print("Numero ocupado")
                winsound.PlaySound("ocupado", winsound.SND_FILENAME)
            if z == True:
                print("Numero fuera de servicio")
                winsound.PlaySound("fueraS", winsound.SND_FILENAME)
        return self.num

    def estadoDis(self):
        c=self.num[0]
        if c in self.disponibles:
            self.estadoDisponible = True
            return self.estadoDisponible
        else:
            self.estadoDisponible = False
            return self.estadoDisponible
    def estadoOc(self):
        c = self.num[0]
        if c in self.ocupados:
            self.estadoOcupado = True
            return self.estadoOcupado
        else:
            self.estadoOcupado = False
            return self.estadoOcupado
    def estadoFue(self):
        c = self.num[0]
        if c in self.outser:
            self.estadoFuera = True
            return self.estadoFuera
        else:
            self.estadoFuera = False
            return self.estadoFuera